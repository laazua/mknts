### router

- **router实现**
```go
package main

import (
	"fmt"
	"net/http"
	"strings"
)

// Router struct is used to store routing rules
type Router struct {
	routes map[string]map[string]http.HandlerFunc
}

// NewRouter creates a new router instance
func NewRouter() *Router {
	return &Router{
		routes: make(map[string]map[string]http.HandlerFunc),
	}
}

// Handle method is used to register routes
func (r *Router) Handle(method, path string, handler http.HandlerFunc) {
	if _, ok := r.routes[method];!ok {
		r.routes[method] = make(map[string]http.HandlerFunc)
	}
	r.routes[method][path] = handler
}

// ServeHTTP method is used to parse HTTP requests and call the corresponding handler functions
func (r *Router) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	methodRoutes, ok := r.routes[req.Method]
	if!ok {
		http.NotFound(w, req)
		return
	}

	handler, ok := methodRoutes[req.URL.Path]
	if!ok {
		// Handle dynamic routing
		for route, h := range methodRoutes {
			if params := matchDynamicRoute(route, req.URL.Path); params != nil {
				req.URL.Query().Set("params", strings.Join(params, ","))
				h(w, req)
				return
			}
		}
		http.NotFound(w, req)
		return
	}

	handler(w, req)
}

// matchDynamicRoute function is used to match dynamic routes
func matchDynamicRoute(route, path string) []string {
	routeParts := strings.Split(route, "/")
	pathParts := strings.Split(path, "/")

	if len(routeParts) != len(pathParts) {
		return nil
	}

	var params []string
	for i, part := range routeParts {
		if strings.HasPrefix(part, ":") {
			params = append(params, pathParts[i])
		} else if part != pathParts[i] {
			return nil
		}
	}

	return params
}

// Middleware is a middleware function type
type Middleware func(http.HandlerFunc) http.HandlerFunc

// Logger is a simple logging middleware
func Logger(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, req *http.Request) {
		fmt.Printf("Received %s request for %s\n", req.Method, req.URL.Path)
		next(w, req)
	}
}

func main() {
	router := NewRouter()

	// Register static route
	router.Handle("GET", "/", func(w http.ResponseWriter, req *http.Request) {
		fmt.Fprintf(w, "Hello, world!")
	})

	// Register dynamic route
	router.Handle("GET", "/hello/:name", func(w http.ResponseWriter, req *http.Request) {
		params := req.URL.Query().Get("params")
		name := strings.Split(params, ",")[0]
		fmt.Fprintf(w, "Hello, %s!", name)
	})

    // use middleware
	router.Handle("GET", "/middleware", Logger(func(w http.ResponseWriter, req *http.Request) {
		fmt.Fprintf(w, "This is a protected route")
	}))

	http.ListenAndServe(":8080", router)
}
```