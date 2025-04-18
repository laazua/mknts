package main

import "fmt"

// 结构体: 类型集合

func main() {
	// p := new(Person)
	p1 := newPerson("ZhangSan", 18, "男")
	fmt.Println("p1 = ", p1)

	p2 := &Person{Name: "LiSi", age: 20, sex: "男"}
	fmt.Println("p2 = ", p2)
}

type Person struct {
	Name string
	age  uint
	sex  string
}

// 构造函数, 构造基类(struct)
func newPerson(name string, age uint, sex string) *Person {
	return &Person{
		Name: name,
		age:  age,
		sex:  sex,
	}
}

type Student struct {
	Person // 匿名结构体
	score  uint8
}

// 构造函数, 构造子类(struct)
func newStuent(p *Person, score uint) *Student {
	s := &Student{}
	s.Name = "xiaolan"
	s.age = 15
	s.sex = "女"
	s.score = 85
	return s
}
