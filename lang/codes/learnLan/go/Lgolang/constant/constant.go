//常量是指在编译期间都不会改变值的量
package constant


func main() {
	/*字面常量:程序中硬编码的常量(我们生活中自然语言常量的概念)
	100		    整型常量
	PI(3.14)    浮点型常量
	2 + 3i      复数常量
	false       bool型常量
	"hello"     字符串常量
	*/

	//常量定义
	const (
		PI  float32 = 3.14
		name string = "hello world"

		//编译期间运算常量表达式
		flag = 1 << 2
	)

	//go语言预定义常量: true, false, iota(遇到下一个const关键字时置为0)

	//枚举一系列相关的常量
	const (
		Sunday = iota
		Monday
		Tuesday
		Wednesday
		Thursday
		Friday
		Saturday
		nmberOfDays     //该常量未导出
	)

	//go中大写命名的变量包外可见
}