package main

import (
	"os/user"
	"fmt"
	"os"
	"strconv"
	_ "github.com/go-sql-driver/mysql"
	"github.com/jmoiron/sqlx"
)

var (
	id, ag, plat string
	db           *sqlx.DB
	game		 []Game
)

type Game struct {
	ServerIp   string `db:"serverIp"`
	DbPort     int    `db:"dbPort"`
	GameDBName string `db:"gameDBName"`
}

func main() {
	if len(os.Args[1:]) != 6 {
		fmt.Println("usage: ./test -i 1 -a iosbreak -g ssjx")
		fmt.Println("-h	help message.")
		fmt.Println("-z	zone")
		fmt.Println("-a	agent")
		fmt.Println("-g	ss|lhsl")
		os.Exit(1)
	}

	for i, arg := range os.Args[1:] {
		if arg == "-z" {
			id = os.Args[i+2]
		} else if arg == "-a" {
			ag = os.Args[i+2]
		} else if arg == "-g" {
			plat = os.Args[i+2]
		}
	}
	game := query(id, ag, plat)
	dumpSql(id, game)
}

func query(id, ag, plat string) (game []Game) {
	url_test := "root:123456@tcp(127.0.0.1:3306)/test"
	zone, _ := strconv.Atoi(id)
	
	if plat == "ss" {
		dbb, err := sqlx.Open("mysql", url_test)
		if err != nil {
			fmt.Println("open mds database err,", err)
			return
		}
		db = dbb
		defer db.Close()

		e := db.Select(&game, "select serverIp,dbPort,gameDBName from mds_server where id=?", zone)
		if e != nil {
			fmt.Println("select info err,", e)
		}
	}
	return game
}

func dumpSql(id string, game []Game) {
	serverIp := game[0].ServerIp
	gameDBName := game[0].GameDBName
	dbPort := game[0].DbPort
	idd, _ := strconv.Atoi(id)
	username := "root"
	password := "123456"
	url := username+":"+password+"@tcp"+"("+serverIp+":"+dbPort+")/"+gameDBName

}
