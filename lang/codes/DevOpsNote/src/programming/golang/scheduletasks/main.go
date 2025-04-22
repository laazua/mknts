package main

import (
	"fmt"
	"net/http"

	"scheduletasks/api"

	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Println("start on: ", 8889)
	router := gin.Default()

	router.GET("/task", api.GetTask)
	router.POST("/task", api.AddTask)
	router.DELETE("/task", api.DelTask)

	server := http.Server{
		Handler: router,
		Addr:    ":8889",
	}

	if err := server.ListenAndServe(); err != nil {
		panic(err)
	}
}
