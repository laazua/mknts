//当一只鸟走起来像鸭子,游泳时像鸭子,叫起来也像鸭子,那么这只鸟就可以被称为鸭子
//空接口类型变量可以存储任何类型的数值,我们可以通过断言得知变量里数值的具体类型.
//与struct一样, interface也可以通过匿名字段进行继承
package main

import(
	"fmt"
)

type Human struct {
	name  string
	age   int
	phone string
}

type Student struct{
	Human	//匿名字段
	school  string
	loan    float32
}

type Employee struct {
	Human    //匿名字段
	company   string
	money     float32
}

//Human实现SayHi()方法
func (h Human) SayHi(){
	fmt.Printf("Hi, I am %s you can call me on %s\n", h.name, h.phone)
}

//Human实现Sing(lyrics string)方法
func (h Human) Sing(lyrics string){
	fmt.Println("La la la la...", lyrics)
}

//Employee重写SayHi()方法
func(e Employee) SayHi(){
	fmt.Printf("Hi, I am %s, I work at %s. Call me on %s\n", e.name, e.company, e.phone)
}

//接口Men被Humen, Student, Emplayee实现,因为这三个类都实现了SayHi和Sing方法
type Men interface {
	SayHi()
	Sing(lyrics string)
}

func main() {
	mike := Student{Human{"Mike",25,"222-222-xxx"},"MIT",0.00}
	paul := Student{Human{"Paul",26,"111-222-xxx"},"Harvard",100}
	sam  := Employee{Human{"Sam",36,"444-222-xxx"},"Golang Inc.",1000}
	Tom  := Employee{Human{"Sam",36,"444-222-xxx"},"Things Ltd.",5000}

	//定义接口Men类型变量i
	var i Men

	//i能存储Student
	i = mike
	fmt.Println("This is Mike, a Student:")
	i.SayHi()
	i.Sing("November rain")

	//i也能存储Employee
	i = Tom
	fmt.Println("This is Tom, an Employee:")
	i.SayHi()
	i.Sing("Born to be wild")

	//定义slice Men
	fmt.Println("Let's use a slice of Men and see what happens")
	x := make([]Men, 3)
	//T这三个都是不同类型的元素,但是它们都实现了interface同一个接口
	x[0], x[1], x[2] = paul, sam, mike
	for _, value := range x{
		value.SayHi()
	}
}
