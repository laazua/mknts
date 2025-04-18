#### 变量

```
package main

import "fmt"

// 声明全局变量
var (
    Sunday = iota
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
)

func main() {
    // 变量声明
    var num int
    var str string
    
    // 变量赋值
    num = 100
    str = "test var"

    // 声明并赋值
    var name = "zhangsan"
    var age int = 18
    address := "xxxxxx"

    fmt.Println(num)
    fmt.Println(str)
}
```