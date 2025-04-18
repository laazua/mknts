package main

import (
	"fmt"
	"log"
	"os"
	"time"
)

/*
#include <unistd.h>
*/
import "C"

func init() {
    C.daemon(1, 1)
}

func main() {
	fmt.Println("aa")
	go func() {
		fd, _ := os.OpenFile("./test.log", os.O_WRONLY|os.O_CREATE|os.O_APPEND, 0644)
		log.SetOutput(fd)
		for {
			log.Println(fmt.Sprint("hello ", os.Getpid()))
			time.Sleep(time.Second * 5)
		}
	}()
	for {
		time.Sleep(time.Second * 1000)
	}
}
