package main

import "fmt"

type Person struct {
	Name    string
	Address string
	ZipCode string
}

type PersonBuilder struct {
	p *Person
}

func NewPersonBuilder() *PersonBuilder {
	return &PersonBuilder{p: &Person{}}
}

// 三个 build 过程，使用简单的赋值简化了实际业务
func (pb *PersonBuilder) Name(s string) *PersonBuilder {
	pb.p.Name = s

	return pb
}

func (pb *PersonBuilder) Address(s string) *PersonBuilder {
	pb.p.Address = s

	return pb
}

func (pb *PersonBuilder) ZipCode(s string) *PersonBuilder {
	pb.p.ZipCode = s

	return pb
}

func (pb *PersonBuilder) Build() *Person {
	return pb.p
}

func main() {
	pb := NewPersonBuilder()
	p := pb.Name("zhangsan").Address("stree 99").ZipCode("620000").Build()
	fmt.Println(p) // &{zhangsan stree 99 620000}
}

// 对象的链式调用是指在对象的成员方法中返回当前对象指针，完全是基于写法上的便利，在 builder 模式中最为典型。

// 建造者模式将一个复杂对象的构造过程分解成多个简单对象的构造过程，从而使得构造过程更加灵活，同时也能够避免由于参数过多或参数顺序不当而导致的调用混乱的问题。

// 在这个示例中，PersonBuilder 封装了 Person 对象的构建过程，它包括了三个 build 方法，分别对应 Name、Address 和 ZipCode 三个属性。每次调用 build 方法之后，就会返回一个指向 Person 对象的指针。这样，我们就可以在构建过程中使用链式调用的方式来设置 Person 对象的各个属性，最后调用 build 方法获取最终的对象。

// 在 PersonBuilder 中，每个 build 方法都返回一个指向 PersonBuilder 对象的指针，这就允许我们在构建过程中链式调用多个方法，如 pb.Name("zhangsan").Address("stree 99").ZipCode("620000").Build()，这样可以让代码更加简洁、易读，同时也减少了出错的概率。

// 最终，在 main 函数中我们可以通过 NewPersonBuilder 方法获取一个新的 PersonBuilder 对象，并使用 pb.Name("zhangsan").Address("stree 99").ZipCode("620000").Build() 的链式调用方式来构建 Person 对象。最后我们打印出了构建出来的 Person 对象，可以看到它的三个属性都被正确地设置了。
