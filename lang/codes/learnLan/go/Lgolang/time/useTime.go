package main

import (
	"fmt"
	"time"
)

func main() {
	//从00:00:00UTC, 1970年1月1日以来的秒数
	fmt.Println("Epoch Time:", time.Now().Unix())
	t := time.Now()
	//时间格式转换
	fmt.Println(t, t.Format(time.RFC3339))
	//各种时间间隔
	fmt.Println(t.Weekday(), t.Day(), t.Month(), t.Year())

	time.Sleep(time.Second)
	t1 := time.Now()
	//连个时间点之间的间隔
	fmt.Println("Time difference:", t1.Sub(t))

	formatT := t.Format("01 January 2006")
	fmt.Println(formatT)
	loc, _ := time.LoadLocation("Europe/Paris")
	LondonTime := t.In(loc)
	fmt.Println("Paris:", LondonTime)
}
