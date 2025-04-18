package main

import (
	"container/list"
	"fmt"
)

// 数组, 切片, 字典, 列表

func main() {
	// 数组
	var areas = [...]string{"Beijing", "Shanghai", "Chengdu", "Guangzhou", "Shenzhen"}
	fmt.Println("The ereas are ", areas)

	// 切片  make也可以创建切片=> a := make([]int, 2)
	cities := areas[0:2]
	fmt.Println("The cities are ", cities)

	// 字典 map[string]int 或者 make(map[string]int)
	score := make(map[string]int)
	score["shuxue"] = 80
	score["yuwen"] = 70
	fmt.Println("score is ", score)

	// 列表(container/list)
	myList := list.New()
	myList.PushBack("apple")
	myList.PushBack("banana")
	myList.PushBack("oringe")
	myList.PushFront("walter")
	for i := myList.Front(); i != nil; i = i.Next() {
		fmt.Println(i.Value)
	}
}
