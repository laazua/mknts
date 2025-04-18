package client

import (
	"bufio"
	"fmt"
	"net"
	"os"

	"github.com/spf13/viper"
)

type ChatClient struct {
	conn net.Conn
}

func NewChatClient() *ChatClient {
	return &ChatClient{}
}

func (cc *ChatClient) connect(address string) error {
	conn, err := net.Dial("tcp", address)
	if err != nil {
		return err
	}
	cc.conn = conn
	return nil
}

func (cc *ChatClient) Run() {
	cc.connect(viper.GetString("server.addr"))
	go cc.receiveMessages()
	cc.sendMessages()
}

func (cc *ChatClient) receiveMessages() {
	scanner := bufio.NewScanner(cc.conn)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}

func (cc *ChatClient) sendMessages() {
        fmt.Println("Enter your nickname: ")
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		input := scanner.Text()
		fmt.Fprintf(cc.conn, "%s\n", input)
	}
}

func (cc *ChatClient) Close() {
	cc.conn.Close()
}
