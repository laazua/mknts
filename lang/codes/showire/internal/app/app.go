package app

import (
	"net/http"

	"show/internal/api"
)

type HTTPServer struct {
	mux *http.ServeMux
}

func NewHTTPServer(apis []api.Api) *HTTPServer {
	mux := http.NewServeMux()
	for _, api := range apis {
		api.RegApi(mux)
	}
	return &HTTPServer{mux: mux}
}

func (s *HTTPServer) Start(addr string) error {
	return http.ListenAndServe(addr, s.mux)
}
