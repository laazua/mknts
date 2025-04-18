//*获取指针的值,即指针的解引用;&可以获取变量的地址,即取地址操作符.
package main


//修改传来的参数,将变量值的改变反映到原值上
func getPointer(n *int) {
	//这里改变了n变量的原始值
	*n = *n * *n
}


//返回指向整数的指针,一般用这种方式操作结构体等复杂数据结构
func returnPointer(n int) * int {
	v := n * n
	return &v
}