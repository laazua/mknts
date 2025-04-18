// log package
package main

import (
	"fmt"
	"log"
	"os"
)

func init() {
	log.SetFlags(log.Llongfile | log.Lmicroseconds | log.Ldate)
	log.Println("test set log format...")
	log.SetPrefix("[TEST]")

	if logFile, err := os.Open("./test.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0644); err != nil {
		fmt.Println("open log file failed, error: ", err)
	} else {
		log.SetOutput(logFile)
	}
}

func customLogger(msg ...interface{}) {
	logger := log.New(os.Stdout, "[TEST]", log.Lshortfile|log.Ldate|log.Ltime)
	logger.Panicln(msg)
}

func main() {
	// 设置日志输出格式和输出位置
	customLogger("自定义的logger记录日志.")
}
