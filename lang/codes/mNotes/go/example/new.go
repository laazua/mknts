package main

import "fmt"

func main() {
	num := 200
	pt := new(int)
	*pt = 100
	fmt.Println(*pt)
	pt = &num
	fmt.Println(*pt)
}
