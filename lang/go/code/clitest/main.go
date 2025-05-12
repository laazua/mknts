package main

import (
	"clitest/cmd"
	"fmt"
)

func main() {
	cmd.Execute()
	fmt.Println(cmd.Aa, cmd.Bb)
}
