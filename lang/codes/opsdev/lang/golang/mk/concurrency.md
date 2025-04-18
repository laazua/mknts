### 并发

- **并发控制**
1. sync.WaitGroup
```go
// 此示例将启动 3 个 goroutines,
// 分别休眠 0 秒、1 秒和 2 秒,
// main 函数将在这 3 个 goroutine 结束后退出
package main

import (
    "fmt"
    "sync"
    "time"
)

func main() {
    var wg sync.WaitGroup

    for i := 0; i < 3; i++ {
        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            fmt.Printf("sub goroutine sleep: %ds\n", i)
            time.Sleep(time.Duration(i) * time.Second)
        }(i)
    }

    wg.Wait()
    fmt.Println("main func done")
}
```

2. channel
- 使用无缓冲通道进行同步
```go
// 无缓冲通道可用于实现 producer-consumer 模式.
// 在这个模式中，一个协程负责生产数据,
// 另一个协程负责消费数据。当生产者协程向通道发送数据时,
// 消费者协程将进入阻塞状态并等待数据到达,
// 这样可以保证生产者和消费者之间的数据同步。
package main

import (
    "fmt"
    "sync"
    "time"
)

func producer(ch chan int, wg *sync.WaitGroup) {
    defer wg.Done()
    for i := 0; i < 10; i++ {
        ch <- i
        fmt.Println("produced", i)
        time.Sleep(100 * time.Millisecond)
    }
    close(ch)
}

func consumer(ch chan int, wg *sync.WaitGroup) {
    defer wg.Done()
    for i := range ch {
        fmt.Println("consumed", i)
        time.Sleep(150 * time.Millisecond)
    }
}

func main() {
    var wg sync.WaitGroup
    ch := make(chan int)

    wg.Add(2)
    go producer(ch, &wg)
    go consumer(ch, &wg)

    wg.Wait()
}
```
- 使用缓冲通道进行速率限制
```go
// 缓冲通道可以用来限制并发 goroutine 的数量.
// 具体的方法是将 channel 的容量设置为所需的最大并发 goroutine 数.
// 在启动每个 goroutine 之前，向 channel 发送一个值;当 goroutine 完成执行时,
// 从 Channel 接收一个值。这样就可以保证同时运行的 goroutine 数量不超过指定的最大并发数.
package main

import (
    "fmt"
    "sync"
)

func main() {
    var wg sync.WaitGroup
    maxConcurrency := 3
    semaphore := make(chan struct{}, maxConcurrency)

    for i := 0; i < 10; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            semaphore <- struct{}{}
            fmt.Println("goroutine", i, "started")
            // do some work
            fmt.Println("goroutine", i, "finished")
            <-semaphore
        }()
    }

    wg.Wait()
}
```

3. context.Context
- 超时控制
```go
// 在某些情况下，为了避免程序长期阻塞或死锁等问题，有必要限制 goroutine 的执行时间.
// Context 可以帮助开发者更好地控制 goroutine 的执行时间.
// 具体作是创建一个带有超时时间的 Context 并将其传递给 goroutine.
// 如果 goroutine 未能在超时时间内完成执行，则可以使用 Context 的 Done 方法取消 goroutine 的执行.
package main

import (
    "context"
    "fmt"
    "time"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
    defer cancel()

    go func() {
        for {
            select {
            case <-ctx.Done():
                fmt.Println("goroutine finished")
                return
            default:
                fmt.Println("goroutine running")
                time.Sleep(500 * time.Millisecond)
            }
        }
    }()

    time.Sleep(3 * time.Second)
}
```
- 取消操作
```go
// 在程序的运行过程中，有时需要取消某些 goroutine 的执行.
// Context 可以帮助开发者更好地控制 goroutine 的取消作.
// 具体的方法是创建一个带有取消函数的 Context 并将其传递给 goroutine.
// 果需要取消 goroutine 的执行，可以调用 Context 的 Cancel 方法.
package main

import (
    "context"
    "fmt"
    "sync"
    "time"
)

func main() {
    ctx, cancel := context.WithCancel(context.Background())

    var wg sync.WaitGroup
    wg.Add(1)
    go func() {
        defer wg.Done()
        for {
            select {
            case <-ctx.Done():
                fmt.Println("goroutine finished")
                return
            default:
                fmt.Println("goroutine running")
                time.Sleep(500 * time.Millisecond)
            }
        }
    }()

    time.Sleep(2 * time.Second)
    cancel()
    wg.Wait()
}
```
- 资源管理
```go
// 在某些场景下，需要对 goroutine 使用的资源进行管理，以防止资源泄漏或竞争条件等问题.
// Context 可以帮助开发人员更好地管理 goroutines 使用的资源.
// 具体作是将资源与 Context 关联起来，并将 Context 传递给 goroutine.
// 当 goroutine 完成执行时，Context 可用于释放资源或执行其他资源管理作.
package main

import (
    "context"
    "fmt"
    "sync"
    "time"
)

func worker(ctx context.Context, wg *sync.WaitGroup) {
    defer wg.Done()
    for {
        select {
        case <-ctx.Done():
            fmt.Println("goroutine finished")
            return
        default:
            fmt.Println("goroutine running")
            time.Sleep(500 * time.Millisecond)
        }
    }
}

func main() {
    ctx, cancel := context.WithCancel(context.Background())

    var wg sync.WaitGroup
    wg.Add(1)
    go worker(ctx, &wg)

    time.Sleep(2 * time.Second)
    cancel()
    wg.Wait()
}
```