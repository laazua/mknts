package cli

import (
	"fmt"
	"io"
	"time"
)

// ==================== 上下文扩展方法 ====================

// Printf 格式化输出到标准输出
func (c Context) Printf(format string, args ...any) (int, error) {
	return fmt.Fprintf(c.Stdout, format, args...)
}

// Println 输出一行到标准输出
func (c Context) Println(args ...any) (int, error) {
	return fmt.Fprintln(c.Stdout, args...)
}

// Errorf 格式化错误输出
func (c Context) Errorf(format string, args ...any) (int, error) {
	return fmt.Fprintf(c.Stderr, format, args...)
}

// Errorln 输出错误行
func (c Context) Errorln(args ...any) (int, error) {
	return fmt.Fprintln(c.Stderr, args...)
}

// GetStringFlag 获取字符串标志值
func (c Context) GetStringFlag(name string) (string, bool) {
	if c.Flags == nil {
		return "", false
	}

	flag := c.Flags.Lookup(name)
	if flag == nil {
		return "", false
	}

	return flag.Value.String(), true
}

// GetIntFlag 获取整数标志值
func (c Context) GetIntFlag(name string) (int, error) {
	if c.Flags == nil {
		return 0, fmt.Errorf("flags not available")
	}

	flag := c.Flags.Lookup(name)
	if flag == nil {
		return 0, fmt.Errorf("flag %s not found", name)
	}

	var result int
	_, err := fmt.Sscanf(flag.Value.String(), "%d", &result)
	return result, err
}

// GetBoolFlag 获取布尔标志值
func (c Context) GetBoolFlag(name string) (bool, error) {
	if c.Flags == nil {
		return false, fmt.Errorf("flags not available")
	}

	flag := c.Flags.Lookup(name)
	if flag == nil {
		return false, fmt.Errorf("flag %s not found", name)
	}

	var result bool
	_, err := fmt.Sscanf(flag.Value.String(), "%t", &result)
	return result, err
}

// SetData 设置上下文数据
func (c Context) SetData(key string, value any) {
	if c.Data == nil {
		return
	}
	c.Data[key] = value
}

// GetData 获取上下文数据
func (c Context) GetData(key string) (any, bool) {
	if c.Data == nil {
		return nil, false
	}
	value, exists := c.Data[key]
	return value, exists
}

// MustGetData 必须获取到数据，否则panic
func (c Context) MustGetData(key string) any {
	value, exists := c.GetData(key)
	if !exists {
		panic(fmt.Sprintf("data key '%s' not found in context", key))
	}
	return value
}

// ==================== 中间件支持 ====================

// Middleware 中间件类型
type Middleware func(Context, NextFunc) error

// NextFunc 下一个处理函数
type NextFunc func(Context) error

// Chain 创建中间件链
func Chain(middlewares ...Middleware) Middleware {
	return func(ctx Context, next NextFunc) error {
		// 构建处理链
		var chain NextFunc = next
		for i := len(middlewares) - 1; i >= 0; i-- {
			mw := middlewares[i]
			currentChain := chain
			chain = func(ctx Context) error {
				return mw(ctx, currentChain)
			}
		}
		return chain(ctx)
	}
}

// ==================== 预定义中间件 ====================

// LoggingMiddleware 日志中间件
func LoggingMiddleware(logger io.Writer) Middleware {
	return func(ctx Context, next NextFunc) error {
		start := time.Now()
		fmt.Fprintf(logger, "[%s] 开始执行命令\n", start.Format(time.RFC3339))

		err := next(ctx)

		duration := time.Since(start)
		if err != nil {
			fmt.Fprintf(logger, "[%s] 命令执行失败: %v (耗时: %v)\n",
				time.Now().Format(time.RFC3339), err, duration)
		} else {
			fmt.Fprintf(logger, "[%s] 命令执行成功 (耗时: %v)\n",
				time.Now().Format(time.RFC3339), duration)
		}

		return err
	}
}

// ValidationMiddleware 验证中间件
func ValidationMiddleware(validators ...func(Context) error) Middleware {
	return func(ctx Context, next NextFunc) error {
		for _, validator := range validators {
			if err := validator(ctx); err != nil {
				return fmt.Errorf("验证失败: %w", err)
			}
		}
		return next(ctx)
	}
}
