package utils

import (
	"os"
	"os/exec"
	"syscall"
)

func Daemon(logpath string) *exec.Cmd {
	if syscall.Getppid() == 1 {
		if err := os.Chdir("./"); err != nil {
			panic(err)
		}
		syscall.Umask(0)
		return nil
	}
	fd, err := os.OpenFile(logpath, os.O_WRONLY|os.O_APPEND, 0644)
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
	// if fd, err := os.OpenFile("./app.pid", os.O_CREATE|os.O_WRONLY, 0644); err != nil {
	// 	panic(err)
	// } else {
	// 	if _, err = fd.WriteString(fmt.Sprintf("%v", cmd.Process.Pid)); err != nil {
	// 		panic(err)
	// 	}
	// 	defer fd.Close()
	// }
	os.Exit(0)
	return cmd
}
