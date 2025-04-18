package main

import "fmt"

func main() {
	server := NewServer(WithPort("8080"), WithHost("localhost"))
	fmt.Println(server)
}

type Server struct {
	Port string
	Host string
}

type Option func(s *Server)

func WithPort(port string) Option {
	return func(s *Server) {
		s.Port = port
	}
}

func WithHost(host string) Option {
	return func(s *Server) {
		s.Host = host
	}
}

func NewServer(options ...Option) *Server {
	s := &Server{
		Port: "8080",
		Host: "localhost",
	}
	for _, option := range options {
		option(s)
	}
	return s
}
