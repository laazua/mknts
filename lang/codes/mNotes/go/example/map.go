package main

import "fmt"

func main() {
	map_one := map[string]int{"a": 1, "b": 2}
	map_tow := make(map[string]int, 2)

	fmt.Println(map_one, len(map_one))
	fmt.Println(map_tow, len(map_tow))

	for k, v := range map_one {
		fmt.Println("key: ", k, "value: ", v)
	}
}
