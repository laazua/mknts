// map是无序的key-value数据结构
package main

import (
	"fmt"
)

func main() {
	var m1 map[string]string
	m1 = make(map[string]string)
	// var m1 map[string]string = make(map[string]string)
	// var m1 map[string]string = map[string]string{}
	m1["xiaohong"] = "beijing"
	m1["xiaoli"] = "shanghai"
	fmt.Println("m1 = ", m1)

	m2 := make(map[int]string)
	m2[1] = "a"
	m2[2] = "b"
	fmt.Println("m2 = ", m2)
}
