package collector

import (
	"testing"
)

func TestReadPid(t *testing.T) {
	pid := readPid("/app/node_exporter/pid.txt")
	if pid == 0 {
		t.Error("读取pid失败")
	} else {
		t.Log("读取pid成功")
	}
}

func TestGetProcess(t *testing.T) {
	p, err := getProcess("/app/node_exporter/pid.txt")
	if err != nil {
		t.Errorf("获取进程实例失败: %v", err)
	} else {
		t.Logf("获取进程实例成功: %v", p.Pid)
	}
}

func TestGetDiskIo(t *testing.T) {
	ioCnt, err := getDiskIo("/app/node_exporter/pid.txt")
	if err != nil {
		t.Errorf("获取磁盘IO失败: %v", err)
	} else {
		t.Logf("磁盘IO: %v", ioCnt)
		t.Logf("进程读取磁盘次数: %v", ioCnt.ReadCount)
		t.Logf("进程写入磁盘次数: %v", ioCnt.WriteCount)
		t.Logf("进程读取磁盘的字节数: %v", ioCnt.ReadBytes)
		t.Logf("进程写入磁盘的字节数: %v", ioCnt.WriteBytes)
	}
}

func TestGetCpuTotalUsage(t *testing.T) {
	c, err := getCpuTotalUsage("/app/node_exporter/pid.txt")
	if err != nil {
		t.Errorf("获取进程cpu使用情况失败: %v", err)
	} else {
		t.Logf("获取进程cpu使用情况成功: %v", c)
	}
}

func TestGetMemTotalUsage(t *testing.T) {
	m, err := getMemTotalUsage("/app/node_exporter/pid.txt")
	if err != nil {
		t.Errorf("获取进程内存使用情况失败: %v", err)
	} else {
		t.Logf("获取进程内存使用情况成功: %v", m)
	}
}

func TestGetNetConnNum(t *testing.T) {
	num, err := getNetConnNum("/app/node_exporter/pid.txt")
	if err != nil {
		t.Errorf("获取进程网络连接数量失败: %v", err)
	} else {
		t.Logf("获取进程网络连接数量成功: %v", num)
	}
}

func TestGetRequestNum(t *testing.T) {
	num, err := getConnectionNum("/home/huheng/app/node_exporter/pid.txt")
	if err != nil {
		t.Errorf("获取请求连接数量失败: %v", err)
	} else {
		t.Logf("请求连接数量: %v", num)
	}
}
