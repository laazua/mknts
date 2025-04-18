// 数组: 固定长度,特定类型的一组数据组成的序列
package main

import "fmt"

func main() {
	// 一维数组
	var arr_1 = [5]int{1, 2, 3, 4, 5}
	fmt.Println(arr_1)

	var arr_2 = [...]string{"a", "b", "c"}
	fmt.Println(arr_2)

	arr_3 := [5]int{0: 1, 2: 5}
	fmt.Println(arr_3)

	// 二维数组
	arr_4 := [2][3]int{{1, 2, 3}, {4, 5, 6}}
	fmt.Println(arr_4)
}
