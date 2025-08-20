### Graceful

- **说明**
1. 优雅退出http服务
2. 单元测试禁用缓存: go test -test.count=1 ./...

- **示例**
```go

package main

import (
	"errors"
	"log/slog"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"
)

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("POST /hook", func(w http.ResponseWriter, r *http.Request) {
		_, err := w.Write([]byte("ok"))
		if err != nil {
			return
		}
	})

	server := &http.Server{
		Addr:         "0.0.0.0:8080",
		Handler:      mux,
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 5 * time.Second,
	}

	start := make(chan error, 1)
	go func() {
		slog.Info("starting server")
		if err := server.ListenAndServe(); err != nil && !errors.Is(err, http.ErrServerClosed) {
			start <- err
		}
	}()

	// 等待中断信号
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM, syscall.SIGQUIT)

	select {
	case err := <-start:
		slog.Error("server start error ", slog.String("err", err.Error()))
	case sig := <-quit:
		slog.Info("received signal ", slog.String("signal", sig.String()))
	}
}

```
