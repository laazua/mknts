package collector

import (
	"bufio"
	"errors"
	"os"
	"p_exporter/common"
	"strconv"
	"time"

	"github.com/go-kit/log/level"
	"github.com/shirou/gopsutil/mem"
	"github.com/shirou/gopsutil/v3/process"
)

var PidStatus chan string

// 读取pid进程号
func readPid(pidfile string) int {
	file, err := os.Open(pidfile)
	if err != nil {
		level.Error(common.Logger).Log("ERR", "open pid file error")
		return 0
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var pid int
	// 读取文件的第一行（只读取一行）
	if scanner.Scan() {
		// 获取读取的内容并转换为整数
		str := scanner.Text()
		pid, err = strconv.Atoi(str)
		if err != nil {
			return 0
		}
	}
	// 检查Scanner是否发生错误
	if scanner.Err() != nil {
		level.Error(common.Logger).Log("ERR", "scanner pid file error")
		return 0
	}

	return pid
}

// 实现逻辑当被监控的进程停止运行时
// 把被监控的进程从列表中移除,否则监控程序会崩溃
func WatchPidStat() bool {
	select {
	case <-PidStatus:
		return true
	default:
		return false
	}
}

// 获取进程实例
func getProcess(pidFile string) (*process.Process, error) {
	pid := readPid(pidFile)
	if pid == 0 {
		PidStatus <- pidFile
		return nil, errors.New("读取pid失败")
	}
	// 通过PID获取进程实例
	p, err := process.NewProcess(int32(pid))
	if err != nil {
		return nil, err
	}
	return p, nil
}

// 获取进程磁盘io情况
func getDiskIo(pidFile string) (*process.IOCountersStat, error) {
	p, err := getProcess(pidFile)
	if err != nil {
		return nil, err
	}
	ioCounters, err := p.IOCounters()
	if err != nil {
		return nil, err
	}
	return ioCounters, nil
}

// 获取进程cpu使用情况
func getCpuTotalUsage(pidFile string) (float64, error) {
	p, err := getProcess(pidFile)
	if err != nil {
		return -0.1, err
	}
	cpuPercent, err := p.CPUPercent()
	if err != nil {
		return -0.1, err
	}

	return cpuPercent, nil
}

// 获取进程内存使用情况
func getMemTotalUsage(pidFile string) (float64, error) {
	p, err := getProcess(pidFile)
	if err != nil {
		return -0.1, err
	}
	memPInfo, err := p.MemoryInfo()
	if err != nil {
		return -0.1, err
	}
	// 获取主机内存使用情况
	memHInfo, err := mem.VirtualMemory()
	if err != nil {
		return -0.1, err
	}
	// 进程内存使用率
	memUsage := float64(memPInfo.RSS) / float64(memHInfo.Total) * 100
	return memUsage, nil
}

// 进程磁盘io读取写入速率
func getDiskIoReadWrite(pidFile string) (float64, float64, error) {
	preDiskIo, err := getDiskIo(pidFile)
	if err != nil {
		return -0.1, -0.1, err
	}
	stime := time.Now()
	time.Sleep(200 * time.Millisecond)
	etime := time.Now()
	atime := etime.Sub(stime).Seconds()
	curDiskIo, _ := getDiskIo(pidFile)
	readByte := float64(curDiskIo.ReadBytes-preDiskIo.ReadBytes) / atime
	writeByte := float64(curDiskIo.WriteBytes-preDiskIo.WriteBytes) / atime

	return readByte, writeByte, nil
}

// 进程文件句柄数量
func getFileDescNum(pidFile string) (int32, error) {
	p, err := getProcess(pidFile)
	if err != nil {
		return -1, err
	}
	num, err := p.NumFDs()
	if err != nil {
		return -1, err
	}
	return num, nil
}

// 进程中的线程数量
func getThreadsNum(pidFile string) (int32, error) {
	p, err := getProcess(pidFile)
	if err != nil {
		return -1, err
	}
	num, err := p.NumThreads()
	if err != nil {
		return -1, err
	}
	return num, nil
}

// 进程网络连接数量
func getConnectionNum(pidFile string) (int, error) {
	p, err := getProcess(pidFile)
	if err != nil {
		return -1, err
	}
	nums, err := p.Connections()
	if err != nil {
		return -1, err
	}
	return len(nums), nil
}
