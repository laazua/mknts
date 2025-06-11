package server

import (
	"errors"
	"fmt"
	"io"
	"net"
	"sync"
	"time"

	"sksrv/pkg/codec"
	"sksrv/pkg/comm"
)

// Handler 消息处理器接口
type Handler interface {
	Handle(conn *Conn, msg *comm.Message) error
}

// HandlerFunc 是一个适配器，允许普通函数作为Handler使用
type HandlerFunc func(conn *Conn, msg *comm.Message) error

// Handle 实现Handler接口
func (f HandlerFunc) Handle(conn *Conn, msg *comm.Message) error {
	return f(conn, msg)
}

// Middleware 中间件接口
type Middleware func(next Handler) Handler

type Server struct {
	address     string
	listener    net.Listener
	handler     Handler
	middlewares []Middleware
	codec       codec.Codec
	wg          sync.WaitGroup
	quit        chan struct{}
	connections sync.Map
}

// NewServer 创建TCP服务器
func NewServer(address string, codec codec.Codec) *Server {
	return &Server{
		address:     address,
		codec:       codec,
		quit:        make(chan struct{}),
		middlewares: make([]Middleware, 0),
	}
}

// Use 添加中间件
func (s *Server) Use(middleware Middleware) {
	s.middlewares = append(s.middlewares, middleware)
}

// SetHandler 设置处理器
func (s *Server) SetHandler(handler Handler) {
	// 应用中间件
	h := handler
	for i := len(s.middlewares) - 1; i >= 0; i-- {
		h = s.middlewares[i](h)
	}
	s.handler = h
}

// Start 启动服务器
func (s *Server) Start() error {
	var err error
	s.listener, err = net.Listen("tcp", s.address)
	if err != nil {
		return fmt.Errorf("listen error: %v", err)
	}

	fmt.Printf("TCP server started on %s\n", s.address)

	s.wg.Add(1)
	go s.acceptConn()

	// 启动心跳检测
	s.wg.Add(1)
	go s.heartbeatCheck()

	return nil
}

// Stop 停止服务器
func (s *Server) Stop() {
	close(s.quit)
	s.listener.Close()
	s.wg.Wait()
	fmt.Println("TCP server stopped")
}

// acceptConnections 接受连接
func (s *Server) acceptConn() {
	defer s.wg.Done()

	for {
		select {
		case <-s.quit:
			return
		default:
			conn, err := s.listener.Accept()
			if err != nil {
				if !errors.Is(err, net.ErrClosed) {
					fmt.Printf("accept error: %v\n", err)
				}
				continue
			}

			connection := NewConn(conn, s.codec)
			s.connections.Store(conn.RemoteAddr().String(), connection)

			s.wg.Add(1)
			go s.handleConn(connection)
		}
	}
}

// handleConnection 处理连接
func (s *Server) handleConn(conn *Conn) {
	remoteAddress := conn.GetRemoteAddress()
	defer func() {
		conn.Close()
		s.connections.Delete(remoteAddress.String())
		s.wg.Done()
	}()

	fmt.Printf("Client connected: %s\n", remoteAddress)

	for {
		select {
		case <-s.quit:
			return
		default:
			msg, err := conn.ReceMessage()
			if err != nil {
				if err == io.EOF {
					fmt.Printf("Client disconnected: %s\n", remoteAddress)
				} else {
					fmt.Printf("Read error from %s: %v\n", remoteAddress, err)
				}
				return
			}

			if err := s.handler.Handle(conn, msg); err != nil {
				fmt.Printf("Handle message error: %v\n", err)
				return
			}
		}
	}
}

// heartbeatCheck 心跳检测
func (s *Server) heartbeatCheck() {
	defer s.wg.Done()

	ticker := time.NewTicker(comm.BeatInterval)
	defer ticker.Stop()

	for {
		select {
		case <-s.quit:
			return
		case <-ticker.C:
			s.connections.Range(func(key, value interface{}) bool {
				conn := value.(*Conn)
				if time.Since(conn.GetLastActiveTime()) > comm.BeatInterval*2 {
					fmt.Printf("Client %s timeout, closing connection\n", conn.GetRemoteAddress())
					conn.Close()
					s.connections.Delete(key)
				}
				return true
			})
		}
	}
}
