// 切片: 动态数组,长度不固定
package main

import "fmt"

func main() {
	// sil := make([]int, 0, 4)

	var sli_1 []int
	fmt.Printf("len=%d, cap=%d, slice=%v\n", len(sli_1), cap(sli_1), sli_1)

	sli_2 := []int{1, 2, 3, 4, 5, 6}
	fmt.Printf("len=%d, cap=%d, slice=%v\n", len(sli_2), cap(sli_2), sli_2)

	// sli_2[:4]; sli_2[1:]
	sli_3 := sli_2[2:4]
	fmt.Printf("len=%d, cap=%d, slice=%v\n", len(sli_3), cap(sli_3), sli_3)

	// 追加元素
	sli_1 = append(sli_1, 100)
	fmt.Printf("len=%d, cap=%d, slice=%v\n", len(sli_1), cap(sli_1), sli_1)

	// 删除元素
	sli_4 := sli_2[:len(sli_2)-2]
	fmt.Printf("len=%d, cap=%d, slice=%v\n", len(sli_4), cap(sli_4), sli_4)
}
