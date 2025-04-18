// interface: 一组方法的聚合
// golang中有两种接口, runtime.iface: 用于结构体的方法; runtime.eface: interface{}空接口
package main

import "fmt"

type Student struct {
	Name string
	Age  int
}

func (s *Student) SetName(name string) {
	s.Name = name
}

func (s *Student) SetAge(age int) {
	s.Age = age
}

func (s Student) SayHi() {
	fmt.Println("my name: ", s.Name, "my age: ", s.Age)
}

type Seter interface {
	SetName(name string)
	SetAge(age int)
}

func main() {
	s := Student{}
	s.SetName("xiaogang")
	s.SetAge(18)
	s.SayHi()

	// Seter接口只实现了SetName()和SetAge()方法
	var S Seter = &Student{}
	S.SetName("我是用接口实现的")
	S.SetAge(15)
	// S.SayHi()   Seter接口只实现了SetName(), SetAge()方法, 所以SayHi()方法这里不能调用
	fmt.Println("S = ", S)
}
