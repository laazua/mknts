package build-in-method

import(
	"fmt"
	"reflect"
)

// make方法: 创建slice, map, chan, 返回引用类型
func makeSlice() {
	mSlice := make([]string, 3)
	mSlice[0] = "apple"
	mSlice[1] = "oringle"
	mSlice[2] = "bnanla"
	fmt.Println(mSlice)
}

func makeMap() {
	mMap := make(map[int]string)
	mMap[1] = "aaa"
	mMap[4] = "bbb"
	fmt.Println(mMap)
}

func makeChan() {
	mChan := make(chan int, 3)
	mChan <- 1
	mChan <- 2
	mChan <- 3
}

// new方法: 返回传入类型的指针地址, 会将指向的内存置零
func newMap() {
	nMap := new(map[int]string)
	fmt.Println(reflect.TypeOf(nMap))
}

// append & delete & copy
// slice: append & copy
// map: delete


// panic & recover 处理异常
// panic抛出异常
// recover捕获异常
func receivePanic() {
	defer coverPanic()
	panic("i am panic")
}

func coverPanic() {
	msg := recover()
	switch msg.(type) {
	case string:
		fmt.Println("string type: ", msg)
	case error:
		fmt.Println("error type: ", msg)
	default:
		fmt.Println("unknown panic: ", msg)
	}
}

// len & cap & close
// len: string, array, slice, map, chan
// cap: slice, array, chan
// close: chan   关闭后不能往chan中写数据