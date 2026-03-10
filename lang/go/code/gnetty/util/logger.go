package util

import (
    "fmt"
    "log"
    "os"
    "time"
)

// LogLevel 日志级别
type LogLevel int

const (
    DEBUG LogLevel = iota
    INFO
    WARN
    ERROR
    FATAL
)

var levelNames = []string{"DEBUG", "INFO", "WARN", "ERROR", "FATAL"}

// Logger 日志记录器
type Logger struct {
    level  LogLevel
    logger *log.Logger
}

// NewLogger 创建新的日志记录器
func NewLogger(level LogLevel) *Logger {
    return &Logger{
        level:  level,
        logger: log.New(os.Stdout, "", log.LstdFlags),
    }
}

// SetLevel 设置日志级别
func (l *Logger) SetLevel(level LogLevel) {
    l.level = level
}

// Debug 记录调试信息
func (l *Logger) Debug(msg string, args ...interface{}) {
    if l.level <= DEBUG {
        l.log(DEBUG, msg, args...)
    }
}

// Info 记录信息
func (l *Logger) Info(msg string, args ...interface{}) {
    if l.level <= INFO {
        l.log(INFO, msg, args...)
    }
}

// Warn 记录警告信息
func (l *Logger) Warn(msg string, args ...interface{}) {
    if l.level <= WARN {
        l.log(WARN, msg, args...)
    }
}

// Error 记录错误信息
func (l *Logger) Error(msg string, args ...interface{}) {
    if l.level <= ERROR {
        l.log(ERROR, msg, args...)
    }
}

// Fatal 记录致命错误并退出
func (l *Logger) Fatal(msg string, args ...interface{}) {
    l.log(FATAL, msg, args...)
    os.Exit(1)
}

func (l *Logger) log(level LogLevel, msg string, args ...interface{}) {
    timestamp := time.Now().Format("2006-01-02 15:04:05")
    prefix := fmt.Sprintf("[%s] [%s] ", timestamp, levelNames[level])

    if len(args) > 0 {
        msg = fmt.Sprintf(msg, args...)
    }

    l.logger.Println(prefix + msg)
}