package network

import (
	"fmt"
	"io/ioutil"
	"net"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s host:port\n", os.Args)
		os.Exit(1)
	}
    service := os.Args[1]

    //解析地址&端口
    tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
    checkError(err)

    //建立连接
    conn, err := net.DialTCP("tcp", nil, tcpAddr)
    checkError(err)

    _, err = conn.Write([]byte("HEAD / HTTP/1.0\r\n\r\n"))
    checkError(err)

    result, err := ioutil.ReadAll(conn)
    checkError(err)

    fmt.Println(string(result))

    os.Exit(0)
}

func checkError1(err error) {
    if err != nil {
    	fmt.Fprintf(os.Stderr, "Fatal error: %s\n", err.Error())
    	os.Exit(1)
	}
}
/*
func net.ParseIP()    验证地址的有效性
func IPv4Mask(a, b, c, d byte) IPMask    创建默认子网掩码
func (ip IP) DefaultMask() IPMask        获取默认子网掩码
根据域名查找ip:
func ResolveIPAddr(net, addr string) (*IPAddr, error)
func LookupHost(name string) (cname string, addrs []string, err error);
*/