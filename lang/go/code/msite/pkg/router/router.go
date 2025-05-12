package router

import (
	"context"
	"fmt"
	"net/http"
	"strings"
	"sync"
)

// 路由器结构
type Router struct {
	Mux         *http.ServeMux
	routes      []Route
	middlewares []func(http.Handler) http.Handler
	prefix      string
	parent      *Router
	registered  map[string]map[string]bool
	mu          sync.Mutex
}

// 路由结构
type Route struct {
	method  string
	pattern string
	handler http.Handler
}

// 创建一个新的路由器
func NewRouter() *Router {
	return &Router{
		Mux:        http.NewServeMux(),
		registered: make(map[string]map[string]bool),
	}
}

// 路由分组
func (r *Router) Group(prefix string) *Router {
	return &Router{
		Mux:         r.Mux,
		parent:      r,
		registered:  r.registered,
		prefix:      r.prefix + prefix,
		middlewares: r.middlewares,
	}
}

// 添加中间件
func (r *Router) Use(middleware func(http.Handler) http.Handler) {
	r.middlewares = append(r.middlewares, middleware)
}

// 路由注册方法
func (r *Router) Handle(method, pattern string, handler http.HandlerFunc) {
	fullPattern := r.prefix + pattern
	r.mu.Lock()
	defer r.mu.Unlock()

	// 检查路由冲突
	if _, exists := r.registered[method]; !exists {
		r.registered[method] = make(map[string]bool)
	}
	if r.registered[method][fullPattern] {
		panic(fmt.Sprintf("route conflict: %s %s", method, fullPattern))
	}

	// 包装中间件
	finalHandler := http.Handler(handler)
	for i := len(r.middlewares) - 1; i >= 0; i-- {
		finalHandler = r.middlewares[i](finalHandler)
	}

	// 注册到 mux
	r.Mux.HandleFunc(fullPattern, func(w http.ResponseWriter, req *http.Request) {
		if req.Method != method {
			http.NotFound(w, req)
			return
		}
		if match, params := matchRoute(fullPattern, req.URL.Path); match {
			ctx := req.Context()
			for key, value := range params {
				ctx = context.WithValue(ctx, contextKey(key), value)
			}
			req = req.WithContext(ctx)
			finalHandler.ServeHTTP(w, req)
			return
		}
		http.NotFound(w, req)
	})

	r.routes = append(r.routes, Route{method, fullPattern, handler})
	r.registered[method][fullPattern] = true
}

// 启动 HTTP 服务器
func (r *Router) Run(addr string) error {
	return http.ListenAndServe(addr, r.Mux)
}

// 匹配路径并提取参数
func matchRoute(pattern, path string) (bool, map[string]string) {
	patternParts := strings.Split(strings.Trim(pattern, "/"), "/")
	pathParts := strings.Split(strings.Trim(path, "/"), "/")

	if len(patternParts) != len(pathParts) {
		return false, nil
	}

	params := make(map[string]string)
	for i, part := range patternParts {
		if strings.HasPrefix(part, "{") && strings.HasSuffix(part, "}") {
			paramName := part[1 : len(part)-1]
			params[paramName] = pathParts[i]
		} else if part != pathParts[i] {
			return false, nil
		}
	}
	return true, params
}

// 从上下文中获取路径参数
type contextKey string

func Param(req *http.Request, key string) string {
	if value, ok := req.Context().Value(contextKey(key)).(string); ok {
		return value
	}
	return ""
}
