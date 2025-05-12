package main

import (
	"fmt"
	"os/exec"
)

func main() {
	cmd := exec.Command("python", "app.py")
	out, err := cmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println(string(out))
}

