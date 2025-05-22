package api

import "net/http"

type Api interface {
	RegApi(mux *http.ServeMux)
}
