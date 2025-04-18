//流程控制
package control

import "fmt"

func main() {
	// if, else 和 else if
	// switch, case, select
	// for, range
	// goto
	// break, continue
}


func switchTest(i int) {
	switch i {
		case 0:
			fmt.Println(0)
		case 1:
			fmt.Println(1)
		case 2:
			fmt.Println(2)
		case 3:
			fmt.Println(3)
		default:
			fmt.Println("default")
	}
}

func selectTest(i, j chan int) {
	select {
		case a := <-i:
			fmt.Println("received ", a, " from i")
		case b := <-i:
			fmt.Println("received ", b, "from j")
		default:
			fmt.Println("over")
	}
}

//for循环代码事例
func testFor() {
	//典型for循环
	for i := 0; i < 100; i++ {
		if i%20 == 0 {
			continue
		}
		if i == 95 {
			break
		}
		fmt.Println(i, " ")
	}

	//for模拟while循环
	i := 10
	for {
		if i < 0 {
			break
		}
		fmt.Println(i, " ")
		i--
	}

	//for模拟do...while
	i = 0
	anExpression := true
	for ok := true; ok; ok = anExpression {
		if i > 10 {
			anExpression = false
		}
		fmt.Println(i, " ")
		i++
	}

	//for ... := range ...
	anArray := [5]int{1,2,3,4,5}
	for i, v := range anArray{
		fmt.Println("index: ", i, "value:", v)
	}
}