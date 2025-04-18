/*
socket编程一般步骤:
    建立socket:  socket()函数
    绑定socket:  bind()函数
    监听:        listen()函数    或者连接:   connect()
    接受连接:    accept()函数
    接受数据:    receive()函数    或者发送数据:   send()函数

go语言标准库对此过程进行了抽象和封装,无论使用什么样形式连接,只需要调用net.Dial()即可:
    func Dial(net, addr string) (Conn, error)
    net: 网络协议
    addr: ip地址或域名:port
    Conn: 连接对象
    error: 错误
例子:
    tcp: conn, err := net.Dial("tcp", "127.0.0.1:8000")
    udp: conn, err := net.Dial("udp", "127.0.0.1:8000")
    icmp(协议名称链接): conn, err := net.Dial("ip4:icmp", "www.baidu.com")
    icmp(协议编号连接): conn, err := net.Dial("ip4:1", "127.0.0.1")
*/
package network

import(
	"bytes"
	"fmt"
	"io"
	"net"
	"os"
)

func main()  {
	if len(os.Args) != 2 {
		fmt.Println("Usage: ", os.Args[0], "host")
		os.Exit(1)
	}
	service := os.Args[1]

	conn, err := net.Dial("ip4:icmp", service)
	checkError(err)

	var msg [512]byte
	msg[0] = 8    //echo
	msg[1] = 0    //code 0
	msg[2] = 0    //checksum
    msg[3] = 0    //checksum
    msg[4] = 0    //identifier[0]
    msg[5] = 13   //identifier[1]
    msg[6] = 0    //sequence[0]
    msg[7] = 37   //sequence[1]
    len := 8
    check := checkSum(msg[0:len])
    msg[2] = byte(check >> 8)
    msg[3] = byte(check & 255)

    _, err = conn.Write(msg[0:len])
    checkError(err)

    fmt.Println("Got response")
    if msg[5] == 13 {
    	fmt.Println("Identifier matches")
	}
	if msg[7] == 37 {
		fmt.Println("Sequence matches")
	}
	os.Exit(0)
}

func checkSum(msg []byte) uint16 {
	sum := 0

	//先假设为偶数
	for n := 1; n <len(msg)-1; n += 2 {
		sum += int(msg[n]) * 256 + int(msg[n+1])
	}
	sum = (sum >> 16) + (sum & 0xffff)
	sum += (sum >> 16)
	var answer uint16 = uint16((^sum))
	return answer
}

func checkError(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
		os.Exit(1)
	}
}

func readFully(conn net.Conn) ([]byte, error) {
    defer conn.Close()

    result := bytes.NewBuffer(nil)
    var buf [512]byte
    for {
    	n, err := conn.Read(buf[0:])
    	result.Write(buf[0:n])
    	if err != nil {
    		if err == io.EOF {
    			break
			}
			return nil, err
		}
	}
	return  result.Bytes(), nil
}

