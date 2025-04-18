package model

import (
	"github.com/google/uuid"
	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	Name           string    `gorm:"name"`
	Password       string    `gorm:"password"`
	Email          string    `gorm:"email"`
	TrafficUp      int64     `gorm:"trafficUp"`      // 上行流量计算
	TrafficDown    int64     `gorm:"trafficDown"`    // 下行流量计算
	TrafficTag     string    `gorm:"TrafficTag"`     // 流量套餐标识(购买后确定:m20|m50|m120)
	AccountBalance uint      `gorm:"accountBalance"` // 账户余额
	Uuid           uuid.UUID `gorm:"uuid"`
}

type LoginRequest struct {
	Username string `form:"username"`
	Password string `form:"password"`
}
