package main

import (
	"context"
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"log"
	"time"
)

//定义数据库凭据
const (
	username = "root"
	password = "123456"
	host = "127.0.0.1:3306"
	dbname = "test"
)

//返回一个dsn
func dsn(dbName string) string {
	return fmt.Sprintf("%s:%s@tcp(%s)/%s", username, password, host, dbname)
}

func main() {
	//打开并返回数据库连接
	db, err := sql.Open("mysql", dsn(""))
	if err != nil {
		log.Printf("Error %s when open DB\n", err)
		return
	}
	defer db.Close()

	//创建数据库
	ctx, cancelfunc := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancelfunc()
	res, err := db.ExecContext(ctx, "CREATE DATABASE IF NOT EXISTS " + dbname)
	if err != nil {
		log.Printf("Error %s when create DB\n", err)
		return
	}
	no, err := res.RowsAffected()
	if err != nil {
		log.Printf("Error %s when fetching rows", err)
		return
	}
	log.Printf("rows affected %d\n", no)

	db.Close()
	db, err = sql.Open("mysql", dsn(dbname))
	if err != nil {
		log.Printf("Error %s when opening DB", err)
		return
	}
	defer db.Close()

	ctx, cancelfunc = context.WithTimeout(context.Background(), 5*time.Second)
	defer cancelfunc()
	err = db.PingContext(ctx)
	if err != nil {
		log.Printf("Error %s pinging DB", err)
		return
	}
	log.Printf("Connected to DB %s successfully\n", dbname)
}
