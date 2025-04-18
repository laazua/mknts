package oldk

import "net/http"

type route struct {
	handlers map[string]HandlerFunc
}

func newRoute() *route {
	return &route{handlers: make(map[string]HandlerFunc)}
}

func (r *route) addRoute(method, pattern string, handler HandlerFunc) {
	key := method + "-" + pattern
	r.handlers[key] = handler
}

func (r *route) handle(c *Context) {
	key := c.Method + "-" + c.Path
	if handler, ok := r.handlers[key]; ok {
		handler(c)
	} else {
		c.String(http.StatusNotFound, "404 Not Found: %s\n", c.Path)
	}
}
