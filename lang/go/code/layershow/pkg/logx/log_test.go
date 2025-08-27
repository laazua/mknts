package logx

import (
	"log/slog"
	"testing"
)

// 映射转换
// 便于将配置文件中的配置转化为slog.Level类型
var LogLevelMap = map[string]Level{
	"debug": slog.LevelDebug,
	"info":  slog.LevelInfo,
	"warn":  slog.LevelWarn,
	"error": slog.LevelError,
}

func TestNewLogger(t *testing.T) {
	opts := LoggerOptions{
		FileOptions: RotateFileHandlerOptions{
			MaxSize:     1024 * 1024 * 10, // 10MB 切割
			BackupCount: 20,
		},
		EnableConsole: true,
		LogFormat:     "json", // json or text
		Level:         LogLevelMap["info"],
		AddSource:     false,
	}

	blog, err := NewLogger("logs/app.log", opts)
	if err != nil {
		t.Error("Error creating new logger")
	}
	blog.Info("this is a test", String("hello", "world"))
}
