// go涉及到的数据类型: 字符串,布尔，数字，复数, 其他(struct, chan, 指针, map, array, slice, interface等)
package main

import "fmt"

func main() {
	// 变量声明: var variableName type, 如果变量声明没有初始化,则其值为它当前类型的默认值.
	// 变量声明并赋值: var variableName = ""abc; variableName := "abc"
	// 常量声明: const variableName = 100

	// 字符串: 用双引号("")或(``)括起来的,不能用('')定义
	s := "abcefghijklmnopqrstuvwxyz"
	fmt.Printf("%v\n", s[2:6])
	fmt.Printf("%#v\n", s)
	fmt.Printf("%q\n", s)
	fmt.Printf("%v\n", s+s)

	// 布尔: true, false
	fmt.Printf("%t\n", true)

	// byte type 与uint8是同一类型

	// rune type 与int32是同一类型

	// 数字: int8, uint8; int16, uint16; int32, uint32; int64, uint64; int, uint(根据操作系统架构确定位数)
	//       float32, float64

	// complex64  complex128复数类型

	// uintptr 可以保存任意指针的位模式的整数类型

	// error类型 内建error接口类型,约定用于表示错误信息,nil表示没有错误.
	n := 12
	var m int = 15
	fmt.Printf("%v, %v\n", n, m)
}
