package typeSystem

import "fmt"

func main() {
	/*
	基本类型系统:
	基础类型: byte, int, string, float, bool
	符合类型: array, slice, map, struct, pointer
	可以指向任意对象的类型: interface{}(空接口Any类型)
	值语义和引用语义
	面向对象
	接口

	4种引用类型: slice, map, channel, interface
	*/
}

func testSomething() {
	//数组很纯粹的值类型
	var array1 = [3]int{1,2,3}
	var array2 = array1    //完整的内容复制
	array2[1]++
	fmt.Println(array1, array2)

	//引用表达方式
	var array3 = &array1
	array3[1]++
	fmt.Println(array1, array3)
}


//结构体(自定义类型)
type Rect struct {
	a, b float64
	width, height float64
}

//给结构体绑定方法
func (r *Rect) Area() float64 {
	return r.width * r.height
}

func testStruct() {
	//创建和初始化Rect类型,未被显示初始化的变量都会初始化为该类型的零值
	a := new(Rect)
	b := &Rect{}
	c := &Rect{1,2,10,20}
	d := &Rect{width: 100, height: 200}
}

//对象的创建由一个全局函数来完成,以NewXXX来命名(类似构造函数的功能)
func NewRect(x, y, width, height float64) *Rect {
	return &Rect{x, y, width, height}
}
