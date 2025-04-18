package main

import "fmt"

func main() {
	var isDone bool = true
	var byteNum byte = 8
	var runeNum rune = 32
	var intNum int = 32
	var uintNum uint = 64
	var int8Num int8 = 8
	var uint8Num uint8 = 8
	var int16Num int16 = 16
	var uint16Num uint16 = 16
	var int32Num int32 = 32
	var uint32Num uint32 = 32
	var int64Num int64 = 64
	var uint64Num uint64 = 64
	var f32Num float32 = 32.0
	var f64Num float64 = 64.0
	var c64Num complex64 = 0
	var c128Num complex128 = 0
	var up uintptr = 0

	fmt.Println("布尔类型: ", isDone)
	fmt.Println("byte类型: ", byteNum)
	fmt.Println("rune类型: ", runeNum)
	fmt.Println("int类型: ", intNum)
	fmt.Println("uint类型: ", uintNum)
	fmt.Println("int8类型: ", int8Num)
	fmt.Println("uint8类型: ", uint8Num)
	fmt.Println("int16类型: ", int16Num)
	fmt.Println("uint16类型: ", uint16Num)
	fmt.Println("int32类型: ", int32Num)
	fmt.Println("uint32类型: ", uint32Num)
	fmt.Println("int64类型: ", int64Num)
	fmt.Println("uint64类型: ", uint64Num)
	fmt.Println("float32类型: ", f32Num)
	fmt.Println("float64类型: ", f64Num)
	fmt.Println("complex64类型: ", c64Num)
	fmt.Println("complex128类型: ", c128Num)
	fmt.Println("uintptr类型: ", up)
}
