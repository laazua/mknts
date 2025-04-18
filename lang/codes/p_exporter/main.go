package main

import (
	"flag"
	"fmt"
	"net/http"
	"p_exporter/collector"
	"p_exporter/common"

	"github.com/go-kit/log/level"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"github.com/prometheus/common/version"
)

var (
	address     = flag.String("address", ":9110", "The listening address of the service.")
	metricsPath = flag.String("metricsPath", "/metrics", "The data export path of the p_exporter program.")
	configFile  = flag.String("configFile", "./p_exporter.yaml", "The configuration file of the p_exporter program.")
)

func main() {

	flag.Parse()

	// 注册指标
	registerCollector(*metricsPath, *configFile)
	// 创建HTTP服务器实例
	server := http.Server{Addr: *address}
	level.Info(common.Logger).Log("MSG", "Start p_exporter", "version", version.Info())
	if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
		panic(err)
	}
}

// 获取被监听的进程信息
func getProcess(fileName string) map[string]string {
	v := common.LoadConfig(fileName)
	processes, ok := v.Get("programs").([]interface{})
	if !ok {
		return nil
	}
	programs := make(map[string]string)
	for _, process := range processes {
		program := process.(map[string]interface{})
		name := program["name"].(string)
		pidFile := program["path"].(string) + "/pid.txt"
		select {
		case cpidFile := <-collector.PidStatus:
			if cpidFile == pidFile {
				level.Error(common.Logger).Log("ERR", "Pid file stop: ", pidFile)
				continue
			}
		default:
			programs[name] = pidFile
		}
	}
	return programs
}

// 向promethues注册指标
func registerCollector(metricsPath, fileName string) {
	register := prometheus.NewRegistry()
	processes := getProcess((fileName))
	if processes == nil {
		panic("can't get config of process")
	}
	for name, pidFile := range processes {
		level.Info(common.Logger).Log("MSG", fmt.Sprintf("Regist %v...", name))
		pCollector := collector.NewProcessCollector(pidFile, name)
		register.Register(pCollector)
	}
	http.Handle(metricsPath, promhttp.HandlerFor(register, promhttp.HandlerOpts{Registry: register}))
}
