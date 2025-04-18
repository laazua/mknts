package main

import "fmt"

// 接口规范
type Runnable interface {
	Run(speed int)
}

// 接口函数类型
type RunnableFunc func(int)

// 实现了 Runnable 接口，内部调用它自己
func (f RunnableFunc) Run(speed int) {
	f(speed)
}

type Cat struct{}

func (c Cat) Run(speed int) {
	fmt.Printf("Cat running by %dm\n", 3*speed)
}

type Dog struct{}

func (d Dog) Run(speed int) {
	fmt.Printf("Dog running by %dm\n", 4*speed)
}

// 业务逻辑要求能 Run 的具体对象来完成工作
func Move(r Runnable, speed int) {
	r.Run(speed)
}

func main() {
	// 1.简单场景可以减少代码量，面向对象和函数式变成结合了起来
	fish := func(speed int) {
		fmt.Printf("Fish running by %dm\n", 1*speed)
	}

	// 把具名函数封装成接口对象
	Move(RunnableFunc(fish), 1)

	// 把匿名函数封装成接口对象
	Move(RunnableFunc(func(speed int) {
		fmt.Printf("Bird running by %dm\n", 2*speed)
	}), 2)

	// 2. 复杂的场景，可能需要传入一个实现了接口的自定义对象
	Move(new(Cat), 3)
	Move(new(Dog), 4)

	/*
		Fish running by 1m
		Bird running by 4m
		Cat running by 9m
		Dog running by 16m
	*/
}

// 代码实现了一个 Runnable 接口和一个 Move 函数，可以让不同的对象在不同的速度下运动。其中，Runnable 接口规范了一个 Run 方法，Move 函数则接受一个实现了 Runnable 接口的对象和一个速度参数，调用该对象的 Run 方法让其运动起来。

// 这里使用了一个有趣的技巧：定义一个 RunnableFunc 类型的函数，让其实现 Runnable 接口。这样，我们就可以把一个普通的具名或匿名函数转换为 Runnable 对象，然后传给 Move 函数让其运动起来，这种方法可以减少代码量并且方便使用。

// 具体实现中，定义了 Cat 和 Dog 两个实现了 Runnable 接口的结构体，分别在 Run 方法中输出不同的文字描述。此外，还定义了两个函数 fish 和一个匿名函数，这些函数都实现了 RunnableFunc 的类型规范。最后，在 main 函数中分别使用不同的参数调用了 Move 函数，让这些对象在不同的速度下运动起来。

// 接口函数的价值在于即能将普通的函数类型作为实现接口的参数，也能将结构体作为实现了接口的参数，标准库 net/http 的对 handler 函数的定义:

// net/http使用了这种方式:
// type Handler interface {
// 	ServeHTTP(ResponseWriter, *Request)
// }
// type HandlerFunc func(ResponseWriter, *Request)

// func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request) {
// 	f(w, r)
// }
