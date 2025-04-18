// 格式化输出
package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func test(i, j int) int {
	return i + j
}

func main() {
	p := point{1, 2}

	fmt.Printf("%d\n", p) // {1, 2}

	fmt.Printf("%+v\n", p) // {x:1, y:2}

	fmt.Printf("%#v\n", p) // main.point{x:1, y:2}

	//输出类型
	fmt.Printf("%T\n", p) // main.point

	//输出函数签名
	fmt.Printf("%T\n", test) // func(int, int) int

	//输出bool值
	b := true
	fmt.Printf("%t\n", b) // true

	// 尝试将一个字符串作为参数来输出bool值,不要尝试这样做
	fmt.Printf("%t\n", "true") // %!t(string=true)

	//十进制形式输出
	fmt.Printf("%d\n", 100) // 100

	//输出一个字符对应的ASCII码
	fmt.Printf("%c\n", 12)

	//输出整数的二进制值
	fmt.Printf("%b\n", 12)

	//输出一个字符的二进制值
	fmt.Printf("%b\n", 'a')

	//如果参数是数字,则以16进制形式输出
	fmt.Printf("%x\n", 100)

	//如果参数是字符串,则打印字符串的每一个字符的ASCII码
	fmt.Printf("%x\n", "hello world")

	//浮点数形式输出,默认小数6位
	fmt.Printf("%f\n", 12.00)

	//占位符与参数不对应，不会报错，自动类型转换
	fmt.Printf("%d\n", 12.00) // %!d(float=12.00)

	//科学计数法的形式输出
	fmt.Printf("%e\n", 12.00)
	fmt.Printf("%E\n", 12.00)

	//输出字符串
	fmt.Printf("%s\n", "\"abc")

	//保留字符串引号输出
	fmt.Printf("%q\n", "abc")

	//输出指针(地址)的值
	fmt.Printf("%p\n", &p)

	//最小宽度为6,默认右对齐,不足6位时,空格补全,超过6位时,不会截断
	fmt.Printf("|%6d|%6d|\n", 12, 15)

	//最小6个宽度(包含小数点),2位小数,超过6位时,不会截断
	fmt.Printf("|%6.2f|%6.2f|\n", 12.00, 115.00)

	//使用 - 表示左对齐
	fmt.Printf("|%-6.2f|%-6.2f|\n", 12.00, 115.00)

	//最小6个宽度,右对齐,不足6个时,空格补齐,超过6个时,不会截断
	fmt.Printf("|%6s|%6s|\n", "foo", "foobarfoo")

	//不会输出内容,相反,会将内容以字符串的形式返回
	s := fmt.Sprintf("a%s", "bc")
	fmt.Println(s) //abc

	//使用Fprintf来格式化输出到io.Writer对象
	fmt.Fprintf(os.Stderr, "an %s\n", "error")
}
