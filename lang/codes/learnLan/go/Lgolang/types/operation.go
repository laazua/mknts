package types

import (
	"fmt"
	"math"
)

func main() {
	/*
	数值运算: +  -  *  /  %  ++  --
	比较运算: >  <  >=  <=   ==  !=
	位运算: <<  >>  x^y(异或)  &  |  ^x(取反)
	逻辑运算: &&  ||  !
	赋值运算: =  +=  -=  *=  /=  %=  <<=  >>=  &=  ^=  |=
	指针地址操作: *  &
	*/
}

//浮点类型比较,p自定义精度r如0.001
func compareFloat(x, y, p float64) bool {
	return math.Dim(x, y) < p
}

//字符串操作,更多操作参照strings包
func stringOperation(x, y string) string {
	w := x + y
	for i, v := range w {
		fmt.Println(i, v)
	}

	return w[len(x + y)/2:]
}

func array(a [5]int) {
	//元素访问, range关键字
	for i := 0; i < len(a); i++ {
		fmt.Println("index:", i, "element:", a[i])
	}
	//go中数组是值类型,在赋值和传参都会产生一次复制动作
}

func sliceOperation(s []int) (l, c int) {
	//slice: cap, len, pointer
	for _, v := range s {
		fmt.Println(v)
	}

	return len(s), cap(s)
	//make([]int, 5, 10), len(), cap(), append(s, ...), copy()
}

func mapOperation(m map[int]string) {
	//m := make(map[int]string, 10), delete()
	v, ok := m[1]
	if ok {
		fmt.Println(v)
	}
}
