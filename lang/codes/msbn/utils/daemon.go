package utils

import (
	"fmt"
	"msbn/global"
	"os"
	"os/exec"
	"syscall"
)

func StartApp() {
	if syscall.Getppid() == 1 {
		if err := os.Chdir("./"); err != nil {
			panic(err)
		}
		syscall.Umask(0)
		return
	}
	fd, err := os.OpenFile("/dev/null", os.O_WRONLY|os.O_APPEND, 0644)
	if err != nil {
		panic(err)
	}
	defer func() {
		_ = fd.Close()
	}()

	cmd := exec.Command(os.Args[0], os.Args[1:]...)
	cmd.Stdout = fd
	cmd.Stderr = fd
	cmd.Stdin = nil
	cmd.SysProcAttr = &syscall.SysProcAttr{Setsid: true}
	if err := cmd.Start(); err != nil {
		panic(err)
	}
	_, _ = fd.WriteString(fmt.Sprintf("[PID] %d start at :%s", cmd.Process.Pid, global.AppCon.GetString("app.port")))
	f, err := os.OpenFile("/tmp/app.pid", os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		panic("open pid file error!")
	}
	defer f.Close()
	fmt.Println(cmd.Process.Pid)
	if _, err := f.Write([]byte(fmt.Sprintf("%d", cmd.Process.Pid))); err != nil {
		panic("write pid to tmp file error")
	}
	os.Exit(0)
}

func StopApp() {

}
