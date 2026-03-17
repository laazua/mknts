package xlog

import (
	"context"
	"sync"
)

type Logger interface {

	// structured logging
	Debug(msg string, args ...any)
	Info(msg string, args ...any)
	Warn(msg string, args ...any)
	Error(msg string, args ...any)
	Fatal(msg string, args ...any)

	// printf style
	Debugf(format string, args ...any)
	Infof(format string, args ...any)
	Warnf(format string, args ...any)
	Errorf(format string, args ...any)
	Fatalf(format string, args ...any)

	// context logging
	DebugContext(ctx context.Context, msg string, args ...any)
	InfoContext(ctx context.Context, msg string, args ...any)
	WarnContext(ctx context.Context, msg string, args ...any)
	ErrorContext(ctx context.Context, msg string, args ...any)
}

var (
	logger Logger
	once   sync.Once
)

func SetLogger(l Logger) {
	once.Do(func() {
		logger = l
	})
}

func Debug(msg string, args ...any) {
	if logger != nil {
		logger.Debug(msg, args...)
	}
}

func Info(msg string, args ...any) {
	if logger != nil {
		logger.Info(msg, args...)
	}
}

func Warn(msg string, args ...any) {
	if logger != nil {
		logger.Warn(msg, args...)
	}
}

func Error(msg string, args ...any) {
	if logger != nil {
		logger.Error(msg, args...)
	}
}

func Fatal(msg string, args ...any) {
	if logger != nil {
		logger.Fatal(msg, args...)
	}
}

func Debugf(format string, args ...any) {
	if logger != nil {
		logger.Debugf(format, args...)
	}
}

func Infof(format string, args ...any) {
	if logger != nil {
		logger.Infof(format, args...)
	}
}

func Warnf(format string, args ...any) {
	if logger != nil {
		logger.Warnf(format, args...)
	}
}

func Errorf(format string, args ...any) {
	if logger != nil {
		logger.Errorf(format, args...)
	}
}

func Fatalf(format string, args ...any) {
	if logger != nil {
		logger.Fatalf(format, args...)
	}
}

func DebugContext(ctx context.Context, msg string, args ...any) {
	if logger != nil {
		logger.DebugContext(ctx, msg, args...)
	}
}

func InfoContext(ctx context.Context, msg string, args ...any) {
	if logger != nil {
		logger.InfoContext(ctx, msg, args...)
	}
}

func WarnContext(ctx context.Context, msg string, args ...any) {
	if logger != nil {
		logger.WarnContext(ctx, msg, args...)
	}
}

func ErrorContext(ctx context.Context, msg string, args ...any) {
	if logger != nil {
		logger.ErrorContext(ctx, msg, args...)
	}
}
