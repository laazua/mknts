//go字符串实际上是一个字节切片,可以存储任意类型,任意长度的字节
package main

import (
	"fmt"
	"strings"
)

var str strings.Builder

func main() {
	//字符串是一个不可改变的字节序列(一个只读的字节数组)
	//支持切片操作
	fmt.Printf("%#v\n", []byte("hello, 世界")) //打印字符串转型[]byte类型后的信息

	fmt.Printf("%#v\n", []rune("世界"))
	fmt.Printf("%#v\n", string([]rune{'世', '界'}))

	// 字符串是只读的,每次修改字符串都会创建一个新的字符串.所以高效得拼接字符串,使用strings.Builder，最小化内存拷贝
	for i := 1; i < 20; i++ {
		str.WriteString("a")
	}
	fmt.Println(str.String())
}

//rune是什么?
//rune是一个类型为int32的值,主要用来代表一个Unicode码点，Unicode码点代表Unicode字符的数值
//rune字面量实际上是一个用单引号括起来的字符,并且与Unicode码点的概念相关联

//字节切片[]byte就是一系列rune的集合

//unicode包提供很多函数来判断字符串的某一部分是否能够以rune的类型打印出来
//strings包里面提供了很多操作UTF-8字符串的强大工具
