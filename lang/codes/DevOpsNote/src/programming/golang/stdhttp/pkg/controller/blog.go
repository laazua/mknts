package controller

import (
	"fmt"
	"log/slog"
	"net/http"

	"stdhttp/pkg/middleware"
	"stdhttp/pkg/router"
)

type Blog struct {
	Logger *slog.Logger
}

// 实现Controller接口
func (b *Blog) Name() string {
	return "blog"
}

func (b *Blog) InitRoute(router *router.Router) {
	b.Logger.Info(fmt.Sprintf("URI: %v", router.Prefix))
	router.Use(middleware.AuthMw)
	router.Handle(http.MethodPost, router.Prefix+"/create", http.HandlerFunc(b.create))
	router.Handle(http.MethodDelete, router.Prefix+"/delete", http.HandlerFunc(b.delete))
	router.Handle(http.MethodPut, router.Prefix+"/update", http.HandlerFunc(b.update))
	router.Handle(http.MethodGet, router.Prefix+"/query", http.HandlerFunc(b.query))
}

func (b *Blog) create(w http.ResponseWriter, r *http.Request) {
	b.Logger.Info("create endpoint hit")
	success(w, object{"code": 200, "message": "blog create api"})
}

func (b *Blog) delete(w http.ResponseWriter, r *http.Request) {
	b.Logger.Info("delete endpoint hit")
	failure(w, object{"code": 400, "message": "blog delete api"})
}

func (b *Blog) update(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "update api")
}

func (b *Blog) query(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "query api")
}
