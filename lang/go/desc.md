<!-- Golang相关的目录结构 -->
### Golang
---

- [go代码指南](https://dave.cheney.net/practical-go/presentations/qcon-china.html)
- [Go指南](https://tour.go-zh.org/list)
- [Go语言编程](https://go-zh.org/)
- [gitbook](https://evanli.github.io/programming-book-2/Go/)
- [cookbook](https://go-cookbook.com/)

* **socket**

- [服务器](code/tcp_server.go)
- [客户端](code/tcp_client.go)

* **编译优化**
```
GOOS=linux GOARCH=amd64 go build -ldflags="-w -s"
```
