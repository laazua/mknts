package main
//go get -u github.com/go-sql-driver/mysql
/*
import (
	"time"
	"database/sql"
	_ "github.com/go-sql-driver/mysql"
)

//configure the database connection (always check errors)
db, err := sql.Open("mysql", "username:password@(127.0.0.1:3306)/dbname?parseTime=true")

//initialize the first connection to the database, to see if everything works correctly
//make sure to check the error.
 err := db.Ping()

 //create database table
 query := `
	CREATE TABLE users (
		id INT AUTO_INCREMENT,
		username TEXT NOT NULL,
		password TEXT NOT NULL,
		created_at DATETIME,
		PRIMARY KEY (id)
	);`

 //executes the SQL query in our database. check err to ensure there was no error
 _, err := db.Exec(query)

 //insert some data to table : INSERT INTO users (username, password, created_at) VALUES(?, ?, ?)

 username := "bobo"
 password := "123456"
 createdAt := time.Now()

 result, err := db.Exec(`INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)`, username, password, createdAt)

 userID, err := result.LastInsertId()

 //在GO中我们先要声明一些变量来存储数据,然后像这样查询单条数据:
 var(
 	id int
 	username string
 	password string
 	createdAt time.Time
 )

 query := `SELECT id, username, password, created_at FROM users WHERE id = ?`
 err := db.QueryRow(query, 1).Scan(&id, &username, &password, &createdAt)

 //在整张表中查询数据: SELECT id, username, password, created_at FROM users
 type user struct {
 	id  int
 	username  string
 	password  string
 	createdAt time.Time
 }

 rows, err := db.Query(`SELECT id, username, password, created_at FROM users`)
 defer rows.Close()

 var users []user
 for rows.Next() {
 	var u user
 	err := rows.Scan(&u.id, &u.username, &u.password, &u.createAt)
 	users = append(users, u)
 }
 err := rows.Err()

 //现在users可能包含一下内容
 users {
 	user {
 		id:    1,
 		username:    "bobo",
 		password:    "12346",
 		createdAt:   time.Time{wall:0x0, ext: 63701044325, loc: (*time.Location)(nil)},
    },
    user {
    	id:    2,
    	username:    "lili",
    	password:    "abcdefg",
    	createdAt:   time.Time{wall: 0x0, ext: 63701044622, loc: (*time.Location)(nil)},
    },
}

 //delete some data && check err
 _, err := db.Exec(`DELETE FROM users WHERE id = ?`, 1)

 */

import (
	"database/sql"
	"fmt"
	"log"
	"time"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	db, err := sql.Open("mysql", "root:123456@(127.0.0.1:3306)/test?parseTime=true")
	if err != nil {
		log.Fatal(err)
	}
	if err := db.Ping(); err != nil {
		log.Fatal(err)
	}

	{//create a new table
		query := `
			CREATE TABLE users (
				id INT AUTO_INCREMENT,
				username TEXT NOT NULL,
				password TEXT NOT NULL,
				created_at DATETIME,
				PRIMARY KEY (id)
			);`
		if _, err := db.Exec(query); err != nil {
			log.Fatal(err)
		}
	}

	{//Insert a new user
		username := "johnode"
		password := "secret"
		createdAt := time.Now()

		result, err := db.Exec(`INSERT INTO users (username, password,created_at) VALUES (?,?,?)`,username, password, createdAt)
		if err != nil {
			log.Fatal(err)
		}

		id, err := result.LastInsertId()
		fmt.Println(id)
	}

	{//Query a single user
		var(
			id        int
			username  string
			password  string
			createdAt time.Time
		)

		query := `SELECT id, username, password, created_at FROM users WHERE id = ?`
		if err := db.QueryRow(query, 1).Scan(&id, &username, &password, &createdAt); err != nil {
			log.Fatal(err)
		}
		fmt.Println(id, username, password, createdAt)
	}

	{//Query all uers
		type user struct{
			id        int
			username  string
			password  string
			createdAt time.Time
		}

		rows, err := db.Query(`SELECT id, username, password, created_at FROM users`)
		if err != nil {
			log.Fatal(err)
		}
		defer rows.Close()

		var users []user
		for rows.Next() {
			var u user
			err := rows.Scan(&u.id, &u.username, &u.password, &u.createdAt)
			if err != nil {
				log.Fatal(err)
			}
			users = append(users, u)
		}
		if err := rows.Err(); err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%#v\n", users)
	}

	{//Delete some data
		_, err := db.Exec(`DELETE FROM users WHERE id = ?`, 1)
		if err != nil {
			log.Fatal(err)
		}
	}
}