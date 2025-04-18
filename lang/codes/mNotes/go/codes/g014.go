package main

import(
    "fmt"
    "time"
)

func main() {
    // 必须在panic之前声明defer 
    defer func() {
        if err := recover(); err != nil {
            // 记录异常
            fmt.Println(err)
        }
        
        // 恢复程序后执行的代码
        for {
            fmt.Println(111)
            time.Sleep(2*time.Second)
        }
    }()
    // 遇到异常的代码
    panic("手动抛出错误")
}
