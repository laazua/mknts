package hello

import (
    "fmt"
    "os"
    "strings"
)

func HelloMain() {
	fmt.Println("Module Name: ", os.Getenv("hello.name"))
	fruits := strings.Split(os.Getenv("hello.fruit"), ",")
	fmt.Println("Hello Fruit: ", fruits)
}
