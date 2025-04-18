package main

import "fmt"

func main() {
	/* var 关键字用于声明变量 */

	// 无符号整型
	var age uint = 18
	fmt.Println("Your age is ", age)

	// 有符号整型
	var temperature int = -1
	fmt.Println("Today temperature is ", temperature, " C")

	// rune
	var distance rune = 25
	fmt.Println("The distance is ", distance)

	// byte
	var width byte = 8
	fmt.Println("The width is ", width)

	// 浮点型
	var high float32 = 172.5
	fmt.Println("Your high is ", high)

	// string
	var name string = "Wang er ma zi"
	fmt.Println("Your name is ", name)

	// bool
	var answer bool
	fmt.Println("Golang is fun? ", answer)
}
