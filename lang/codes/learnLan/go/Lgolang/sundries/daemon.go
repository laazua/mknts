//https://github.com/sevlyar/go-daemon
package main

import (
	"fmt"
	"os"
	"os/exec"
	"syscall"
	"time"
)

func main() {
	daemon()
}


func daemon() {
	cmd := exec.Command(os.Args[0])
	cmd.Stdin = nil
	cmd.Stdout = nil
	cmd.Stderr = nil
	cmd.SysProcAttr = &syscall.SysProcAttr{Setsid:true}

	err := cmd.Start()
	//if err != nil {
	//	cmd.Process.Release()
	//  os.Exit(0)
	//}
	if err != nil {
		fmt.Println(err)
		return
	}
	cmd.Process.Release()

	pid := os.Getpid()
	fmt.Println(pid)
	task()

}

func task() {
	fd, err	:= os.Create("/text.log")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer fd.Close()

	for i := 0; i < 100; i++ {
		fd.WriteString("aa\n")
		time.Sleep(time.Second * 2)
	}
}