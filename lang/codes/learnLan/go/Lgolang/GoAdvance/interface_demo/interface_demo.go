// 多态, 接口就是一组方法的组合
package interface_demo

import "fmt"

type Student struct {
	age  int
	name string
}

func (s *Student) getName() {
	fmt.Println(s.name)
}

func (s *Student) getAge() {
	fmt.Println(s.age)
}

//接口就是一组方法的签名
type Person interface {
	getName()
	getAge()
}

func main() {
	// go中，不需要显示的声明实现了某个接口,只需要实现接口对应的方法即可.
	// 实例化Student后,会将实例化的对象强制转换成对应的接口类型(实例化的对象p必须全部实现了接口中的所有方法,这种转换才不会报错)
	var p Person = &Student{12, "alen"}
	p.getAge()
	p.getName()
}
