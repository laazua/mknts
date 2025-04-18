// 程序控制流程
package main

import (
	"fmt"
)

func ifCondition(num int) {
	if num == 0 {
		fmt.Println("num = 0")
	} else if num > 0 {
		fmt.Println("num > 0")
	} else {
		fmt.Println("num < 0")
	}
}

func switchCondition(value int) {
	// 与if可以转换
	switch value {
	case 0:
		fmt.Println("value = 0")
	case 1:
		fmt.Println("value = 1")
	default:
		fmt.Println("value = ", value)
	}
}

func selectCondition(num int) {
	c := make(chan int, 10)
	select {
	// case 必须是一个chan操作,要么发送,要么接收
	case c <- num:
		fmt.Println("c = ", c)
	case c <- 0:
		fmt.Println("c = ", c)
	default:
		fmt.Println("这是个select例子")
	}
}

func forControl(num int) {
	for i := 0; i < num; i++ {
		fmt.Println("i = ", i)
	}

	// for conditon {}
	// for {} 无限循环
	// 配合break, continue, goto,range使用
}

func main() {
	ifCondition(100)
	switchCondition(10)
	selectCondition(20)
	forControl(5)
}
