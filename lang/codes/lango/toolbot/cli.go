// 解析命令行参数
package main

import (
	"flag"
	"fmt"
	"os"
	"strings"
)

var cmdFlag struct {
	Help *bool
	Ip   string
	Mod  string // cli | web
}

func init() {
	cmdFlag.Help = flag.Bool("help", false, "help message")
	flag.StringVar(&cmdFlag.Mod, "mod", "", "use mod: [cli|web].")
	flag.StringVar(&cmdFlag.Ip, "ip", "", "ip list you want to query.")

	flag.Usage = func() {
		fmt.Printf("Usage:\n  %v -mod web\n  %v -mod cli -ip 127.0.0.1,127.0.0.2\n\n", os.Args[0], os.Args[0])
		flag.PrintDefaults()
		os.Exit(0)
	}
	flag.Parse()
	argc := len(os.Args)
	if argc != 3 && argc != 5 {
		flag.Usage()
	}
	if cmdFlag.Mod == "cli" && cmdFlag.Ip == "" {
		flag.Usage()
	}
	if cmdFlag.Mod == "web" && cmdFlag.Ip != "" {
		flag.Usage()
	}
}

func parseIpFlag(ips string) []string {
	if ips == "" {
		return nil
	}
	return strings.Split(ips, ",")
}
