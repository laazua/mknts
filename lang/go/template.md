### template

- **加载模板**
```go
package api

import (
	"errors"
	"fmt"
	"html/template"
	"path/filepath"
	"strings"
	"sync"
)

type TemplateRender struct {
	mu            sync.RWMutex
	defaultLayout string
}

// 全局渲染器
var Renderer = &TemplateRender{
	defaultLayout: "./web/html/base.html", // 默认前台布局
}

// 渲染模板
func (r *TemplateRender) Render(data any, pageName ...string) (string, error) {
	r.mu.RLock()
	defer r.mu.RUnlock()

	if r.defaultLayout == "" {
		return "", errors.New("未设置默认布局")
	}

	// 组合所有模板文件：布局 + 页面 + 部分模板
	allFiles := []string{r.defaultLayout}
	allFiles = append(allFiles, pageName...)

	fmt.Println("模板文件: ", allFiles)

	// 解析所有模板
	tmpl, err := template.ParseFiles(allFiles...)
	if err != nil {
		return "", fmt.Errorf("解析模板失败: %v", err)
	}

	var buf strings.Builder
	// 使用布局模板的名称作为执行目标
	err = tmpl.ExecuteTemplate(&buf, filepath.Base(r.defaultLayout), data)
	if err != nil {
		return "", fmt.Errorf("执行模板失败: %v", err)
	}

	return buf.String(), nil
}

```

- **使用模板**
```go
func Show(w http.ResponseWriter, r *http.Request) {
	slog.Info("show ....")
	html, err := Renderer.Render(map[string]any{"User": "主人,你好"}, "web/html/index.html", "web/html/a.html")
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	w.Write([]byte(html))
}
```
