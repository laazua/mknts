###

- http server

```
////////////////////engin///////////////////////
import "net/http"

type HandleFunc func(*Context)

// 实现ServeHTTP接口的类
type Engine struct {
	route *route
}

// 实例化Engine类
func New() *Engine {
	return &Engine{route: newRouter()}
}

// 注册请求方法,路由和处理函数
func (e *Engine) registerRoute(method string, pattern string, handler HandleFunc) {
	e.route.addRoute(method, pattern, handler)
}

// GET请求处理函数
func (e *Engine) Get(pattern string, handler HandleFunc) {
	e.registerRoute("GET", pattern, handler)
}

// POST请求处理函数
func (e *Engine) Post(pattern string, handler HandleFunc) {
	e.registerRoute("POST", pattern, handler)
}

// 启动服务
func (e *Engine) Run(addr string) (err error) {
	return http.ListenAndServe(addr, e)
}

// 实现ServeHTTP接口
func (e *Engine) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	c := newContext(w, req)
	e.route.handle(c)
}
////////////////////route///////////////////////
import "net/http"

type route struct {
	handles map[string]HandleFunc
}

func newRouter() *route {
	return &route{handles: make(map[string]HandleFunc)}
}

func (r *route) addRoute(method string, pattern string, handler HandleFunc) {
	key := method + "-" + pattern
	r.handles[key] = handler
}

func (r *route) handle(ctx *Context) {
	key := ctx.Method + "-" + ctx.Path
	if handler, ok := r.handles[key]; ok {
		handler(ctx)
	} else {
		ctx.String(http.StatusNotFound, "404 NOT FOUND: %s\n", ctx.Path)
	}
}

////////////////////context///////////////////////
import (
	"encoding/json"
	"fmt"
	"net/http"
)

type H map[string]interface{}

type Context struct {
	W          http.ResponseWriter
	R          *http.Request
	Path       string
	Method     string
	StatusCode int
}

func newContext(w http.ResponseWriter, r *http.Request) *Context {
	return &Context{
		W:      w,
		R:      r,
		Path:   r.URL.Path,
		Method: r.Method,
	}
}

func (ctx *Context) PostForm(key string) string {
	return ctx.R.FormValue(key)
}

func (ctx *Context) Query(key string) string {
	return ctx.R.URL.Query().Get(key)
}

func (ctx *Context) Status(code int) {
	ctx.StatusCode = code
	ctx.W.WriteHeader(code)
}

func (ctx *Context) SetHeader(key, value string) {
	ctx.W.Header().Set(key, value)
}

func (c *Context) String(code int, format string, values ...interface{}) {
	c.SetHeader("Content-Type", "text/plain")
	c.Status(code)
	c.W.Write([]byte(fmt.Sprintf(format, values...)))
}

func (c *Context) JSON(code int, obj interface{}) {
	c.SetHeader("Content-Type", "application/json")
	c.Status(code)
	encoder := json.NewEncoder(c.W)
	if err := encoder.Encode(obj); err != nil {
		http.Error(c.W, err.Error(), 500)
	}
}

func (c *Context) Data(code int, data []byte) {
	c.Status(code)
	c.W.Write(data)
}

func (c *Context) HTML(code int, html string) {
	c.SetHeader("Content-Type", "text/html")
	c.Status(code)
	c.W.Write([]byte(html))
}


```
