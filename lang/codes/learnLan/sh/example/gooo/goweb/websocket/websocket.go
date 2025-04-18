//该示例展示如何在go中使用websocket.
//创建一个简单的服务器,该服务器回显发送给他的所有内容
//go get github.com/gorilla/websocket
package main

import (
	"fmt"
	"net/http"
	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
	ReadBufferSize:    1024,
	WriteBufferSize:   1024,
}

func main() {
	http.HandleFunc("/echo", func(w http.ResponseWriter, r *http.Request) {
		conn, _ := upgrader.Upgrade(w, r, nil)    //error ignored for sake of simplicity

		for {
			//read message from browser
			msgType, msg, err := conn.ReadMessage()
			if err != nil {
				return
			}
			//print the message to the console
			fmt.Printf("%s sent: %s\n", conn.RemoteAddr(), string(msg))
			//write message back to browser
			if err = conn.WriteMessage(msgType, msg); err != nil {
				return
			}
		}
	})

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request){
		http.ServeFile(w, r, "websocket.html")
	})
	http.ListenAndServe("0.0.0.0:8888", nil)
}