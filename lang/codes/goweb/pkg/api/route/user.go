package route

import (
	"fmt"
	"gweb/pkg/utils"
	"html/template"
	"net/http"
)

// type IndexData struct {
// 	Done bool
// }

func Index(w http.ResponseWriter, r *http.Request) {
	r.Header.Set("content type", "application/json")
	r.Header.Set("Access-Control-Allow-Origin", "*")
	r.Header.Set("Access-Control-Allow-Credentials", "true")
	template.Must(template.ParseFiles("templates/login.html"))
	data, err := utils.ParseLoginBodyData(r)
	if err != nil {
		return
	}
	fmt.Println(data)
	// if username == "" || password == "" {
	// 	tmpl.Execute(w, IndexData{Done: false})
	// 	return
	// }
	// tmpl.Execute(w, IndexData{Done: true})
}

func DashBoard(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("templates/dashboard.html"))
	tmpl.Execute(w, "templates/dashboard.html")
}

func Login(w http.ResponseWriter, r *http.Request) {
	if r.Method != "GET" {
		return
	}

}

func AddUser(w http.ResponseWriter, r *http.Request) {

}

func DelUser(w http.ResponseWriter, r *http.Request) {

}

func UptUser(w http.ResponseWriter, r *http.Request) {

}

func GetUser(w http.ResponseWriter, r *http.Request) {

}
