//bufio包实现了有缓冲的I/O。它包装一个io.Reader或io.Writer接口对象，
//创建另一个也实现了该接口，且同时还提供了缓冲和一些文本I/O的帮助函数的对象
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// create a write buffer object
	w := bufio.NewWriter(os.Stdout)
	fmt.Fprintf(w, "Hello, ")
	fmt.Fprintf(w, "world!")
	w.Flush() // Don't forget to flush
}
