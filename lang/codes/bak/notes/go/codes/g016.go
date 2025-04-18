// 控制并发协程
package main

import(
    "fmt"
//  "sync"
    "time"
    "context"
)

// channel控制
// func main() {
//    done := make(chan struct{})
//    go func() {
//        fmt.Println("goroutine")
//        done <- struct{}{}
//    }()
//    <- done
//    fmt.Println("main goroutine")
//}

// WaitGroup控制
// func main() {
//    wg := sync.WaitGroup{}
//    wg.Add(3)
//    for i := 0; i < 3; i++ {
//        go func(id int) {
//            fmt.Println(id, "goroutine")
//            wg.Done()
//        }(i)
//    }   
//    wg.Wait()
//    fmt.Println("main goroutine")
// }

// context控制多级协程嵌套
func main() {
    ctx, cancel := context.WithCancel(context.Background())
    go firstGoroutine(ctx)
    fmt.Println("stop all sub goroutine")
    cancel()
    time.Sleep(time.Second * 2)
}

func firstGoroutine(ctx context.Context) {
    go secondGoroutine(ctx)
    for {
        select {
        case <-ctx.Done():
            fmt.Println("first goroutine exit")
            return
        default:
            fmt.Println("first goroutine run")
            time.Sleep(time.Second * 1)
        }
    }
}

func secondGoroutine(ctx context.Context) {
    for {
        select {
        case <-ctx.Done():
            fmt.Println("second goroutine exit")
            return
        default:
            fmt.Println("second goroutine run")
            time.Sleep(time.Second * 1)
        }
    }
}
