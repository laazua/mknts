//结构体指针
package main

import "fmt"

type myStructure struct {
	Name string
	Surname string
	Height int32
}

func NewStructurePointer(n, s string, h int32) * myStructure {
	if h > 300 {
		h = 0
	}
	return &myStructure{n, s, h}
}

func NewStructure(n, s string, h int32) myStructure {
	if h > 300 {
		h = 0
	}
	return myStructure{n, s, h}
}

func main() {
	s1 := NewStructurePointer("Mihalis", "Tsoukalos", 456)
	s2 := NewStructure("Mihalis", "Tsoukalos", 798)
	fmt.Println((*s1).Name)
	fmt.Println(s2.Name)
	fmt.Println(s1)
	fmt.Println(s2)

	//使用new()创建新的对象,返回的是对象的指针
	ps := new(myStructure)
	fmt.Println(ps)

	//new()与make()的区别:new()返回内存地址;make()仅仅可以用来创建映射,切片和通道,并且返回的不是指针
}