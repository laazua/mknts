package code

import (
	"fmt"
	"net"
)

// ip address
func ParseIp(ip string) {
	addr := net.ParseIP(ip)
	if addr == nil {
		fmt.Println("Invaild ip")
	} else {
		fmt.Println("ip: ", addr)
	}
}

// ip mask
