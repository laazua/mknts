//该示例将展示如何使用go中流行的gorilla/sessions包将数据存储在session cookies中
//cookies是存储在用户浏览器中的一小部分数据,并根据每个请求发送到服务器.我们可以在服务器系统中存储用户的登陆记录
//来判断是谁在发送请求.
//在此示例中,仅仅允许经过身份验证的用户在/secret页面上查看秘密消息
package main

import (
	"fmt"
	"github.com/gorilla/sessions"
	"net/http"
)

var(
	//key must be 16, 24, or 32 bytes long (AES-128,AES-192 OR AES-256)
	key = []byte("super-secret-key")
	store = sessions.NewCookieStore(key)
)

func secret(w http.ResponseWriter, r *http.Request) {
	session, _ := store.Get(r, "cookie-name")
	//check if user is authenticated
	if auth, ok := session.Values["authenticated"].(bool); !ok || !auth {
		http.Error(w, "Forbidden", http.StatusForbidden)
		return
	}
	//print secret message
	fmt.Fprintln(w, "the cake is a lie!")
}

func login(w http.ResponseWriter, r *http.Request) {
	session, _ := store.Get(r, "cookie-name")
	//authentication goes here
	//...

	//set user as authenticated
	session.Values["authenticated"] = true
	session.Save(r, w)
}

func logout(w http.ResponseWriter, r *http.Request) {
	session, _ := store.Get(r, "cookie-name")
	//revoke users authentication
	session.Values["authenticated"] = false
	session.Save(r, w)
}

func main() {
	http.HandleFunc("/secret", secret)
	http.HandleFunc("/login", login)
	http.HandleFunc("/logout", logout)

	http.ListenAndServe("0.0.0.0:8888",nil)
}

//go run sessions.go
//curl -s http://localhost:8888/secret
//Forbidden

//curl -s -I http://localhsot:8888/login
//set-cookie: cookie-name=.....
//curl -s --cookie "cookie-name=dkjf;alkjdf;" http://localhost:8888/secret
