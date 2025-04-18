
// 单例模式: 一个类只有一个实例
package main

import(
    "fmt"
    "sync"
)


type Single struct {
	Name string
}


var (
    Instance *Single
    once = sync.Once{}
)


func GetSingleInstance() *Single {
	if Instance == nil {
            once.Do(func() {
	        Instance = new(Single)
            })
	}
	return Instance
}


func main() {
	s1 := GetSingleInstance()
	s1.Name = "张三"
	s2 := GetSingleInstance()
	s2.Name = "李四"

	fmt.Printf("%p\n", s1)
	fmt.Printf("%p\n", s2)
	fmt.Println(s1.Name)
	fmt.Println(s2.Name)

        // 高并发测试
        wg := sync.WaitGroup{}
        for i := 0; i < 10; i++ {
            wg.Add(1)
            go func() {
                s := GetSingleInstance()
                fmt.Printf("%p \n %s \n", s, s.Name)
                wg.Done()
            }()
        }
        wg.Wait()
}
