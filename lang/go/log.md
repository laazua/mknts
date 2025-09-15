### log

- **日志切割**
```go
// 主要实现io.Writer接口(Write方法)
package main

import (
	"fmt"
	"os"
	"path/filepath"
	"sync"
	"time"
)

func main() {
     // 设置标准库的logger
     options := RoTatingOptions{
		BaseDir:    "logs",
		BaseName:   "app",
		MaxSize:    10 * 1024 * 1024, // 10M
		MaxBackups: 5,                // 保留5个备份
	}
	rotatingWriter := NewRotatingWriter(options) // 10MB, 保留5个备份
    defer rotatingWriter.Close()   // 在程序退出时进行资源释放

	// 创建slog handler
	handler := slog.NewTextHandler(rotatingWriter, &slog.HandlerOptions{
		Level: slog.LevelInfo,
	})

	// 设置默认logger
	slog.SetDefault(slog.New(handler))


}

// =========== 将下面代码封装成一个包 ===========

// RotatingWriter 实现io.Writer接口的轮转writer
type RotatingWriter struct {
	mu          sync.Mutex
	baseDir     string
	baseName    string
	maxSize     int64
	maxBackups  int
	currentFile *os.File
	currentSize int64
}

func NewRotatingWriter(options RoTatingOptions) *RotatingWriter {
	return &RotatingWriter{
		baseDir:    options.BaseDir,
		baseName:   options.BaseName,
		maxSize:    options.MaxSize,
		maxBackups: options.MaxBackups,
	}
}

type RoTatingOptions struct {
	BaseDir    string
	BaseName   string
	MaxSize    int64
	MaxBackups int
}

func (w *RotatingWriter) Write(p []byte) (n int, err error) {
	w.mu.Lock()
	defer w.mu.Unlock()

	if err := w.ensureFile(); err != nil {
		return 0, err
	}

	// 检查是否需要轮转
	if w.currentSize+int64(len(p)) > w.maxSize {
		if err := w.rotate(); err != nil {
			return 0, err
		}
	}

	n, err = w.currentFile.Write(p)
	if err == nil {
		w.currentSize += int64(n)
	}
	return n, err
}

func (w *RotatingWriter) ensureFile() error {
	if w.currentFile != nil {
		return nil
	}

	os.MkdirAll(w.baseDir, 0755)

	filename := filepath.Join(w.baseDir, w.baseName+".log")
	file, err := os.OpenFile(filename, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0644)
	if err != nil {
		return err
	}

	info, err := file.Stat()
	if err != nil {
		file.Close()
		return err
	}

	w.currentFile = file
	w.currentSize = info.Size()
	return nil
}

func (w *RotatingWriter) rotate() error {
	if w.currentFile == nil {
		return nil
	}

	w.currentFile.Close()

	// 重命名当前文件
	oldFile := filepath.Join(w.baseDir, w.baseName+".log")
	timestamp := time.Now().Format("20060102-150405")
	newFile := filepath.Join(w.baseDir, fmt.Sprintf("%s.%s.log", w.baseName, timestamp))

	if err := os.Rename(oldFile, newFile); err != nil {
		return err
	}

	// 清理旧文件
	w.cleanupOldFiles()

	// 创建新文件
	file, err := os.OpenFile(oldFile, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0644)
	if err != nil {
		return err
	}

	w.currentFile = file
	w.currentSize = 0
	return nil
}

func (w *RotatingWriter) cleanupOldFiles() {
	if w.maxBackups <= 0 {
		return
	}

	pattern := filepath.Join(w.baseDir, w.baseName+".*.log")
	files, err := filepath.Glob(pattern)
	if err != nil {
		return
	}

	// 保留最新的maxBackups个文件
	if len(files) > w.maxBackups {
		// 简单按文件名排序（时间戳在文件名中）
		for i := 0; i < len(files)-1; i++ {
			for j := i + 1; j < len(files); j++ {
				if files[i] > files[j] {
					files[i], files[j] = files[j], files[i]
				}
			}
		}

		for i := 0; i < len(files)-w.maxBackups; i++ {
			os.Remove(files[i])
		}
	}
}

func (w *RotatingWriter) Close() error {
	w.mu.Lock()
	defer w.mu.Unlock()

	if w.currentFile != nil {
		return w.currentFile.Close()
	}
	return nil
}
```