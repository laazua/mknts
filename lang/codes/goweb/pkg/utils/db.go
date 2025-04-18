package utils

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

var Db *sql.DB

func LoadMysql() {
	dbUrl := fmt.Sprintf("%s:%s@(%s:%d)/%s?parseTime=true",
		AppCon.Mysql.Username, AppCon.Mysql.Password,
		AppCon.Mysql.Host, AppCon.Mysql.Port, AppCon.Mysql.Dbname)
	if db, err := sql.Open("mysql", dbUrl); err != nil {
		panic(err)
	} else {
		if err := db.Ping(); err != nil {
			panic(err)
		}
		Db = db
		// 建表
		createTb(db)
	}
}

func createTb(db *sql.DB) error {
	createZoneTb := `
	CREATE TABLE IF NOT EXISTS zone (
	  Id INT AUTO_INCREMENT,
	  ZoneName VARCHAR(64),
	  ZoneId INT,
	  ZoneIp VARCHAR(64),
	  IsCombine TINYINT,
	  PRIMARY  KEY (id)
	) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
	`
	createUserTb := `
	CREATE TABLE IF NOT EXISTS user (
		Id INT AUTO_INCREMENT, 
		UserName VARCHAR(64), 
		PassWord VARCHAR(64), 
		PRIMARY  KEY (id)	
	) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
	`
	if _, err := db.Exec(createUserTb); err != nil {
		return err
	}
	if _, err := db.Exec(createZoneTb); err != nil {
		return err
	}
	return nil
}
