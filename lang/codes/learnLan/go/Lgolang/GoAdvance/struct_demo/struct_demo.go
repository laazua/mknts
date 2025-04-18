//结构体定义&面向对象特性
package structt

import "fmt"

type Animal struct {
	Color string
}

type Dog struct {
	Animal // 继承了结构体Animal的属性和方法
	ID     int
	Name   string
	Age    int
}

// 结构体声明并初始化
func testDog() {
	// var 声明初始化
	var d Dog
	d.ID = 1
	d.Name = "wawa"
	d.Age = 5

	// new 创建并初始化
	o := new(Dog)
	o.ID = 2
	o.Name = "maomao"
	o.Age = 7

	// 匿名方式
	g := Dog{ID: 3, Name: "duoduo", Age: 6}

	fmt.Println(d, o, g)
}

func (a *Animal) Eat() {
	fmt.Println("i am animal")
}

func (d *Dog) Wang() {
	fmt.Println("wang wang wang...")
}
