package core

import (
	"context"
	"encoding/json"
	"net/http"
	"strings"
)

// ------ 路径参数绑定 ------- //
type route struct {
	Method  string
	Pattern string
	Handler http.HandlerFunc
}

type MuxServer struct {
	routes []route
	mux    *http.ServeMux // 嵌入 http.ServeMux 实例
}

type Mstring string

// NewMuxServer 创建并返回一个 MuxServer 实例
func NewMuxServer() *MuxServer {
	return &MuxServer{
		mux:    http.NewServeMux(), // 初始化 http.ServeMux
		routes: []route{},          // 初始化自定义路由信息
	}
}

// ServeHTTP 实现 http.Handler 接口，处理请求
func (p *MuxServer) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	// 设置 CORS 头
	w.Header().Set("Access-Control-Allow-Origin", "*") // 允许所有来源
	w.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")
	// 先处理 ServeMux 的静态文件和其他路由
	if p.mux != nil {
		if _, patternExists := p.mux.Handler(r); patternExists != "" {
			p.mux.ServeHTTP(w, r)
			return
		}
	}

	// 然后处理自定义路由
	for _, route := range p.routes {
		if route.Method != r.Method {
			continue
		}
		if params, ok := match(route.Pattern, r.URL.Path); ok {
			ctx := r.Context()
			for key, value := range params {
				ctx = context.WithValue(ctx, Mstring(key), Mstring(value))
			}
			c := &Context{Writer: w, Request: r.WithContext(ctx)}
			route.Handler(c.Writer, c.Request)
			return
		}
	}
	http.NotFound(w, r)
}

// HandleFunc 添加自定义路由
func (p *MuxServer) HandleFunc(uri string, handler func(http.ResponseWriter, *http.Request)) {
	parts := strings.SplitN(uri, " ", 2)
	if len(parts) != 2 {
		// 如果 `uri` 格式不正确，返回一个错误，或者你可以选择使用默认值处理
		panic("handleFunc Format: HandleFunc('METHOD path', http.handler)")
	}
	method := parts[0]
	pattern := parts[1]
	p.routes = append(p.routes, route{
		Method:  method,
		Pattern: pattern,
		Handler: handler,
	})
}

// Handle 添加 ServeMux 的路由
func (p *MuxServer) Handle(pattern string, handler http.Handler) {
	p.mux.Handle(pattern, handler)
}

// match 用于匹配带参数的路径
func match(pattern, path string) (map[string]string, bool) {
	patternParts := strings.Split(pattern, "/")
	pathParts := strings.Split(path, "/")

	if len(patternParts) != len(pathParts) {
		return nil, false
	}

	params := make(map[string]string)
	for i := 0; i < len(patternParts); i++ {
		if strings.HasPrefix(patternParts[i], ":") {
			paramName := strings.TrimPrefix(patternParts[i], ":")
			params[paramName] = pathParts[i]
		} else if patternParts[i] != pathParts[i] {
			return nil, false
		}
	}

	return params, true
}

// --------Context--------
type H map[string]interface{}

type Context struct {
	Writer  http.ResponseWriter
	Request *http.Request
	H       map[string]interface{}
}

func (c *Context) BindJSON(obj interface{}) error {
	decoder := json.NewDecoder(c.Request.Body)
	return decoder.Decode(obj)
}

func (c *Context) JSON(statusCode int, obj interface{}) {
	c.Writer.Header().Set("Content-Type", "application/json")
	c.Writer.WriteHeader(statusCode)
	json.NewEncoder(c.Writer).Encode(obj)
}
