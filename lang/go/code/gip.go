// go build -o gip

package main

import (
	"flag"
	"fmt"
	"net"
	"os"
	"regexp"
)

var ip string

func main() {
	flag.StringVar(&ip, "ip", "127.0.0.1", "ip address")
	flag.Parse()
	if len(os.Args) != 3 {
		flag.Usage()
		return
	}
	if !checkIp(ip) {
		fmt.Println("IP 格式不正确!")
		return
	}
	// 解析IP地址
	ip := net.ParseIP(ip)
	if ip == nil {
		fmt.Println("错误: 无效的IP地址格式")
		return
	}

	// 根据IP类型获取默认掩码
	var mask net.IPMask
	if ip.To4() != nil {
		// IPv4地址 - 使用默认类掩码
		mask = defaultIPv4Mask(ip)
	} else {
		// IPv6地址 - 使用标准/64掩码
		mask = net.CIDRMask(64, 128)
	}

	// 输出结果
	fmt.Printf("%-18s %-18s\n", "IP Address:", ip)
	fmt.Printf("%-18s %-18s\n", "Mask Addresss:", net.IP(mask))
	fmt.Printf("%-18s %-18s\n", "Network Address:", networkAddress(ip, mask))
}

// 根据IPv4地址类别返回默认掩码
func defaultIPv4Mask(ip net.IP) net.IPMask {
	firstOctet := ip.To4()[0]

	switch {
	case firstOctet < 128: // A类
		return net.CIDRMask(8, 32)
	case firstOctet < 192: // B类
		return net.CIDRMask(16, 32)
	case firstOctet < 224: // C类
		return net.CIDRMask(24, 32)
	default: // D类和E类
		return net.CIDRMask(32, 32)
	}
}

// 计算网络地址
func networkAddress(ip net.IP, mask net.IPMask) net.IP {
	return ip.Mask(mask)
}

func checkIp(ip string) bool {
	ipv4Regex := regexp.MustCompile(`^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$`)
	return ipv4Regex.MatchString(ip)
}

