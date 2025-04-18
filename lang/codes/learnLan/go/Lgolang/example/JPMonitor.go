//这是个监控主机负载及单进程cpu使用情况的工具
package main

import (
    "flag"
    "fmt"
    "net/http"
    "strings"
    "time"

    "github.com/shirou/gopsutil/load"
    "github.com/shirou/gopsutil/process"
)

var (
    user *string = flag.String("u", "java", "process user")
    cpu *float64 = flag.Float64("d", 300, "process cpu flag")
    ld *float64 = flag.Float64("l", 150, "host load")
    ip *string = flag.String("i", "127.0.0.1", "host address")
    webHook = `https://oapi.dingtalk.com/robot/send?`
)

func main() {
    flag.Parse()
    //if user != nil {
    //    fmt.Println("user =", *user)
    //}
    for {
        GetProcess(*user, *cpu, *ip)
        time.Sleep(time.Second * 60)
        getLoad(*ld, *ip)
    }
}

//获取单进程cpu使用情况
func GetProcess(user string, c float64, ip string) {
    //PInfo := make([]int32, 2, 4)
    ps, _ := process.Processes()

    for _, p := range ps {
        //fmt.Println(p.Name())
        username, _ := p.Name()
        cpu, _ := p.CPUPercent()

        if username == user && float64(cpu) > c {
            info := fmt.Sprintf("异常PID: %d -> %.2f", p.Pid, cpu)

            sendMsg(time.Now().Format("2006-01-02 15:04:05"), "GameName=yyzb && IP: ", ip, info)
            fmt.Println(time.Now().Format("2006-01-02 15:04:05"), "GameName=yyzb && IP: ", ip, info)
        }
    }
    //fmt.Println(PInfo)
}

//获取机器15分钟负载
func getLoad(ld float64, ip string) {
    Load, _ := load.Avg()
    if Load.Load15 > ld {
        sendMsg(time.Now().Format("2006/01/02 15:04:05"), "GameName=yyzb && IP: ", ip, "当前负载:", Load.Load15)
        fmt.Println(time.Now().Format("2006/01/02 15:04:05"), "当前负载: ", Load.Load15)
    }
}

//发送报警信息
func sendMsg(msg ...interface{}) {
    //interface transfer strings
    m := fmt.Sprintf("%v", msg)
    content := `{"msgtype": "text","text": {"content": "` + m + `"}}`

    //create request
    req, err := http.NewRequest("POST", webHook, strings.NewReader(content))
    if err != nil {
        fmt.Println("create req failed,", err)
    }

    client := &http.Client{}
    req.Header.Set("Content-type", "application/json; charset=utf-8")

    //send req
    resp, err := client.Do(req)
    defer resp.Body.Close()

    if err != nil {
        fmt.Println("send msg failed", err)
    }
}
