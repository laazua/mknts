// go 传统启动tcp server
package main

import (
	"fmt"
	"net"
)

func main() {
	/*
	   流程:
	   1 创建addr
	   2 创建监听句柄
	   3 获取连接句柄
	   4 业务处理
	*/
	NewServe("0.0.0.0", 8888)

	// 阻塞
	select {}
}

func NewServe(ip string, port int) {
	go func() {
		addr, err := net.ResolveTCPAddr("tcp4", fmt.Sprintf("%s:%d", ip, port))
		if err != nil {
			fmt.Println("Resolve tcp addr error: ", err)
			return
		}

		// 开启一个监听句柄
		listen, err := net.ListenTCP("tcp4", addr)
		if err != nil {
			fmt.Println("Get listen error: ", err)
			return
		}

		fmt.Printf("[start] listen on %s:%d...\n", ip, port)

		for {
			conn, err := listen.AcceptTCP()
			if err != nil {
				fmt.Println("conn error: ", err)
				continue
			}

			fmt.Printf("client ip: %s connected\n", conn.RemoteAddr())

			// 业务实现
			go func() {
				for {
					buffer := make([]byte, 1024)
					cnt, err := conn.Read(buffer)
					if err != nil {
						fmt.Println("Recive buffer error: ", err)
						continue
					}

					// 回显业务
					if _, err := conn.Write(buffer[:cnt]); err != nil {
						fmt.Println("Write buffer error: ", err)
						continue
					}
				}
			}()
		}
	}()
}
