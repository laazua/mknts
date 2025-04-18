package models

type Page struct {
	Size int `form:"size" binding:"required"`
	Num  int `form:"num" binding:"required"`
}

// 充值排行接口参数校验
type Rrs struct {
	Stime string `form:"stime" binding:"required"`
	Etime string `form:"etime" binding:"required"`
	Zone  string `form:"zone" binding:"required"`
}

// 等级分布接口参数校验
type Gds struct {
	Stime string `form:"stime" binding:"required"`
	Etime string `form:"etime" binding:"required"`
	Zone  string `form:"zone" binding:"required"`
}

// 数据查询接口参数校验
type Dgs struct {
	Gds
}

// 滚服数据接口参数校验
type Rds struct {
	Gds
}

// 留存数据接口参数校验
type Kds struct {
	Gds
}
