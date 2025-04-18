// 将零个或多个任意类型聚合在一起
package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func main() {
	var p1 Person
	p1.Name = "xiaoming"
	p1.Age = 12
	fmt.Println("p1 = ", p1)
	p1.SayName()

	var p2 = Person{"xiaogang", 15}
	fmt.Println("p2 = ", p2)

	p3 := struct {
		Name string
		Age  int
	}{"匿名结构体", 20}
	fmt.Println("p3 = ", p3)

	// 结构体方法
	p4 := Person{}
	p4.SetName("xiaoliang")
	p4.SetAge(15)
	fmt.Println("p4 = ", p4)
}

// 方法: 绑定到结构体上的特殊函数
func (p *Person) SetName(name string) {
	// 结构体指针实现
	p.Name = name
}

func (p *Person) SetAge(age int) {
	// 结构体指针实现
	p.Age = age
}

func (p Person) SayName() {
	// 结构体实现
	fmt.Println(p.Name)
}
