package views

import (
	"embed"
	"net/http"
	"text/template"
)

var templates *template.Template

//go:embed templates/*
var templatesFs embed.FS

func init() {
	//templates = template.Must(template.ParseGlob("views/templates/*.html"))
	templates = template.Must(template.ParseFS(templatesFs, "templates/*.html"))
}

func renderTemplate(w http.ResponseWriter, tmpl string, data any) {
	var err error
	cxtData := map[string]any{
		"Page": tmpl, // 子模板的名称
		"Data": data, // 子模板的数据
	}
	// 检查是否是 login.html 模板，特殊处理
	if tmpl == "login.html" {
		err = templates.ExecuteTemplate(w, tmpl, nil)
	} else {
		// 渲染 layout.html 并传递 context
		err = templates.ExecuteTemplate(w, "layout.html", cxtData)
	}
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

// 登陆返回数据
type loginResp struct {
	ErrMsg string
}
