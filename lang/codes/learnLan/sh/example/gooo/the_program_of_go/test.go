package main

import(
	"fmt"
)

func main() {
    fmt.Println(hypot(3, 4))
}

func hypot(x, y float64) float64 {
	return math.Sqrt(x*x + y*y)
}