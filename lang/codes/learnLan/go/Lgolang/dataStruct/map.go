//go maps(映射)
package main

import "fmt"

func main() {
	//map创建
	m := make(map[string]int)
	n := map[string]int{
		"aa": 1,
		"bb": 2,
	}
	fmt.Println(m, n)
	delete(n, "aa")
	fmt.Println(n, n["bb"])

	_, ok := n["bb"]
	if ok {
		fmt.Println("bb Exist")
	} else {
		fmt.Println("bb Not Exist")
	}

	// 判断map中是否包含某个Key
	if val, ok := m["bar"]; ok {
		fmt.Println("map m 中包含key值为bar的键,其对应的值为:", val)
	}
}
