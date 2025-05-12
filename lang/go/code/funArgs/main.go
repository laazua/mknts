package main

import "fmt"

type Person struct {
	Name    string
	Address string
	ZipCode string
}

type Option func(*Person)

func Address(s string) Option {
	return func(p *Person) {
		p.Address = s
	}
}

func ZipCode(s string) Option {
	return func(p *Person) {
		p.ZipCode = s
	}
}

// 假设 name 对业务上是必须的，Address 和 ZipCode 是可选的
func NewPerson(name string, opts ...Option) *Person {
	p := &Person{Name: name}

	for _, opt := range opts {
		opt(p)
	}

	return p
}

func main() {
	p1 := NewPerson("zhangsan", Address("street 99"), ZipCode("620000"))
	fmt.Println(p1) // &{zhangsan street 99 620000}

	p2 := NewPerson("lisi")
	fmt.Println(p2) // &{lisi  }
}

// 通常是 builder 模式的函数式风格重构，通常对参数会重定义一个 Option 函数式类型。
/*
程序通过定义 Option 类型的函数，使用可变参数列表传入，将需要修改的参数值以函数的形式传入，从而实现在构造函数中传入可选参数的效果。

具体实现中，我们定义了一个 NewPerson 构造函数，该函数首先会为必须的参数赋值，然后通过循环调用可选参数的函数，将可选参数的值应用到对象中。这样在构造函数中调用时，可以传入必须的参数，也可以传入多个可选参数，也可以不传任何可选参数，从而实现了可选参数的效果。

在实现中，我们使用了 Go 语言中的闭包，将需要修改的参数值以函数的形式保存下来。通过遍历可选参数列表，逐个将参数函数应用到对象上，从而实现了可选参数的功能。

需要注意的是，对于一些不可选的参数，我们需要在构造函数中指定其值。同时，为了避免可选参数在使用时位置混乱，我们通常将可选参数放在参数列表的最后面。
*/
