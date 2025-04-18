// bytes package: 实现了操作[]byte的常用函数,该包的函数与string包类似
package main

import (
	"bytes"
	"fmt"
	"os"
)

func main() {
	b := bytes.Buffer{}
	b.Write([]byte("hellow "))
	fmt.Fprintf(&b, "world!")
	b.WriteTo(os.Stdout)
}
