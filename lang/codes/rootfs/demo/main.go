package main

import (
    "fmt"
    "time"
)

func main() {
    for {
        time.Sleep(time.Second * 2)
	fmt.Println("this is a test ...")
    }
}
