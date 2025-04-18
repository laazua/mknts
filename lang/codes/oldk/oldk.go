package oldk

import (
	"net/http"
)

// 手动实现http.handler接口的实例
type HandlerFunc func(*Context)

type Engine struct {
	router *route
}

func New() *Engine {
	return &Engine{router: newRoute()}
}

func (e *Engine) addRoute(method, pattern string, handler HandlerFunc) {
	e.router.addRoute(method, pattern, handler)
}

// get 请求
func (e *Engine) Get(pattern string, handler HandlerFunc) {
	e.addRoute("Get", pattern, handler)
}

// post请求
func (e *Engine) Post(pattern string, handler HandlerFunc) {
	e.addRoute("Post", pattern, handler)
}

// 其他请求在此添加

// 启动web服务
func (e *Engine) Run(addr string) error {
	return http.ListenAndServe(addr, e)
}

// 实现http.handler接口
func (e *Engine) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	e.router.handle(NewContext(w, r))
}
