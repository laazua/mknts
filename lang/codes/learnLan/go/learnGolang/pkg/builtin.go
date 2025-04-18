// golang内建类型和函数
package main

import "fmt"

const (
	// true, false是没有类型的
	true  = 1 == 1 //无类型布尔值
	false = 1 != 1 //无类型布尔值
)

func test() {
	const (
		a = iota
		b
		c
	)
	fmt.Println(a, b, c)
}

func main() {
	// type bool  => type bool bool
	// type byte  => type byte byte, uint8别名
	// type rune  => type rune rune, int32别名
	// type int   => type int  int
	// type int8  => type int8 int8  范围:[-128, 127]
	// type int16 => type int16 int16 范围:[-32768,32767]
	// type int32 => type int32 int32 范围:[-2147483648, 2147483647]
	// type int64 => type int64 int64 范围:[-9223372036854775808, 9223372036854775807]
	// type uint  => type uint  uint  至少32位的无符号整形，但和uint32不是同一类型
	// type uint8 => type uint8 uint8 范围:[0, 255]
	// type uint16=> type uint16 uint16  范围:[0, 65535]
	// type uint32=> type uint32 uint32  范围:[0, 4294967295]
	// type uint64=> type uint64 uint64  范围:[0, 18446744073709551615]

	// type float32 => type float32 float32
	// type float64 => type float64 float64

	// type complex64 => type complex64 complex64
	// type complex128 => type complex128 complex128

	// type uintptr => type uintptr uintptr, 可以保存任意指针的位模式的整数类型

	// type string => type string string, 8位byte序列构成的字符串，约定但不必须是utf-8编码的文本。字符串可以为空但不能是nil，其值不可变

	// type error => type error interface { Error() string }, 内建error接口类型是约定用于表示错误信息，nil值表示无错误

	// type Type int, 在本文档中代表任意一个类型，但同一个声明里只代表同一个类型

	// var nil Type, Type必须是指针、通道、函数、接口、映射或切片; nil是预定义的标识符，代表指针、通道、函数、接口、映射或切片的零值

	// func real(c complex64) int, 返回数字类型，复数的实部

	// func imag(c complex64) float64， 返回数字类型, 复数的虚部

	// func complex(r, i int) complex64, 参数为数字类型，返回一个复数

	// func new(Type) *Type, 内建函数new分配内存。其第一个实参为类型，而非值。其返回值为指向该类型的新分配的零值的指针

	// func make(Type, size IntegerType) Type, 内建函数make分配并初始化一个类型为切片、映射、或通道的对象。其第一个实参为类型，而非值.
	// make的返回类型与其参数相同，而非指向它的指针。其具体结果取决于具体的类型:
	// 切片：size指定了其长度。该切片的容量等于其长度。切片支持第二个整数实参可用来指定不同的容量；
	//      它必须不小于其长度，因此 make([]int, 0, 10) 会分配一个长度为0，容量为10的切片。
	// 映射：初始分配的创建取决于size，但产生的映射长度为0。size可以省略，这种情况下就会分配一个
	//	    小的起始大小。
	// 通道：通道的缓存根据指定的缓存容量初始化。若 size为零或被省略，该信道即为无缓存的

	// func cap(v Type) int, 内建函数cap返回 v 的容量，这取决于具体类型
	// 数组：v中元素的数量，与 len(v) 相同
	// 数组指针：*v中元素的数量，与len(v) 相同
	// 切片：切片的容量（底层数组的长度）；若 v为nil，cap(v) 即为零
	// 信道：按照元素的单元，相应信道缓存的容量；若v为nil，cap(v)即为零

	// func len(v Type) int, 内建函数len返回 v 的长度，这取决于具体类型
	// 数组：v中元素的数量
	// 数组指针：*v中元素的数量（v为nil时panic）
	// 切片、映射：v中元素的数量；若v为nil，len(v)即为零
	// 字符串：v中字节的数量
	// 通道：通道缓存中队列（未读取）元素的数量；若v为 nil，len(v)即为零

	// func append(slice []Type, elems ...Type) []Type, 内建函数append将元素追加到切片的末尾。若它有足够的容量，其目标就会重新切片以容纳新的元素。
	// 否则，就会分配一个新的基本数组。append返回更新后的切片，因此必须存储追加后的结果
	// slice = append(slice, elem1, elem2)
	// slice = append(slice, anotherSlice...)
	// 作为特例，可以向一个字节切片append字符串，如下:
	// slice = append([]byte("hello "), "world"...)

	// func copy(dst, src []Type) int, 内建函数copy将元素从来源切片复制到目标切片中，也能将字节从字符串复制到字节切片中。copy返回被复制的元素数量，
	//它会是 len(src) 和 len(dst) 中较小的那个。来源和目标的底层内存可以重叠

	// func delete(m map[Type]Type1, key Type), 内建函数delete按照指定的键将元素从映射中删除。若m为nil或无此元素，delete不进行操作。

	// func close(c chan<- Type), 内建函数close关闭信道，该通道必须为双向的或只发送的。它应当只由发送者执行，而不应由接收者执行，
	// 其效果是在最后发送的值被接收后停止该通道。在最后的值从已关闭的信道中被接收后，任何对其的接收操作都会无阻塞的成功。对于已关闭的信道，语句：
	// x, ok := <-c, 还会将ok置为false

	// func panic(v interface{}), 内建函数panic停止当前Go程的正常执行。当函数F调用panic时，F的正常执行就会立刻停止。F中defer的所有函数先入后出执行后，
	// F返回给其调用者G。G如同F一样行动，层层返回，直到该Go程中所有函数都按相反的顺序停止执行。之后，程序被终止，而错误情况会被报告，包括引发该panic的实参值，
	// 此终止序列称为panic过程。

	// func recover() interface{}, 内建函数recover允许程序管理panic过程中的Go程。在defer的函数中，执行recover调用会取回传至panic调用的错误值，恢复正常执行，
	// 停止panic过程。若recover在defer的函数之外被调用，它将不会停止panic过程序列。在此情况下，或当该Go程不在panic过程中时，或提供给panic的实参为nil时，recover就会返回nil

	// func print(args ...Type), 内建函数print以特有的方法格式化参数并将结果写入标准错误，用于自举和调试

	// func println(args ...Type), println类似print，但会在参数输出之间添加空格，输出结束后换行

}
