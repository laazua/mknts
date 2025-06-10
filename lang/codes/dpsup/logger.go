package main

import (
	"log/slog"
	"os"
)

var logger *slog.Logger

func NewLogger() {
	logFile, err := os.OpenFile(logfile, os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		panic("创建日志文件失败")
	}
	// 设置日志处理器为 Text 格式，并设置日志级别
	handler := slog.NewTextHandler(logFile, &slog.HandlerOptions{
		Level: slog.LevelInfo, // 设置日志级别为 Info，保证至少记录 Info 级别的日志
	})

	// 创建一个新的 Logger，使用 Text 格式的处理器
	logger = slog.New(handler)
}
