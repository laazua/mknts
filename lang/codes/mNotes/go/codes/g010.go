package main

import "fmt"

// 接口 && 方法

func main() {
	t := NewTeacher("xxx", 26, "Beijing")
	fmt.Println("t = ", t)

	// 任何实现了接口中方法的类型都可以给该接口类型赋值
	var a Actor = Teacher{"xxx", 18, "chengdu"}
	a.ShowAddress()

}

// 结构体绑定方法
type Teacher struct {
	Name    string
	Age     uint8
	Address string
}

func NewTeacher(name string, age uint8, address string) *Teacher {
	return &Teacher{
		Name:    name,
		Age:     age,
		Address: address,
	}
}

func (t Teacher) ShowName() {
	fmt.Println(t.Name)
}

func (t Teacher) ShowAge() {
	fmt.Println(t.Age)
}

func (t Teacher) ShowAddress() {
	fmt.Println(t.Address)
}

// 接口签名:
// Teacher结构体实现了Actor接口上的所有方法
// 则Teacher结构体实现了Actor接口
type Actor interface {
	ShowName()
	ShowAge()
	ShowAddress()
}
