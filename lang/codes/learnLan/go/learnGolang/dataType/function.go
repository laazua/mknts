// 函数
package main

import "fmt"

// func funcName(arg1 type1, arg2 type2) (type1, type2){
//     code statment
//     return value1, value2
// }

// go默认函数传参是值传递
func add(num1, num2 int) int {
	return num1 + num2
}

func main() {
	num := add(1, 2)
	fmt.Println("num = ", num)

	// 匿名函数
	anonymous := func(name string) {
		fmt.Println("我是匿名函数:", name)
	}
	anonymous("anonmous")

	// 延迟函数
	defer func(a, b string) {
		fmt.Println(a + b)
	}("a", "b")

	// 传多个参数
	argsTest(1, 2, "ab")
}

// 函数传入多个不定参数语法
func argsTest(arg ...interface{}) {
	for i := range arg {
		fmt.Println(i)
	}
}
