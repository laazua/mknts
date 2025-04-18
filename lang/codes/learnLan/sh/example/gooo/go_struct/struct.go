package main

import(
	"fmt"
	"strconv"
)

type B struct {
	name    string
	id      int
}

type A struct{
	B         //匿名字段,A会继承B中的所有属性(如果B绑定了C方法,那么A的一个实例也拥有C方法).
	a  int
	b  int
}

//实例化结构体对象时,对属性字段操作是操作的副本
func (r A) sum() int {
	r.a = 3
	r.b = 5
	return r.a + r.b
}

//实例化结构体对象,对属性字段操作的是引用
func (r *A) add() int{
	r.a = 4
	r.b = 6
	return r.a + r.b
}


func main() {
	var a int64 = 1
	fmt.Println(strconv.FormatInt(a, 10))

	c := A{B{"BOBO",18},1,2}

	fmt.Println(c.name, c.id)
	d := c.sum()
	//f := c.add()
	fmt.Println(c.a, c.b)
	fmt.Println(d)
	//fmt.Println(f)
}
