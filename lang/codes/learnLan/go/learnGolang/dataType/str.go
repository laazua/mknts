package main

import (
	"bytes"
	"fmt"
	"strings"
)

func main() {
	// 字符串拼接的5种方式
	ret := addMethod("aa", "bb")
	fmt.Println(ret)
  
        ret = sprintf("cc", "dd")
        fmt.Println(ret)
  
        ret = stringsBuilder("ee", "ff")
        fmt.Println(ret)
  
        ret = bytesBuffer("gg", "hh")
        fmt.Println(ret)
  
        ret = sliceByte("ii", "jj")
        fmt.Println(ret)
}

func addMethod(a, b string) string {
	// 效率不高
	return a + b
}

func sprintf(a, b string) string {
	// 不高效
	return fmt.Sprintf("%s%s", a, b)
}

func stringsBuilder(a, b string) string {
	// strings.Builder
	var builder strings.Builder
	builder.WriteString(a)
	builder.WriteString(b)
	return builder.String()
}

func bytesBuffer(a, b string) string {
	// bytes.Buffer
	buffer := new(bytes.Buffer)
	buffer.WriteString(a)
	buffer.WriteString(b)
	return buffer.String()
}

func sliceByte(a, b string) string {
	// []byte
	buffer := make([]byte, 0)
	buffer = append(buffer, a...)
	buffer = append(buffer, b...)
	return string(buffer)
}
