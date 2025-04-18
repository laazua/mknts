package main

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

var (
	id   int
	name string
)

func main() {
	// db是一个sql.DB类型的对象,该对象线程安全,且内部包含了一个连接池,连接池的选项可以在sql.DB的方法中设置
	db, err := sql.Open("mysql", "user:password@tcp(127.0.0.1:3306)/hello")
	if err != nil {
		return
	}
	defer db.Close()

	rows, err := db.Query("SELECT id, name FROM users WHERE id = ?", 1)
	if err != nil {
		return
	}
	defer rows.Close()

	// 必须要把rows中的内容读完,或者显示调用Close()方法,否则在defer的rows.Close()执行前,连接永远不会释放
	for rows.Next() {
		err := rows.Scan(&id, &name)
		if err != nil {
			return
		}
		fmt.Println(id, name)
	}
	err = rows.Err()
	if err != nil {
		return
	}

}
