//pprof: go程序性能分析工具
package main

import (
	"log"
	"net/http"
	"time"

	_ "net/http/pprof" // 引用pprof，以便对程序进行性能分析
)

var datas []string

func main() {
	go func() {
		for {
			log.Printf("len: %d", Add("go-programming-tour-book"))
			time.Sleep(time.Millisecond * 10)
		}
	}()

	_ = http.ListenAndServe("0.0.0.0:8080", nil)
}

func Add(str string) int {
	data := []byte(str)
	datas = append(datas, string(data))
	return len(datas)
}

// 访问http://127.0.0.1:8080/debug/pprof/
// allocs：查看过去所有内存分配的样本，访问路径为$HOST/debug/pprof/allocs
// block：查看导致阻塞同步的堆栈跟踪，访问路径为$HOST/debug/pprof/block
// cmdline：当前程序的命令行的完整调用路径
// goroutine：查看当前所有运行的 goroutines 堆栈跟踪，访问路径为$HOST/debug/pprof/goroutine
// heap：查看活动对象的内存分配情况， 访问路径为$HOST/debug/pprof/heap
// mutex：查看导致互斥锁的竞争持有者的堆栈跟踪，访问路径为$HOST/debug/pprof/mutex
// profile：默认进行 30s 的 CPU Profiling，得到一个分析用的 profile 文件，访问路径为$HOST/debug/pprof/profile
// threadcreate：查看创建新OS线程的堆栈跟踪，访问路径为$HOST/debug/pprof/threadcreate
// 在以上路径后面加上?dubug=1

// go tool pprof https+insecure://localhost:6060/debug/pprof/profile\?seconds\=60
// go tool pprof http://localhost:6060/debug/pprof/profile\?seconds\=60
