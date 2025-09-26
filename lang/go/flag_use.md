### flag

- **命令分组解析**
```go
package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	// 定义全局 Flag
	var verbose bool
	flag.BoolVar(&verbose, "v", false, "Enable verbose mode")

	// 定义子命令（使用 FlagSet 实现分组）
	serverCmd := flag.NewFlagSet("server", flag.ExitOnError)
	serverPort := serverCmd.Int("port", 8080, "Server port")
	serverHost := serverCmd.String("host", "127.0.0.1", "Server host")

	clientCmd := flag.NewFlagSet("client", flag.ExitOnError)
	clientAddr := clientCmd.String("addr", "127.0.0.1:8080", "Server address")

	// 解析顶层 flag
	flag.Parse()
	if len(os.Args) < 2 {
		fmt.Println("expected 'server' or 'client' subcommands")
		os.Exit(1)
	}

	switch os.Args[1] {
	case "server":
		// 解析 server 子命令的参数
		serverCmd.Parse(os.Args[2:])
		fmt.Printf("Run server at %s:%d\n", *serverHost, *serverPort)
		if verbose {
			fmt.Println("Verbose mode enabled")
		}
	case "client":
		// 解析 client 子命令的参数
		clientCmd.Parse(os.Args[2:])
		fmt.Printf("Connect to %s\n", *clientAddr)
		if verbose {
			fmt.Println("Verbose mode enabled")
		}
	default:
		fmt.Println("expected 'server' or 'client' subcommands")
		os.Exit(1)
	}
}

```
