package store

import (
	"database/sql"
	"log/slog"
	"os"

	"gkins/env"

	_ "github.com/go-sql-driver/mysql"
)

var DB *sql.DB

func init() {
	env.Load(".env")
	slog.Info("Load .env success")
	db, err := sql.Open("mysql", os.Getenv("db.uri"))
	if err != nil {
		slog.Error(err.Error())
		panic(err)
	}
	db.SetConnMaxLifetime(env.ParseTDuration(os.Getenv("db.con.max.lifetime")))
	db.SetMaxOpenConns(env.StoInt(os.Getenv("db.con.max.open")))
	db.SetMaxIdleConns(env.StoInt(os.Getenv("db.con.max.idle")))

	// 检查数据库连接是否正常
	if err := db.Ping(); err != nil {
		panic(err)
	}
	slog.Info("Mysql Init success")
	DB = db
}
