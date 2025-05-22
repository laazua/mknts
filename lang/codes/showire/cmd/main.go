package main

import (
	"log/slog"
	"show/mwire"
)

func main() {
	app := mwire.InitializeServer()
	address := ":8030"
	slog.Info("app run", slog.String("address", address))
	app.Start(address)
}
