package main

import (
	"time"

	"./tcpsocket"
)

func main() {
	// runChan := make(chan []byte, 1)
	go tcpsocket.RunService()

	time.Sleep(1 * time.Millisecond)

	go tcpsocket.RunClient()
	// <-runChan
}
