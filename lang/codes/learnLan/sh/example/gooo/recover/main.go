package main

import(
	"fmt"
)

func test() {
	//defer + recover捕获异常,使整个程序不会漰溃
	defer func() {
		//捕获test函数抛出的异常
		if err := recover(); err != nil {
			fmt.Println("test()发生错误", err)
		}
	}()
	var myMap map[int]string
	myMap[0] = "golang"     //error
}

func main() {
	test()
	for i := 0; i < 10; i++ {
		fmt.Println("I am ", i)
	}
}
