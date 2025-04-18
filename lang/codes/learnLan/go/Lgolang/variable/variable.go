//变量是数据在内存中存储时的别名
package variable

import "fmt"

func main() {
    /*通过var关键字声明变量
	var a int = 1
	var b string = "hello world"
	var c [5]int = [5]int{1, 2, 3, 4, 5}
	var d []int = []int{9, 10, 11}
	var e struct {
		name  string
	}
	var f *int = nil
	var g map[int]string
	var h func(a, b int) int
     */
    // 交换两个变量
    var (
    	x = 1
    	y = 2
	)
    x, y = y, x
    fmt.Println("x = ", x, "y = ", y)

    //通过 _ 丢弃不需要的变量值
}


