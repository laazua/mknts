package main

import (
	"crypto/md5"
	"encoding/hex"
	"flag"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"strconv"
	"time"
	//"net/http"
)

var (
	sign        string = "xtLO15ded1@#J645R"
	dataurl     string = "http://47.95.196.255/MDS/interface/OperationQuery?"

	serverId    int64
	userName    string
	gameAgent   string
	gameAlias   string
	help        bool
)

func queryYWData(gameAlias string, agent string, serverId int64) {
	//postDict := make(map[string]interface{})
	localTime := time.Now().Unix()
	m := md5.New()
	m.Write([]byte(sign + string(localTime)))
	securSign := m.Sum(nil)
	securSigns := hex.EncodeToString(securSign)
	postDict := url.Values{}
	postDict.Set("gameAlias", gameAlias)
	postDict.Set("fields", "dbIp,dbPort,gameDBName")
	postDict.Set("platformAlias", agent)
	postDict.Set("sign", securSigns)
	postDict.Set("time", strconv.FormatInt(localTime, 10))
	postDict.Set("serverId", strconv.FormatInt(serverId, 10))

	//fmt.Println(postDict.Encode())
	//fmt.Printf("%T, %T\n", dataurl, postDict.Encode())
	url, err := url.ParseRequestURI()
	if err != nil {
		fmt.Println("url encode err", err)
		return
	}

	//query := u.Query()
	fmt.Println(url)

	client := &http.Client{Timeout:5 * time.Second}
	resp, err := client.Get(url.String())
	if err != nil {
		fmt.Println("Get data err.", err)
		return
	}
	defer resp.Body.Close()

	resoult, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("获取Body失败", err)
		return
	}
	fmt.Println(string(resoult))
}

func init() {
	//获取参数  serverid, username, gameagent
	flag.BoolVar(&help, "h", false, "help messge.")
	flag.Int64Var(&serverId,"i",0,"game serverId.")
	flag.StringVar(&userName, "u", "", "userName.")
	flag.StringVar(&gameAgent, "a", "", "gameAgent: [releasetencent | releaseandroid].")
	flag.StringVar(&gameAlias, "g", "","gamePlat: [ss | lhsl].")
}

func main() {
	flag.Parse()
	if help {
		flag.Usage()
		return
	}
	if serverId == 0 || userName == "" || gameAgent == "" || gameAlias == ""{
		fmt.Println("Usage: ./GetData -a releasetencent -i 10 -u 张三 -g ss")
		return
	}

	queryYWData(gameAlias, gameAgent, serverId)
	//fmt.Println(serverId, userName, gameAgent, gameAlias)
	//fmt.Println(time.Now().Unix())
}
