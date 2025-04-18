package server

import (
	"bufio"
	"fmt"
	"log"
	"log/slog"
	"net"
	"sync"

	"github.com/spf13/viper"
)

type client struct {
	nickname string
	conn     net.Conn
}

type ChatServer struct {
	entry    chan client
	leave    chan client
	messages chan string
	clients  map[net.Conn]client
	mutex    sync.Mutex
}

func NewChatServer() *ChatServer {
	return &ChatServer{
		entry:    make(chan client),
		leave:    make(chan client),
		messages: make(chan string),
		clients:  make(map[net.Conn]client),
	}
}

func (cs *ChatServer) broadcaster() {
	for {
		select {
		case msg := <-cs.messages:
			cs.mutex.Lock()
			for conn := range cs.clients {
				fmt.Fprintf(conn, "%v\n", msg)
			}
			cs.mutex.Unlock()
		case cli := <-cs.entry:
			cs.mutex.Lock()
			cs.clients[cli.conn] = cli
			for _, c := range cs.clients {
				if c.conn != cli.conn {
					fmt.Fprintf(cli.conn, c.nickname+" has entered\n")
				}
			}
			cs.mutex.Unlock()
		case cli := <-cs.leave:
			cs.mutex.Lock()
			delete(cs.clients, cli.conn)
			cli.conn.Close()
			for _, c := range cs.clients {
				fmt.Fprintf(c.conn, cli.nickname+" has left\n")
			}
			cs.mutex.Unlock()
		}
	}
}

func (cs *ChatServer) handleConn(conn net.Conn) {
	ch := make(chan string)
	go cs.clientWriter(conn, ch)

	// fmt.Fprint(conn, "Enter your nickname: ")
	input := bufio.NewScanner(conn)
	var who string
	if input.Scan() {
		who = input.Text()
	}
	cli := client{conn: conn, nickname: who}
	ch <- who
	cs.messages <- who + " has arrived"
	cs.entry <- cli

	for input.Scan() {
		cs.messages <- who + ": " + input.Text()
	}

	cs.leave <- cli
	cs.messages <- who + " has left"
	conn.Close()
}

func (cs *ChatServer) clientWriter(conn net.Conn, ch <-chan string) {
	for msg := range ch {
		fmt.Fprintln(conn, msg)
	}
}

func (cs *ChatServer) Run() {

	listener, err := net.Listen("tcp", viper.GetString("server.addr"))
	if err != nil {
		log.Fatal(err)
	}
	slog.Info("聊天服务已启动...")
	defer listener.Close()

	go cs.broadcaster()

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Print(err)
			continue
		}
		go cs.handleConn(conn)
	}
}
