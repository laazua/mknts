// go mod init helloWorld  这里的helloWorld要与项目名字一致

package main

import (
	"fmt"
	"helloWorld/test"
)

func main() {
	fmt.Println("main func")
	test.Test()
}
