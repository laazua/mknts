package main

import "fmt"

func main() {
	slice_one := make([]int, 10, 10)
	fmt.Println(slice_one, len(slice_one), cap(slice_one))

	arra := [...]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	slice_tow := arra[:]
	fmt.Println(slice_tow, len(slice_tow), cap(slice_tow))

	for i, v := range slice_tow {
		fmt.Println("index: ", i, "value: ", v)
	}
}
