package controller

import (
	"log/slog"
	"net/http"

	"msite/pkg/router"
)

type Blog struct {
	Logger *slog.Logger
}

// 实现Controller接口
func (b *Blog) Name() string {
	return "blog"
}

func (b *Blog) InitRoute(router *router.Router) {
	blog := router.Group("/blog")
	// blog.Use(middleware.Auth)
	blog.Handle(http.MethodPost, "/create", http.HandlerFunc(b.create))
	blog.Handle(http.MethodDelete, "/delete", http.HandlerFunc(b.delete))
	blog.Handle(http.MethodPut, "/update", http.HandlerFunc(b.update))
	blog.Handle(http.MethodGet, "/query", http.HandlerFunc(b.query))
	blog.Handle(http.MethodGet, "/query/{id}", http.HandlerFunc(b.queryId))
}

func (b *Blog) create(w http.ResponseWriter, r *http.Request) {
	b.Logger.Info("create endpoint hit")
	success(w, object{"code": http.StatusOK, "message": "blog create api"})
}

func (b *Blog) delete(w http.ResponseWriter, r *http.Request) {
	b.Logger.Info("delete endpoint hit")
	failure(w, object{"code": http.StatusOK, "message": "blog delete api"})
}

func (b *Blog) update(w http.ResponseWriter, r *http.Request) {
	// fmt.Fprintf(w, "update api")
	success(w, object{"code": http.StatusOK, "message": "blog update api"})
}

func (b *Blog) query(w http.ResponseWriter, r *http.Request) {
	// fmt.Fprintf(w, "query api")
	success(w, object{"code": http.StatusOK, "message": "blog query api"})
}

func (b *Blog) queryId(w http.ResponseWriter, r *http.Request) {
	id := router.Param(r, "id")
	// fmt.Fprintf(w, "ID: "+id)
	success(w, object{"code": http.StatusOK, "message": "blog queryId api: " + id})
}
