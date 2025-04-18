package main

import (
    "flag"
    "fmt"
    "log"
    "net/http"
    "os"
    "strconv"
    "sync"
)

type apiConfig struct {
    fileserverHits int
    mux            sync.Mutex
}

func (cfg *apiConfig) middlewareMetric(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        cfg.mux.Lock()
        cfg.fileserverHits++
        cfg.mux.Unlock()
        next.ServeHTTP(w, r)
    })
}

func (cfg *apiConfig) handlerMetrics(w http.ResponseWriter, r *http.Request) {
    cfg.mux.Lock()
    hits := cfg.fileserverHits
    cfg.mux.Unlock()
    w.Header().Set("Content-Type", "text/plain")
    w.Write([]byte("fileserver_hits " + strconv.Itoa(hits)))
}

func (cfg *apiConfig) handlerReset(w http.ResponseWriter, r *http.Request) {
    cfg.mux.Lock()
    cfg.fileserverHits = 0
    cfg.mux.Unlock()
    w.Write([]byte("Metrics reset\n"))
}

func handlerReadiness(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("OK"))
}

func handlerSayHello(w http.ResponseWriter, r *http.Request) {
    defer r.Body.Close()
    buffer := make([]byte, 1024)
    r.Body.Read(buffer)
    fmt.Printf("POST: %v\n", string(buffer))
    w.Write([]byte("hello world!\n"))
}

func main() {

    var filepathRoot string
    flag.StringVar(&filepathRoot, "p", ".", "filesystem path")
    flag.Parse()

    if len(os.Args) != 3 {
        fmt.Printf("Usage: %v -h for help.\n", os.Args[0])
	return
    }

    const port = "8081"

    mux := http.NewServeMux()

    cfg := &apiConfig{}

    fileServerHandler := http.StripPrefix("/app", http.FileServer(http.Dir(filepathRoot)))

    mux.Handle("/app/", cfg.middlewareMetric(fileServerHandler))
    mux.HandleFunc("GET /metrics", cfg.handlerMetrics)
    mux.HandleFunc("GET /reset", cfg.handlerReset)
    mux.HandleFunc("GET /healthz", handlerReadiness)
    mux.HandleFunc("POST /demo", handlerSayHello)

    srv := &http.Server{
        Addr:    ":" + port,
        Handler: mux,
    }

    log.Printf("Serving files from %s on port: %s\n", filepathRoot, port)
    log.Fatal(srv.ListenAndServe())
}
