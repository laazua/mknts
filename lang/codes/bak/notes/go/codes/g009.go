package main

import "fmt"

// 常量

const (
	MAX = 100
	MIN = 1
)

const (
	ONE = iota
	TOW
	THREE
	FOUR
	FIVE
	SIX
	SEVE
	_
	_
	TEN
)

func main() {
	fmt.Println("MAX = ", MAX)
	fmt.Println("MIN = ", MIN)
	fmt.Println("ONE = ", ONE)
	fmt.Println("TOW = ", TOW)
	fmt.Println("FOUR = ", FOUR)
	fmt.Println("FIVE = ", FIVE)
	fmt.Println("SIX = ", SIX)
	fmt.Println("SEVE = ", SEVE)
	fmt.Println("TEN = ", TEN)
}
