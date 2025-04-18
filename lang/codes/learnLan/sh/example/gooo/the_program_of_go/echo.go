//该程序模仿的的是linux下的echo命令
package main

import (
	"fmt"
	"os"
)

//os.Args获取命令行传入的参数，os.Args[0]表示的是程序本身
func main() {
	var s, sep string //sep变量保存各个参数之间的空格
	for i := 1; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = " "
	}
	fmt.Println(s)
}
