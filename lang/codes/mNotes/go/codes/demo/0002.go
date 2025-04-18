// 模拟过期的kv
package main


import(
    "fmt"
    "sync"
    "time"
)

// 声明线程安全的map
var Kv sync.Map

func Set(k string, v interface{}, expire time.Duration) {
    Kv.Store(k, v)
    time.AfterFunc(expire, func() {
        Kv.Delete(k)
    })
}

func main() {
    Set("name", "张三", 4*time.Second)
    Set("age", 12, 6*time.Second)

    for i:= 0; i < 5; i++ {
        fmt.Println(Kv.Load("name"))
        fmt.Println(Kv.Load("age"))
        time.Sleep(2*time.Second)
    }
}
