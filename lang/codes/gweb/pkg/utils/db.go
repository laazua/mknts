package utils

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

var Db *sql.DB

func LoadSql() {
	dbUrl := fmt.Sprintf("%s:%s@(%s:%d)/%s?parseTime=true",
		Setting.Mysql.Username, Setting.Mysql.Password, Setting.Mysql.Host,
		Setting.Mysql.Port, Setting.Mysql.Dbname)
	if db, err := sql.Open("mysql", dbUrl); err != nil {
		panic(err)
	} else {
		if err := db.Ping(); err != nil {
			panic(err)
		}
		Db = db
		createTb(db)
	}
}

func createTb(db *sql.DB) error {
	ZoneTb := `
	CREATE TABLE IF NOT EXISTS zone (
		Id INT AUTO_INCREMENT,
		ZoneName VARCHAR(64),
		ZoneId INT,
		ZoneIp VARCHAR(64),
		IsCombine TINYINT,
		PRIMARY  KEY (id)
	  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
	`
	UserTb := `
	CREATE TABLE IF NOT EXISTS user (
		Id INT AUTO_INCREMENT, 
		UserName VARCHAR(64), 
		PassWord VARCHAR(64), 
		PRIMARY  KEY (id)	
	) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
	`
	if _, err := db.Exec(UserTb); err != nil {
		return err
	}
	if _, err := db.Exec(ZoneTb); err != nil {
		return err
	}
	return nil
}
