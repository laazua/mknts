// go mod init moduleDemo  这里的moduleDemo要与项目名字一致
package main

import (
	"fmt"
	"moduleDemo/pkg1"
	"moduleDemo/pkg2"
)

func init() {
	fmt.Println("main init")
}

func main() {
	fmt.Println("main func")
	pkg1.Test()
	pkg2.Test()
}
