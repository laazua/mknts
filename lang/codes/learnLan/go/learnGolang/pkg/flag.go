// flag包,命令行参数解析
package main

import (
	"flag"
	"fmt"
)

func main() {
	// 方式1
	name := flag.String("name", "test name", "this is a test parameter.")

	// 方式2
	var person string
	flag.StringVar(&person, "person", "test person", "this is a test parameter.")

	flag.Parse()

	// 使用命令行传入的参数
	fmt.Println("name:", *name)
	fmt.Println("person:", person)
}
