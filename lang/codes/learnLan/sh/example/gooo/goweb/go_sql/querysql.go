package main

import (
	"database/sql"
	"fmt"
	"log"
	"flag"

	_ "github.com/go-sql-driver/mysql"
)

var (
	serverId    int
	userName    string
	gameAgent   string
	gameAlias   string
	help        bool
	mdataSourceName string
)

//用于保存从mds_server查询出来的信息
type UserInfo struct {
	dbIp        string    `json:"dbIp"`
	dbPort      int       `json:"dbPort"`
	gameDBName  string    `json:"gameDBName"`
}

//player
type Player struct {
	AccountID        int64      `json:"AccountID"`
	PlayerID         int64      `json:"PlayerID"`
	PlayerName       string     `json:"PlayerName"`
	ServerID		 int64		`json:"ServerID"`
	VipLevel         int64		`json:"VipLevel"`
	PlayerLevel      int64		`json:"PlayerLevel"`
	Exp              int64		`json:"Exp"`
	Charge           int64		`json:"Charge"`
	Health           int64      `json:"Health"`
	Gold             int64      `json:"Gold"`
	Spirit           int64      `json:"Spirit"`
	Soul             int64      `json:"Soul"`
	Star             int64      `json:"Star"`
	Rank             int64		`json:"Rank"`
	Butterfly		 int64      `json:"Butterfly"`
	LogoffTime       string     `json:"LogoffTime"`
}

//account
type Account struct {
	AccountID        int64		`json:"AccountID"`
	AccountName      string     `json:"AccountName"`
	AccountPassword  string     `json:"AccountPassword"`
	CreateTime       int64		`json:"CreateTime"`
	LastLoginTime    int64		`json:"LastLoginTime"`
	ServerID         int64		`json:"ServerID"`
	Status           int64		`json:"Status"`
	Channel          string		`json:"Channel"`
	deviceId         string     `json:"deviceId"`
	channelAccount   string     `json:"channelAccount"`
}

//初始化函数
func init(){
	//获取参数  serverid, username, gameagent
	flag.BoolVar(&help, "h", false, "help messge.")
	flag.IntVar(&serverId,"i",0,"show game zone.")
	flag.StringVar(&userName, "u", "", "username.")
	flag.StringVar(&gameAgent, "a", "", "gameName.")
	flag.StringVar(&gameAlias, "g", "", "gameAlias: [ss|lhsl]")
}

//从mds_server表中查询信息
func queryMds(agent string, serverid int) map[string]interface{}{
	var userinfo UserInfo
	db, err := sql.Open("mysql", mdataSourceName)
	defer db.Close()
	if err != nil {
		log.Println("打开mds_server表失败.")
		return nil
	}
	err = db.QueryRow("SELECT serverIP, dbPort, gameDBName FROM mds_server where serverId = ? and platformAlias = ?", serverid, agent).Scan(&userinfo.dbIp, &userinfo.dbPort, &userinfo.gameDBName)
	if err != nil {
		fmt.Println("查询mds_server失败", err.Error())
		return nil
	}

	mdsInfo := map[string]interface{}{
		"dbip": userinfo.dbIp,
		"dbport": userinfo.dbPort,
		"gamedbname": userinfo.gameDBName,
	}
	return mdsInfo
}

func quryGame(gameagent string, serverId int, playerName string) {
	resoult := queryMds(gameagent, serverId)
	fmt.Println(resoult)
	gdataSourceName := fmt.Sprintf("username:password(%s:%d)/%s", resoult["dbip"], resoult["dbport"], resoult["gamedbname"])
	fmt.Println(gdataSourceName)
	db, err := sql.Open("mysql", gdataSourceName)
	if err != nil {
		fmt.Println("open gamedb err.", err)
		return
	}
	var player Player
	err = db.QueryRow("SELECT AccountID,PlayerID,PlayerName,ServerID,VipLevel,PlayerLevel,Exp,Charge,Health,Gold,Spirit,Soul,Star,Rank,Butterfly,LogoffTime FROM player where PlayerName = ?", playerName).
		Scan(&player.AccountID,&player.PlayerID,&player.PlayerName,&player.ServerID,&player.VipLevel,&player.PlayerLevel,&player.Exp,&player.Charge,&player.Health,&player.Gold,&player.Spirit,
		&player.Soul,&player.Star,&player.Rank,&player.Butterfly,&player.LogoffTime)
	if err != nil {
		fmt.Println("query player table failed.", err)
		return
	}
	playerInfo := map[string]interface{}{
		"AccountID": player.AccountID,
		"PlayerID": player.PlayerID,
		"PlayerName": player.PlayerName,
		"ServerID": player.ServerID,
		"VipLevel": player.VipLevel,
		"PlayerLevel": player.PlayerLevel,
		"Exp": player.Exp,
		"Charge": player.Charge,
		"Health": player.Health,
		"Gold": player.Gold,
		"Spirit": player.Spirit,
		"Soul": player.Soul,
		"Star": player.Star,
		"Rank": player.Rank,
		"Butterfly": player.Butterfly,
		"LogoffTime": player.LogoffTime,
	}

	var account Account
	err = db.QueryRow("SELECT AccountID,AccountName,AccountPassword,CreateTime,LastLoginTime,ServerID,Status,Channel,deviceId,channelAccount FROM account where AccountName = ?", playerName).
		Scan(&account.AccountID,&account.AccountName,&account.AccountPassword,&account.CreateTime,&account.LastLoginTime,&account.ServerID,&account.Status,&account.Channel,&account.deviceId,
		&account.channelAccount)
	if err != nil {
		fmt.Println("query account table failed.", err)
		return
	}
	accountInfo := map[string]interface{}{
		"AccountID": account.AccountID,
		"AccountName": account.AccountName,
		"AccountPassword": account.AccountPassword,
		"CreateTime": account.CreateTime,
		"LastLoginTime": account.LastLoginTime,
		"ServerID": account.ServerID,
		"Status": account.Status,
		"Channel": account.Channel,
		"deviceId": account.deviceId,
		"channelAccount": account.channelAccount,
	}
	fmt.Println("player table:")
	fmt.Println(playerInfo)
	fmt.Println("account table:")
	fmt.Println(accountInfo)
}

func main() {
	flag.Parse()
	if help {
		flag.Usage()
		return
	}
	if userName == "" || serverId == 0 || gameAgent == "" || gameAlias == "" {
		fmt.Println("please input argument like this:" + "\n" +
			"    ./querysql -a releasetencent -i 10 -u 张三 -g [ss|lhsl]")
		return
	}
	if gameAlias == "ss" {
		mdataSourceName = "username:password@tcp(ip:port)/dbName"
	} else if gameAlias == "lhsl" {
		mdataSourceName = "username:password@tcp(ip:port)/dbName"
	}else {
		fmt.Println("please input right gameAlias.")
		return
	}

	quryGame(gameAgent, serverId, userName)
	resoult := queryMds(gameAgent, serverId)
	fmt.Println(resoult)
}
