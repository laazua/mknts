package router

import (
	"net/http"
)

// 中间件类型
type Middleware func(http.Handler) http.Handler

type Router struct {
	Prefix string
	mw     []Middleware
	Mux    *http.ServeMux
	root   *Router
}

func NewRouter() *Router {
	return &Router{
		mw:  []Middleware{},
		Mux: http.NewServeMux(),
	}
}

func (router *Router) Use(mw Middleware) {
	router.mw = append(router.mw, mw)
}

func (router *Router) Group(prefix string) *Router {
	// 创建一个新的 Router 实例，继承当前的中间件
	group := &Router{
		Prefix: router.Prefix + prefix,
		mw:     append([]Middleware{}, router.mw...), // 复制当前中间件
		Mux:    router.Mux,
		root:   router,
	}
	return group
}

// 注册路由并应用全局和分组中间件
func (router *Router) Handle(method, pattern string, handler http.Handler) {
	// 应用全局中间件
	for _, mw := range router.mw {
		handler = mw(handler)
	}

	// 注册到全局的 ServeMux
	root := router.rootRouter() // 找到全局 Router
	root.Mux.HandleFunc(root.Prefix+pattern, func(w http.ResponseWriter, r *http.Request) {
		if r.Method == method {
			handler.ServeHTTP(w, r)
		} else {
			http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
		}
	})
}

// 实现ServeHTTP
func (router *Router) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	router.Mux.ServeHTTP(w, r)
}

// 获取根路由器
func (router *Router) rootRouter() *Router {
	if router.root == nil {
		return router
	}
	return router.root.rootRouter()
}
