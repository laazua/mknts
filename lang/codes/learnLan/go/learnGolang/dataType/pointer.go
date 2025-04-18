// 指针
package main

import "fmt"

func main() {
	// 声明一个整型指针变量, 并初始化为nil
	var p *int = nil
	// 声明并初始化一个整型变量
	a := 10
	// 将指针P指向a所在的内存地址
	p = &a
	fmt.Println(*p)
}
