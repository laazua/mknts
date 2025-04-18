//函数
package main

import (
	"fmt"
)

func main() {
	//基本组成: func关键字, 函数名, 参数列表, 返回值, 函数体, 返回语句
	// func functionName(arg1 type1, arg2 type2, ...) (val1 type1, val2 type2, ...) {
	//     ...
	//     return val1, val2, ...
	// }

	//函数调用,导入函数所在的包,包名.函数名,如: r := math.Add(1,2)
	closureTest()

	//当可变参是一个空接口类型时,调用者是否解包可变参会导致不同结果
	var a = []interface{}{123, "abc"}
	Print(a...)    //123 abc
	Print(a)       //[123, abc]
}

func Print(a ...interface{}) {
	fmt.Println(a...)
}

//不定参数(...type语法糖, 任意类型的不定参数...interface{})
func argsTest(args ...int) {
	//接受不定数量的参数,参数类型全部是int
	for _, v := range args {
		fmt.Println(v)
	}
}

//具名函数
func add(x, y int) int {
	return x + y
}

//多个参数，多个返回值
func Swap(a, b int) (int, int) {
	return b, a
}

//匿名函数
var Add = func(x, y int) int {
	return x + y
}

//闭包
func closureTest() {
	var j int = 3
	f := func() (func()) {
		var i int = 2
		return func() {
			fmt.Println("i: ", i, "j: ", j)
		}
	}()
	f()
	j = 4
	f()

	//f指向的闭包函数引用了局部变量i和j,i的值被隔离,在闭包外不能被修改,j的值修改后,调用f结果是修改后的值
}