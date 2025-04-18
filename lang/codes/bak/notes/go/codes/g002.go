package main

import "fmt"

/* 声明多个包级别的变量 
// 首字母是大写视为包外可见
*/
var (
	name       = "zhangsan"
	address    = "shanghai"
        score uint = 66 // 不推荐
)

func main() {
	// 声明一个局部age变量,并赋值18
	age := 18

	fmt.Println("Your age is ", age)
	fmt.Println("Your name is ", name)
	fmt.Println("Your address is on", address)
}
