package tcpsocket

import (
	"fmt"
	"net"
	"os"

	"../protocol"
)

func RunService() {
	netListen, err := net.Listen("tcp", ":8888")
	CheckErr(err)
	defer netListen.Close()

	fmt.Println("Waiting for clients...")

	for {
		conn, err := netListen.Accept()
		if err != nil {
			continue
		}
		fmt.Println(conn.RemoteAddr().String(), " tcp conet success.")
		go handlerConnection(conn)
	}

}

func handlerConnection(conn net.Conn) {
	// 声明临时缓冲区,存储被截断的数据
	tmpBuf := make([]byte, 0)

	// 声明管道,接受解包数据
	readerChan := make(chan []byte, 16)
	go reader(readerChan)

	buf := make([]byte, 1024)
	for {
		n, err := conn.Read(buf)
		if err != nil {
			fmt.Println(conn.RemoteAddr().String(), "connection error: ", err)
			return
		}
		fmt.Println(conn.RemoteAddr().String(), " Receive data, length: ", n)
		tmpBuf = protocol.Unpack(append(tmpBuf, buf[:n]...), readerChan)
	}
}

func reader(readerChan chan []byte) {
	for {
		select {
		case data := <-readerChan:
			fmt.Println(string(data))
		}
	}
}

func CheckErr(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
	}
}
