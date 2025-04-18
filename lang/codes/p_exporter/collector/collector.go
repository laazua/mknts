package collector

import (
	"fmt"
	"p_exporter/common"
	"sync"

	"github.com/go-kit/log/level"
	"github.com/prometheus/client_golang/prometheus"
)

type ProcessCollector struct {
	pidFile       string
	Name          string
	mutex         sync.Mutex
	cpuTotalUsage *prometheus.Desc
	memTotalUsage *prometheus.Desc
	diskRead      *prometheus.Desc
	diskWrite     *prometheus.Desc
	netConnectNum *prometheus.Desc
	fileDescNum   *prometheus.Desc
	threadsNum    *prometheus.Desc
}

func NewProcessCollector(pidFile, name string) *ProcessCollector {
	return &ProcessCollector{
		pidFile: pidFile,
		Name:    name,
		cpuTotalUsage: prometheus.NewDesc(
			name+"_cpu_total_usage",
			name+" cpu total usage",
			[]string{name + "_process"},
			prometheus.Labels{"process": "cpu total usage"},
		),
		memTotalUsage: prometheus.NewDesc(
			name+"_mem_total_usage",
			name+" mem total usage",
			[]string{name + "_process"},
			prometheus.Labels{"process": "memory total usage"},
		),
		diskRead: prometheus.NewDesc(
			name+"_disk_io_read",
			name+" disk io read",
			[]string{name + "_process"},
			prometheus.Labels{"process": "disk io read"},
		),
		diskWrite: prometheus.NewDesc(
			name+"_disk_io_write",
			name+" disk io write",
			[]string{name + "_process"},
			prometheus.Labels{"process": "disk io wirte"},
		),
		netConnectNum: prometheus.NewDesc(
			name+"_net_conn_num",
			name+" net conn num",
			[]string{name + "_process"},
			prometheus.Labels{"process": "net conn number"},
		),
		fileDescNum: prometheus.NewDesc(
			name+"_file_description_num",
			name+" file description_num",
			[]string{name + "_process"},
			prometheus.Labels{"process": "file description num"},
		),
		threadsNum: prometheus.NewDesc(
			name+"_threads_num",
			name+" threads num",
			[]string{name + "_process"},
			prometheus.Labels{"process": "threads num"},
		),
	}
}

func (p *ProcessCollector) Describe(ch chan<- *prometheus.Desc) {
	p.mutex.Lock()
	defer p.mutex.Unlock()
	ch <- p.cpuTotalUsage
	ch <- p.memTotalUsage
	ch <- p.diskRead
	ch <- p.diskWrite
	ch <- p.netConnectNum
	ch <- p.fileDescNum
	ch <- p.threadsNum
}

func (p *ProcessCollector) Collect(ch chan<- prometheus.Metric) {
	p.mutex.Lock()
	defer p.mutex.Unlock()

	cpu, err := getCpuTotalUsage(p.pidFile)
	if err != nil {
		level.Error(common.Logger).Log("ERR", fmt.Sprintf("Get cpu total usage error: %v", err))
	}
	mem, err := getMemTotalUsage(p.pidFile)
	if err != nil {
		level.Error(common.Logger).Log("ERR", fmt.Sprintf("Get mem total usage error: %v", err))
	}
	rio, wio, err := getDiskIoReadWrite(p.pidFile)
	if err != nil {
		level.Error(common.Logger).Log("ERR", fmt.Sprintf("Get disk read write error: %v", err))
	}
	num, err := getConnectionNum(p.pidFile)
	if err != nil {
		level.Error(common.Logger).Log("ERR", fmt.Sprintf("Get net conn number error: %v", err))
	}
	fdNum, err := getFileDescNum(p.pidFile)
	if err != nil {
		level.Error(common.Logger).Log("ERR", fmt.Sprintf("Get file description error: %v", err))
	}
	tNum, err := getThreadsNum(p.pidFile)
	if err != nil {
		level.Error(common.Logger).Log("ERR", fmt.Sprintf("Get threads number error: %v", err))
	}
	ch <- prometheus.MustNewConstMetric(p.cpuTotalUsage, prometheus.GaugeValue, cpu, p.Name+"_cpu_total_usage")
	ch <- prometheus.MustNewConstMetric(p.memTotalUsage, prometheus.GaugeValue, mem, p.Name+"_mem_total_usage")
	ch <- prometheus.MustNewConstMetric(p.diskRead, prometheus.GaugeValue, rio, p.Name+"_disk_io_read")
	ch <- prometheus.MustNewConstMetric(p.diskWrite, prometheus.GaugeValue, wio, p.Name+"_disk_io_write")
	ch <- prometheus.MustNewConstMetric(p.netConnectNum, prometheus.GaugeValue, float64(num), p.Name+"_net_conn_num")
	ch <- prometheus.MustNewConstMetric(p.fileDescNum, prometheus.CounterValue, float64(fdNum), p.Name+"_file_description_num")
	ch <- prometheus.MustNewConstMetric(p.threadsNum, prometheus.CounterValue, float64(tNum), p.Name+"_threads_num")
}
