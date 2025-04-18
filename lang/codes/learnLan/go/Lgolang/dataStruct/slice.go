package main

import "fmt"

func main() {
	//type SliceHeader struct {
	//     Data    uintptr
	//     Len     int
	//     Cap     int
	// }

	//切片定义
	var a []int   //nil切片,和nil相等,一般用来表示一个不存在的切片
	var b = []int{}    //空切片,和nil不等,一般用来表示一个空集合
	var c = []int{1, 2, 3}    //有3个元素的切片,len和cap都是3
	d := c[:2]
	e := c[0:2:cap(c)]    //有两个元素的切片,len为2,cap为3
	f := c[:0]    //有0个元素的切片,len为0,cap为3
	g := make([]int, 3)    //有3个元素的切片,len和cap都为3
	h := make([]int, 2, 3)    //有两个元素的切片,len为2, cap为3
	i := make([]int, 0, 3)    //有0个元素的切片,len为0,cap为3

	//切片遍历跟数组类似
    var j int = 2
	//append()在切片末尾追加元素,切片容量不足会重新分配内存
	var aa []int
	aa = append(aa, 1,2,3)    //追加多个元素,手写解包
	aa = append(aa, []int{1,2,3}...)     //追加一个切片,追加的切片通过...解包
	//开头追加会重新分配内存,性能差
	aa = append([]int{0}, aa...)    //在开头添加1个元素
	aa = append([]int{-1,-2,-3}, aa...)    //在开头追加一个切片(...解包)
	//切片中间插入元素
	aa = append(aa[:j], append([]int{x}, aa[j:]...)...)    //在i位置插入x
	aa = append(aa[:j], append([]int{1,2,3}, aa[j:]...)...)    //在i位置插入切片

	//copy()和append()组合避免创建中间临时切片,完成元素的操作
	aa = append(aa, 0)    //切片扩展1个空间
	copy(aa[j+1:], aa[j:])    //a[i:]向后移动一个位置
	aa[j] = x    //设置新添加的元素x

	aa = append(aa, x...)
	copy(aa[j+len(x):], aa[j:])
	copy(a[j:], x)       //x为新添加的切片


	aa = aa[:len(aa) - 1]    //删除尾部一个元素
	aa = aa[1:]    //删除开头一个元素
	aa = append(aa[:0], aa[1:]...)    //删除开头一个元素(在原有切片对应的内存区间完成)
	aa = append(aa[:0], aa[N:]...)    //删除开头N个元素(在原有切片对应的内存区间完成)

	b = []int{1 ,2, 3, 4, 5, 6}
	b = append(b[:j], b[j+1:]...)    //删除中间一个元素
	b = append(b[:j], b[j+N:]...)    //删除中间N个元素
	b = b[:j+copy(b[j:], b[j+1:])]   //删除中间一个元素
	b = b[:j+copy(b[j:], b[j+N:])]   //删中间N个元素

	//len为0cap不为0是切片一个有用的特性,当len和cap都为0时,则是一个空切片
	//切片高效操作要点:
	//降低内存分配次数,尽量保证append()操作不会超出cap容量,降低触发内存分配的次数和每次内存分配的大小

	//避免内存泄露,对于引用了底层数据,底层的数组会保存在内存中,直到它不再被引用例子:
	var bb []*int{ ... }
	bb = bb[:len(bb)-1]    //被删除的最后一个元素依然被应用,可能导致GC操作被阻碍
	//正确做法
	bb[len(bb)-1] = nil    //先将要删除的元素置为nil
	bb = bb[:len(bb)-1]

	fmt.Println(a,b,c,d,e,f,g,h,i)


}

//利用0长切片删除[]byte切片中的空格
func testSlice(s []byte) []byte {
	b := s[:0]    //初始化一个长度为0,容量为cap(s)的切片b
	for _, x := range s {
		if x != ' ' {
			b = append(b, x)
		}
	}
	return b
}

//slice非常强大,甚至可以取代数组
//slice作为函数的型参时是传引用操作,传递的是指向slice的内存地址,这意味着在函数内对slice的操作会影响原始的slice
//字节slice s := make([]byte, 5),常在输入输出(网络,文件流等)使用较多.
//二维slice s := make([][]int, 4)
func TestSlice() {
	//slice定义以及初始值
	s := []int{1,2,3,4,5}
	si := make([]int, 2)
	fmt.Println(s, si)
	si = nil
	fmt.Println(si)

	//使用[:]以数组创建slice, [:]只是将引用指向数组,并没有创建一份数组的拷贝
	anArray := [5]int{4,5,6,7,8}
	refAnArray := anArray[:]
	fmt.Println("anArray: ", anArray, "reAnArray: ", refAnArray)
	anArray[4] = 100
	fmt.Println(refAnArray)

	//make()创建slice,go将自动初始化slice对应类型的零值.
	sm := make([]byte, 5)
	fmt.Println(sm)
	ts := make([][]int, 3)
	fmt.Println(ts)


}
