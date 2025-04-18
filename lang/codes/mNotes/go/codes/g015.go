// 泛型
package main

import "fmt"


func main() {
    s1 := Sum(2, 3)
    s2 := Sum(3.3, 6.1)

    fmt.Println("s1 = ", s1)
    fmt.Println("s2 = ", s2)
}

type Number interface {
   int | float64
}

func Sum[T Number](v1 T, v2 T) T {
    return v1 + v2
}

