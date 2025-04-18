package models

import "time"

// 角色数据查询表单校验
type Rgs struct {
	Stime time.Time `form:"stime" binding:"required" time_format:"2006-01-02" time_utc:"1"`
	Etime time.Time `form:"etime" binding:"required" time_format:"2006-01-02" time_utc:"1"`
	Zone  string    `form:"zone" binding:"required"`
}

// 订单数据查询表单校验
type Ods struct {
	Zone  string `form:"zone" binding:"required"`
	Uid   string `form:"uid" binding:"required"`
	Order string `form:"order" binding:"required"`
}

// 货币数据查询表单校验
type Cds struct {
	Rgs
}
