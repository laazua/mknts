package main

import "fmt"

// 结构控制

func main() {
	// 简短声明并赋值
	len := 5

	// 条件判断
	if len > 5 {
		fmt.Println(">5")
	} else {
		fmt.Println("<5")
	}

	// if condition {
	//     some code
	// } else if condition {
	//     some code
	// } else {
	//     some code
	// }

	// 循环
	for len > 0 {
		fmt.Println(len)
		len--
	}

	// for {} 无线循环
	// goto
	// break, continue

	// switch
}
