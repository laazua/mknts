package main

import (
	"bytes"
	"errors"
	"fmt"
	"html/template"
	"log/slog"
	"os"
	"os/exec"
	"strings"
	"time"
)

// 在 fmt.Sprintf 中，% 被视为格式化操作符
// 需要用两个连续的 % 来表示一个字面量的 % 符号
const confTpl string = `[program:{{.Name}}]
##执行命令
directory=%v
command={{.Command}}

##参数
user=root
process_name=%%(process_num)02d
numprocs={{.Number}}
autostart=true
autorestart=true
startretries=3
startsecs=10
exitcodes=0
stopsignal=KILL
stopwaitsecs=10
redirect_stderr=true

##设置log路径
stdout_logfile=/var/log/supervisor/{{.Name}}.log
stdout_logfile_maxbytes=50MB
stdout_logfile_backups=3
stderr_logfile=/dev/null
stderr_logfile_maxbytes=0
stderr_logfile_backups=0
[supervisord]
[supervisorctl]
`

type Dp struct{}

func (dp *Dp) Create(p Process) (string, error) {

	if err := dp.genIni(p); err != nil {
		return "", err
	}
	_, err := dp.run()
	if err != nil {
		logger.Error(err.Error())
		return "", err
	}
	cmdName := fmt.Sprintf("supervisorctl status %v:", p.Name)
	var output string
	for {
		output, err := runCmd(cmdName)
		if err != nil {
			return "", err
		}
		if strings.Contains(output, "FATAL") {
			return "", errors.New("创建队列失败")
		}
		if strings.Contains(output, "RUNNING") {
			break
		}
		time.Sleep(100 * time.Microsecond)
	}
	logger.Info("执行命令", slog.String("command", p.Command))
	logger.Info("命令输出", slog.String("cmdOut", output))
	return output, nil
}

// 根据模板生成进程ini配置
func (dp *Dp) genIni(p Process) error {
	confTPL := fmt.Sprintf(confTpl, GetOsEnv("cmdexpath"))
	tmpl, err := template.New("supervisord").Parse(confTPL)
	if err != nil {
		return errors.New("创建模板失败")
	}
	var buffer bytes.Buffer
	err = tmpl.Execute(&buffer, p)
	if err != nil {
		return errors.New("解析模板失败")
	}
	// fmt.Println(buffer.String())
	dpFileName := fmt.Sprintf("%v/%v.ini", GetOsEnv("spath"), p.Name)
	if yes := fileExist(dpFileName); yes {
		return errors.New("队列配置文件已经存在")
	}
	fd, err := os.OpenFile(dpFileName, os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		logger.Error(err.Error())
		return errors.New("创建supervisor 配置文件失败")
	}
	defer fd.Close()
	_, err = fd.WriteString(buffer.String())
	if err != nil {
		return errors.New("写入supervisor 配置文件失败")
	}
	return nil
}

func (dp *Dp) run() (string, error) {
	cmdName := "supervisorctl update"
	return runCmd(cmdName)
}

func (dp *Dp) Delete(name string) error {
	dpName := fmt.Sprintf("%v/%v.ini", GetOsEnv("spath"), name)
	if yes := fileExist(dpName); !yes {
		return errors.New("队列配置文件不存在")
	}

	cmdName := fmt.Sprintf("mv %v %v && supervisorctl update", dpName, GetOsEnv("sbpath"))
	output, err := runCmd(cmdName)
	if err != nil {
		return err
	}
	logger.Info("执行命令", slog.String("command", cmdName))
	logger.Info("命令输出", slog.String("cmdOut", output))
	return nil
}

func runCmd(command string) (string, error) {
	cmd := exec.Command("bash", "-c", command)
	output, err := cmd.CombinedOutput()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func fileExist(name string) bool {
	_, err := os.Stat(name)
	return err == nil
}
