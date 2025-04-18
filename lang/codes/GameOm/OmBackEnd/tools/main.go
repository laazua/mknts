package main

import (
	"flag"
	"fmt"
	"time"

	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/disk"
	"github.com/shirou/gopsutil/mem"
	"github.com/shirou/gopsutil/v3/load"
)

var diskPath = flag.String("dpath", "/", "disk mount path")

func main() {

	flag.Parse()
	m, _ := mem.VirtualMemory()

	c, _ := cpu.Percent(3*time.Second, false)

	d, _ := disk.Usage(*diskPath)

	l, _ := load.Avg()

	fmt.Printf("{\"cpu\": %0.2f, \"mem\": %0.2f, \"disk\": %0.2f, \"load\": %v}\n", c[0], m.UsedPercent, d.UsedPercent, l.Load5)
}
