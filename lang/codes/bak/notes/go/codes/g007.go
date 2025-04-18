package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println("运行前...")
	// 允许一段手动触发的错误
	ProtectRun(func() {
		fmt.Println("手动崩溃程序前")
		// 使用panic传递上下文
		panic("手动触发panic")
		// fmt.Println("手动崩溃程序后")
	})

	// 空指针访问错误
	ProtectRun(func() {
		fmt.Println("赋值崩溃前")
		var a *int
		*a = 1
		fmt.Println("赋值崩溃后")
	})
	fmt.Println("运行后...")
}

func ProtectRun(entry func()) {
	// 延迟处理函数
	defer func() {
		// 发生崩溃,获取panic传递的上下文并打印
		err := recover()
		switch err.(type) {
		case runtime.Error:
			fmt.Println("runtime error: ", err)
		default:
			fmt.Println("error: ", err)
		}
	}()
	entry()
}
