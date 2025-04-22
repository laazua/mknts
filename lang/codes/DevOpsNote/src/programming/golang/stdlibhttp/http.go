package stdlibhttp

import (
    "net/http"
)

// 中间件类型
type Middleware func(http.Handler) http.Handler

// RouterGroup 结构体
type RouterGroup struct {
    prefix     string
    middlewares []Middleware
    mux        *http.ServeMux
}

// NewRouterGroup 创建一个新的路由分组
func NewRouterGroup(prefix string) *RouterGroup {
    return &RouterGroup{
        prefix:     prefix,
        middlewares: []Middleware{},
        mux:        http.NewServeMux(),
    }
}

// Use 添加中间件到路由分组
func (g *RouterGroup) Use(middleware Middleware) {
    g.middlewares = append(g.middlewares, middleware)
}

// HandleMethod 注册特定请求方法的路由
func (g *RouterGroup) HandleMethod(method, pattern string, handler http.Handler) {
    // 应用所有中间件
    for _, mw := range g.middlewares {
        handler = mw(handler)
    }
    g.mux.Handle(g.prefix+pattern, http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        if r.Method == method {
            handler.ServeHTTP(w, r)
        } else {
            http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
        }
    }))
}

// ServeHTTP 实现 http.Handler 接口
func (g *RouterGroup) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    g.mux.ServeHTTP(w, r)
}
