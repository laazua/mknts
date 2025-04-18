package main

import (
	"fmt"
	"image"
	"image/jpeg"
	"image/png"
	"io"
)

func main() {
	//数组的定义方式
	var a [3]int    //定义长度为3的int类型数组,元素全部为0
	var b = [...]int{1, 2, 3}     //定义长度为3的int类型数组,元素为1,2,3
	var c = [...]int{2: 3, 1: 2}    //定义长度为3的int类型数组,元素为0,2,3
	var d = [...]int{1, 2, 4: 5, 6}    //定义长度为6的int类型数组,元素为1,2,0,0,5,6
	fmt.Println(a, b, c, d)

	testArray()
}

func testArray() {
	//Go语言中数组是值语义,即一个数组变量表示整个数组,它并不是隐式指向数组第一个元素.
	//当一个数组变量被赋值或者被传递的时候,实际上是复制的整个数组,如果数组较大,那么复制的过程也会有较大开销,
	//为了避免复制数组带来的开销,可以传递一个指向数组的指针,数组指针并不是数组.
	var a = [...]int{1, 2, 3}
	var b = &a     //b是指向数组a的一个指针
	fmt.Println(a[0], a[1])
	fmt.Println(b[0], b[1])

	for i, v := range b {    //通过数组指针迭代数组元素
		fmt.Println(i, v)
	}

	for i := 0; i < len(a); i++ {    //通过循环迭代数组
		fmt.Printf("a[%d]: %d\n", i, a[i])
	}
	for i := range a {    //通过range循环迭代数组(推荐)
		fmt.Printf("a[%d]: %d\n", i, a[i])
	}

	var times [5][0]int
	for range  times {    //无下标迭代数组
		fmt.Println("hello")
	}

	//字符串数组
	var s1 = [2]string{"hello", "world"}
	var s2 = [...]string{"你好", "世界"}
	var s3 = [...]string{1:"hello", 2:"world"}

	//结构体数组
	var line1 [2]image.Point
	var line2 = [...]image.Point{image.Point{X: 0, Y: 0}, image.Point{X: 1, Y: 1}}
	var line3 = [...]image.Point{{0, 0}, {1, 1}}

	//图像解码数组(函数)
	var decoder1 [2]func(io.Reader) (image.Image, error)
	var decoder2 = [...]func(io.Reader) (image.Image, error) {
		png.Decode,
		jpeg.Decode,
	}

	//接口数组
	var unknown1 [2]interface{}
	var unknown2 = [...]interface{}{123, "hello"}

	//长度为0的数组在内存中并不占用空间,可以用于强调某种特有类型的操作避免分配和外的内存空间,如管道同步操作
	//并不关心管道中传输数据的真实类型,管道接受和发送操作只是用于消息同步,对于这种场景,用空数组来作为管道类型可以减少管道元素赋值时的开销
	c := make(chan [0]int)
	go func() {
		fmt.Println("c")
		c <- [0]int{}
	}()
	<- c
	//或者倾向于以下的方式
	c1 := make(chan interface{})
	go func() {
		fmt.Println("c1")
		c1 <- struct{}{}    //struct{}是类型, {}表示对应的结构体值
	}()
	<- c1

	//fmt.Printf()函数提供的%T和%#v打印数组详细信息
	fmt.Printf("s1: %T\n", s1)    //s1: [2]string
	fmt.Printf("s1: %#v\n", s1)   //s1: [2]string{"hello", "world}"

	//Go中数组类型是切片和字符串等结构的基础.很多数组操作都可以用于字符串和切片
}
