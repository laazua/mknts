package main

import (
    "fmt"
    "os"

    "env"
    "hello"
)

func main() {

    env.Load()

    fmt.Println("Module Name: ", os.Getenv("main.name"))

    hello.HelloMain()
}
