package main

import (
	"fmt"
	"log/slog"
	"net/http"
	"os"

	"github.com/Sseve/imux"
)

// Logger 中间件示例
// 示例中间件
func Logger(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		println("Request:", r.Method, r.URL.Path)
		next.ServeHTTP(w, r)
	})
}

func Auth(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		token := r.Header.Get("Authorization")
		if token == "" {
			http.Error(w, "Unauthorized", http.StatusUnauthorized)
			return
		}
		next.ServeHTTP(w, r)
	})
}

type UserForm struct {
	Name     string `json:"name"`
	Password string `json:"password"`
}

func main() {
	imux.LoadEnv(".env")

	mux := imux.NewRouter()
	// 添加全局中间件
	mux.Use(Logger)

	mux.Get("/ping", func(w http.ResponseWriter, r *http.Request) {
		imux.Success(w, imux.Map{"code": 200, "message": "pong"})
	})

	// 获取 < /pong?name=zhangsan&password=123456 > 查询参数
	mux.Get("/pong", func(w http.ResponseWriter, r *http.Request) {
		name := r.URL.Query().Get("name")
		password := r.URL.Query().Get("password")
		imux.Success(w, imux.Map{"code": 200, "message": "pong", "name": name, "password": password})
	})

	// 路由分组: /v2/hello 增删改查等 (RESTful API)
	v1 := mux.Group("/v1")
	v1.Get("/hello", func(w http.ResponseWriter, r *http.Request) {
		imux.Success(w, imux.Map{"code": 200, "message": "Get hello"})
	})

	v1.Post("/hello", func(w http.ResponseWriter, r *http.Request) {
		imux.Success(w, imux.Map{"code": 200, "message": "Post hello"})
	})

	v1.Delete("/hello", func(w http.ResponseWriter, r *http.Request) {
		imux.Success(w, imux.Map{"code": 200, "message": "Delete hello"})
	})

	v1.Put("/hello", func(w http.ResponseWriter, r *http.Request) {
		imux.Success(w, imux.Map{"code": 200, "message": "Put hello"})
	})

	// 路由分组(加入中间件)
	api := mux.Group("/api", Auth)
	api.Get("/user/:id", func(w http.ResponseWriter, r *http.Request) {
		id := imux.Param(r, "id")
		imux.Success(w, imux.Map{"code": 200, "message": "Get user id: " + id})
	})

	api.Post("/user", func(w http.ResponseWriter, r *http.Request) {
		var user UserForm
		if err := imux.Bind(r, &user); err != nil {
			imux.Failure(w, imux.Map{"code": 500, "message": "bind user error"})
			return
		}
		imux.Success(w, imux.Map{"code": 200, "message": "Create user success"})
	})

	// 启动服务
	server := http.Server{Addr: os.Getenv("app.address"), Handler: mux}
	slog.Info(fmt.Sprintf("start server: %v", server.Addr))
	if err := server.ListenAndServe(); err != nil {
		panic(err)
	}
}
