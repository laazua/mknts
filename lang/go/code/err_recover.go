package code

import (
	"fmt"
)

func Test() {
	// 阻止程序因异常退出
	defer func() {
		if err := recover(); err != nil {
			fmt.Println("recover panic.")
		}
	}()

	panic("Throw Error!")
}
