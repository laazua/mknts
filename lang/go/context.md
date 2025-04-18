### context包

- 示例说明
```go
package main

import (
	"context"
	"fmt"
	"time"
)

/**
context 包是 Go 标准库中的一个非常重要的包，它主要用于跨 API 边界传递请求范围的上下文信息，
特别是在处理并发和网络请求时，能够有效地管理请求的生命周期、传递取消信号以及携带元数据。
它尤其在需要取消操作或在多个 goroutine 中传递请求相关数据时非常有用。

context 包中的核心概念是 Context 类型。Context 是一个接口，负责传递跨 API 边界的数据，通常用于：
  - 请求取消信号。
  - 请求的截止时间。
  - 传递一些请求范围的数据。
Context 的具体实现并不复杂，通常通过两种方式来创建和使用：通过 context.Background() 或 context.TODO() 创建根上下文，
然后可以通过 WithCancel(), WithDeadline(), WithTimeout(), 或 WithValue() 来派生出子上下文。

常用方法：
  - context.Background(): 返回一个空的 Context，通常作为所有上下文的根上下文，通常在 main 函数或测试中使用。
  - context.TODO(): 用于尚不确定何时使用上下文的地方，通常是一个占位符，后续可以替换为合适的上下文。
  - WithCancel(parent Context): 返回一个新的 Context 和一个取消函数，取消函数用于通知取消操作。
  - WithDeadline(parent Context, deadline time.Time): 返回一个新的 Context，该上下文在指定的截止时间之后自动取消。
  - WithTimeout(parent Context, timeout time.Duration): 返回一个新的 Context，该上下文在指定的时间段后自动取消，实际上是 WithDeadline 的一个简化版。
  - WithValue(parent Context, key, value interface{}): 返回一个新的 Context，它携带了键值对，用于在多个函数之间传递数据。
*/

// RootContext 创建根上下文
func RootContext() {
	ctx1 := context.TODO()
	fmt.Println("TODO CTX: ", ctx1)

	ctx2 := context.Background()
	fmt.Println("BACKGROUND CTX: ", ctx2)
}

// CancelContext 创建用于取消的上下文
func CancelContext() {
	ctx, cancel := context.WithCancel(context.Background())

	go func() {
		time.Sleep(2 * time.Second)
		fmt.Println("Task Completed")
		cancel()
	}()

	<-ctx.Done()
	fmt.Println(ctx.Err())
}

// DeadlineContext 创建截至时间上下文
func DeadlineContext() {
	deadline := time.Now().Add(5 * time.Second)
	ctx, cancel := context.WithDeadline(context.Background(), deadline)
	defer cancel()

	select {
	case <-time.After(2 * time.Second):
		fmt.Println("Task Completed Within deadline")
	case <-ctx.Done():
		fmt.Println("Context deadline exceeded:", ctx.Err())
	}
}

// TimeoutContext 超时上下文
func TimeoutContext() {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	select {
	case <-time.After(5 * time.Second):
		fmt.Println("Task Completed")
	case <-ctx.Done():
		fmt.Println("Task Timeout: ", ctx.Err())
	}
}

// ValueContext 值上下文
func ValueContext() {
	// 创建上下文，并存储值
	ctx := context.WithValue(context.Background(), "userID", 12345)

	// 从上下文中获取值
	userID := ctx.Value("userID")
	if userID != nil {
		fmt.Println("User ID:", userID)
	} else {
		fmt.Println("No user ID found in context")
	}
}

// PanelContext 并发使用上下文示例
func PanelContext() {
	// 创建带有取消的上下文
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	go doTask(ctx, "Task 1")
	go doTask(ctx, "Task 2")

	// 模拟运行一段时间后取消任务
	time.Sleep(2 * time.Second)
	cancel()

	// 等待任务完成
	time.Sleep(2 * time.Second)
}

func doTask(ctx context.Context, taskName string) {
	select {
	case <-time.After(3 * time.Second): // 模拟任务执行
		fmt.Println(taskName, "completed")
	case <-ctx.Done(): // 监听取消信号
		fmt.Println(taskName, "canceled:", ctx.Err())
	}
}
```