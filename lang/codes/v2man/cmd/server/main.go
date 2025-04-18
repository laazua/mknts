package main

import (
	"log"
	"net/http"
	"time"

	"v2man/pkg/config"
	"v2man/pkg/router"
	"v2man/pkg/v2ray"
	"v2man/storage"
)

func main() {
	// Load config
	cfg, err := config.LoadConfig("config.yaml")
	if err != nil {
		log.Fatalf("could not load config: %v", err)
	}

	// Load database
	DbHandler := storage.NewDbHandler(cfg)
	if DbHandler == nil {
		log.Fatal("Can't conn DB")
		return
	}
	defer DbHandler.Close()

	server := http.Server{
		Addr:    cfg.Address,
		Handler: router.NewRouter(cfg, DbHandler),
	}

	if v2 := v2ray.NewUserTraffic(cfg, DbHandler); v2 != nil {
		timer := v2ray.NewTimer(60*time.Second, v2.UpdateUserTraffic)
		timer.Start()
		defer timer.Stop()
	}

	log.Printf("V2man server start on: [%v]\n", cfg.Address)
	if err := server.ListenAndServe(); err != nil {
		log.Fatalf("Server start with error: %v", err)
	}
}
