package main

import (
	"fmt"
	"math"
)

//定义一个几何形状的接口
type geometry interface {
	area() float64
	perim() float64
}


//在rect和circle类型上实现geometry接口
type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}


//rect类型绑定area()方法和perim()方法
func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return  2*r.width + 2*r.height
}


//circle类型上绑定area()方法和perim()方法
func (c circle) area() float64 {
	return  math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return  2 * math.Pi * c.radius
}


//interface test
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	//定义并初始化rect类型和circle类型对象
	r := rect{width:3,height:4}
	//c := circle{radius:5}

	measure(r)
	//measure(c)
}
