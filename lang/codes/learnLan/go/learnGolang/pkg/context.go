//  goroutine运行状态,环境,现场等信息
// 在goroutine之间传递上下文信息,如: 取消信号, 超时时间等
package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	go test(ctx, "goroutine one")
	go test(ctx, "goroutine two")
	go test(ctx, "goroutine three")

	time.Sleep(5 * time.Second)
}

func test(ctx context.Context, name string) {
	for {
		select {
		case <-ctx.Done():
			fmt.Println(name, "goroutine stopped...")
			return
		default:
			fmt.Println(name, "goroutine running...")
			time.Sleep(5 * time.Second)
		}
	}
}
