// ip信息查询
package main

import (
	"embed"
	"fmt"
	"log/slog"
	"net"
	"sync"

	"github.com/oschwald/geoip2-golang"
)

var wg sync.WaitGroup

//go:embed db/GeoLite2-City.mmdb
var dbFile embed.FS

func SearchIp(ips []string) {
	// 读取嵌入的 GeoLite2-City.mmdb 文件
	data, err := dbFile.ReadFile("db/GeoLite2-City.mmdb")
	if err != nil {
		slog.Error("Error reading embedded file: ", err.Error())
		return
	}
	db, err := geoip2.FromBytes(data)
	if err != nil {
		slog.Error(err.Error())
		return
	}
	defer db.Close()
	defer func(db *geoip2.Reader) {
		err := db.Close()
		if err != nil {
			slog.Error(err.Error())
			return
		}
	}(db)

	resultChan := make(chan string, len(ips))
	for _, ip := range ips {
		iP := net.ParseIP(ip)
		if iP == nil {
			slog.Info("Invalid IP address ", slog.String("ip", ip))
			continue
		}
		wg.Add(1)
		go executeQuery(db, iP, resultChan)
	}
	wg.Wait()
	close(resultChan)
	for result := range resultChan {
		fmt.Println(result)
	}
}

func executeQuery(db *geoip2.Reader, ip net.IP, resultChan chan<- string) {
	defer wg.Done()
	record, err := db.City(ip)
	if err != nil {
		resultChan <- fmt.Sprintf("Error querying IP %s: %v", ip.String(), err)
		return
	}

	// 你可以根据需要提取更详细的记录信息，以下是一个简单的例子
	result := fmt.Sprintf("IP: %s, City: %s, Country: %s", ip.String(), record.City.Names["en"], record.Country.Names["en"])
	resultChan <- result
}
