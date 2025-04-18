package main

/*
#include <unistd.h>
*/
import "C"
import (
	"fmt"
	"os"
	"runtime"
	"time"
)

func main() {
	C.daemon(1,1)
	runtime.GOMAXPROCS(runtime.NumCPU())
	fmt.Println("starting ...")
	task()
}

func task() {
	fd, err	:= os.Create("/home/wnot/test.log")  //绝对路径
	if err != nil {
		fmt.Println(err)
		return
	}
	defer fd.Close()

	for i := 0; i < 100; i++ {
		fmt.Println("aa")
		fd.WriteString("aa\n")
		time.Sleep(time.Second * 2)
	}
}
