package main
//该示例展示如何从特定的目录提取静态文件(css,js, images文件)

import "net/http"

func main() {
	fs := http.FileServer(http.Dir("assets/"))
	http.Handle("/static/", http.StripPrefix("/static", fs))

	http.ListenAndServe(":8080", nil)
}

/*
$ tree assets
assets/
|__ css/
	|__styles.css

$ go run static.go
$ curl -s http://localhost:8080/static/css/styles.css
body {
	backgground-color: black;
}
*/