// 监控主机资源
package main

import (
	"log/slog"
	"net/http"
	"runtime"
	"strings"
	"time"

	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/load"
	"github.com/shirou/gopsutil/mem"
)

func isCpuOk() bool {
	//系统的平均CPU使用率
	cpu, err := cpu.Percent(time.Second, false)
	if err != nil {
		logger.Error("获取cpu使用情况错误", slog.String("error", err.Error()))
		return false
	}
	logger.Info("当前系统平均cpu使用率", slog.Float64("usage", cpu[0]))
	return cpu[0] <= StoFloat(GetOsEnv("cpu"))
}

func isMemOk() bool {
	mem, err := mem.VirtualMemory()
	if err != nil {
		logger.Error("获取内存使用情况报错", slog.String("error", err.Error()))
		return false
	}
	realUsage := float64(mem.Total-mem.Available) / float64(mem.Total) * 100
	logger.Info("当前系统真实内存使用率", slog.Float64("RealUsage", realUsage))
	if realUsage > StoFloat(GetOsEnv("mem")) {
		return false
	}
	logger.Info("当前系统虚拟内存使用率", slog.Float64("VirUsage", mem.UsedPercent))
	return mem.UsedPercent <= StoFloat(GetOsEnv("mem"))
}

func isLoadOk() bool {
	// 获取平均负载（1/5/15分钟）
	loadStat, err := load.Avg()
	if err != nil {
		logger.Error("获取负载失败", slog.String("error", err.Error()))
		return false
	}

	// 获取 CPU 核心数
	cpuCount := runtime.NumCPU()
	// 设定判断规则（根据实际场景调整）
	threshold := float64(cpuCount)

	// 获取当前一分钟平均负载
	load1 := loadStat.Load1
	switch {
	case load1 <= threshold:
		logger.Info("系统负载正常", slog.Float64("load1", loadStat.Load1), slog.Float64("load5", loadStat.Load5), slog.Float64("load15", loadStat.Load15))
		return true
	case load1 <= threshold*1.5:
		logger.Info("系统轻度过载", slog.Float64("load1", loadStat.Load1), slog.Float64("load5", loadStat.Load5), slog.Float64("load15", loadStat.Load15))
		return true
	case load1 <= threshold*2:
		logger.Error("系统中度过载", slog.Float64("load1", loadStat.Load1), slog.Float64("load5", loadStat.Load5), slog.Float64("load15", loadStat.Load15))
		return true
	default:
		logger.Error("系统严重过载", slog.Float64("load1", loadStat.Load1), slog.Float64("load5", loadStat.Load5), slog.Float64("load15", loadStat.Load15))
		return false
	}

}

func IsOsResourceOk() bool {
	if isCpuOk() && isMemOk() && isLoadOk() {
		return true
	}
	return false
}

func IpWhiteList(r *http.Request) bool {
	ip := strings.Split(r.RemoteAddr, ":")[0]
	logger.Info("来访IP地址", slog.String("IP", ip))
	if strings.Contains(GetOsEnv("whiteip"), "all") {
		return true
	}
	return strings.Contains(GetOsEnv("whiteip"), ip)
}
