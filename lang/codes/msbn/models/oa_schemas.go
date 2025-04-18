package models

import "time"

// 充值排行查询参数校验
type RechargeRankSchema struct {
	Stime time.Time `json:"stime" binding:"required" time_format:"2006-01-02" time_utc:"1"`
	Etime time.Time `json:"etime" binding:"required" time_format:"2006-01-02" time_utc:"1"`
	Zone  string    `json:"zone"`
	Page  Page      `json:"page"`
}

// 等级分布
type GradeDistibutionSchema struct {
	Stime time.Time `json:"stime" binding:"required" time_format:"2006-01-02" time_utc:"1"`
	Etime time.Time `json:"etime" binding:"required" time_format:"2006-01-02" time_utc:"1"`
	Zone  string    `json:"zone"`
	Page  Page      `json:"page"`
}

type Page struct {
	Size int `json:"size"`
	Num  int `json:"num"`
}

// VIP等级
type VipGradeSchema struct {
	Zone uint `json:"zone"`
}
