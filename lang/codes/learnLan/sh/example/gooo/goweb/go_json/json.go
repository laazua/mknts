//该示例展示如何使用encoding/jso包对json数据进行编码和解码
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type User struct {
	Firstname    string `json:"firstname"`
	Lastname     string `json:"lastname"`
	Age          int    `json:"age"`
}

func main() {
	http.HandleFunc("/decode", func(w http.ResponseWriter, r *http.Request){
		var user User
		json.NewDecoder(r.Body).Decode(&user)

		fmt.Fprintf(w, "%s %s is %d years old!", user.Firstname, user.Lastname, user.Age)
	})

	http.HandleFunc("/encode", func(w http.ResponseWriter, r *http.Request){
		peter := User{
			Firstname: "John",
			Lastname:  "Done",
			Age:        25,
		}
		json.NewEncoder(w).Encode(peter)
	})

	http.ListenAndServe("0.0.0.0:8888", nil)
}