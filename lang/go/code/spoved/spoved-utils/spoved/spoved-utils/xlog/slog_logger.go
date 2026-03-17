package xlog

import (
	"context"
	"fmt"
	"io"
	"log/slog"
	"os"
	"spoved-utils/config"
	"strings"

	"gopkg.in/natefinch/lumberjack.v2"
)

type Config struct {
	Level      string
	Filename   string
	MaxSize    int
	MaxBackups int
	MaxAge     int
	Compress   bool
	Json       bool
}

type SLogger struct {
	log *slog.Logger
}

var logLevels = map[string]slog.Level{
	"debug": slog.LevelDebug,
	"info":  slog.LevelInfo,
	"warn":  slog.LevelWarn,
	"error": slog.LevelError,
}

func parseLevel(level string) slog.Level {
	if l, ok := logLevels[strings.ToLower(level)]; ok {
		return l
	}
	return slog.LevelInfo
}

func New() *SLogger {
	fileWriter := &lumberjack.Logger{
		Filename:   config.Get().Log.Filename,
		MaxSize:    config.Get().Log.MaxSize,
		MaxBackups: config.Get().Log.MaxBackups,
		MaxAge:     config.Get().Log.MaxAge,
		Compress:   config.Get().Log.Compress,
	}
	writer := io.MultiWriter(os.Stdout, fileWriter)
	opts := &slog.HandlerOptions{
		Level: parseLevel(config.Get().Log.Level),
	}
	var handler slog.Handler
	if config.Get().Log.Formatter == "json" {
		handler = slog.NewJSONHandler(writer, opts)
	}
	if config.Get().Log.Formatter == "text" {
		handler = slog.NewTextHandler(writer, opts)
	}
	return &SLogger{
		log: slog.New(handler),
	}
}

func (l *SLogger) Debug(msg string, args ...any) {
	l.log.Debug(msg, args...)
}

func (l *SLogger) Info(msg string, args ...any) {
	l.log.Info(msg, args...)
}

func (l *SLogger) Warn(msg string, args ...any) {
	l.log.Warn(msg, args...)
}

func (l *SLogger) Error(msg string, args ...any) {
	l.log.Error(msg, args...)
}

func (l *SLogger) Fatal(msg string, args ...any) {
	l.log.Error(msg, args...)
	os.Exit(1)
}

func (l *SLogger) Debugf(format string, args ...any) {
	l.log.Debug(fmt.Sprintf(format, args...))
}

func (l *SLogger) Infof(format string, args ...any) {
	l.log.Info(fmt.Sprintf(format, args...))
}

func (l *SLogger) Warnf(format string, args ...any) {
	l.log.Warn(fmt.Sprintf(format, args...))
}

func (l *SLogger) Errorf(format string, args ...any) {
	l.log.Error(fmt.Sprintf(format, args...))
}

func (l *SLogger) Fatalf(format string, args ...any) {
	l.log.Error(fmt.Sprintf(format, args...))
	os.Exit(1)
}

func (l *SLogger) DebugContext(ctx context.Context, msg string, args ...any) {
	l.log.DebugContext(ctx, msg, args...)
}

func (l *SLogger) InfoContext(ctx context.Context, msg string, args ...any) {
	l.log.InfoContext(ctx, msg, args...)
}

func (l *SLogger) WarnContext(ctx context.Context, msg string, args ...any) {
	l.log.WarnContext(ctx, msg, args...)
}

func (l *SLogger) ErrorContext(ctx context.Context, msg string, args ...any) {
	l.log.ErrorContext(ctx, msg, args...)
}
