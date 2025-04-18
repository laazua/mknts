package main

import (
	"fmt"
	"os"
)

/* 函数 */

func main() {

	// 声明一个函数类型(回调函数)
	var callBack func(int, int) int

	callBack = avg

	res := callBack(4, 6)
	fmt.Println("res is ", res)

	//////////////////////////////
	// 声明一个接口变量
	var a actor
	// 实例化结构体
	p := new(Person) // 或者 p := &Person
	// 将示例化的结构体赋值给接口变量
	a = p

	// 用接口变量调用结构体方法
	a.SayName("ZhangSan")
	a.SayAge(20)

	// 闭包调用
	ad := add(2)
	fmt.Println(ad())
	fmt.Printf("%p\n", &ad)

	// 闭包生成一个人
	p1 := GenPerson("Lisi", "男")
	p2 := GenPerson("Cuihua", "女")
	fmt.Println(p1())
	fmt.Println(p2())
}

// 函数
func avg(a int, b int) int {
	return (a + b) / 2
}

// 接口函数实现
type Person struct {
	name string
	age  uint
}

type actor interface {
	SayName(string)
	SayAge(uint)
}

// 用结构体去实现actor接口中的方法
func (p *Person) SayName(name string) {
	fmt.Println("My Name Is ", name)
}

func (p *Person) SayAge(age uint) {
	fmt.Println("My Age Is ", age)
}

// 闭包
func add(v int) func() int {
	return func() int {
		v++
		return v
	}
}

// 闭包一般用于生成器
func GenPerson(name, sex string) func() (string, string, string) {
	// 出生地,不变的地址
	address := "Beijing"
	return func() (string, string, string) {
		return name, sex, address
	}
}

// 可变参数的函数: fmt.Println() (n int, err error)
func indefiniteArgs(a int, b ...interface{}) {
	fmt.Println("固定参数a: ", a)
	fmt.Fprintln(os.Stdout, b...)
}
