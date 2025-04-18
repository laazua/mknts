package stdlibhttp

import (
    "fmt"
    "net/http"
)

// 中间件函数
func loggingMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        fmt.Printf("Request Method: %s, Request URL: %s\n", r.Method, r.URL)
        next.ServeHTTP(w, r) // 调用下一个处理器
    })
}

// 处理器函数
func homeHandler(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("Welcome to the Home Page"))
}

func aboutHandler(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("About Us"))
}

func usersHandler(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("Users API"))
}

func productsHandler(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("Products API"))
}

func main() {
    mux := http.NewServeMux()

    // 创建主路由
    mux.HandleFunc("/home", homeHandler)
    mux.HandleFunc("/about", aboutHandler)

    // 创建API路由分组
    apiGroup := NewRouterGroup("/api")
    apiGroup.Use(loggingMiddleware) // 为整个分组添加中间件

    // 注册特定请求方法的路由
    apiGroup.HandleMethod(http.MethodGet, "/users", http.HandlerFunc(usersHandler))
    apiGroup.HandleMethod(http.MethodPost, "/products", http.HandlerFunc(productsHandler))

    // 注册API路由分组
    mux.Handle("/api/", apiGroup)

    // 启动HTTP服务器
    http.ListenAndServe(":8080", mux)
}
