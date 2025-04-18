package models

// 添加区服表单参数校验
type Ozs struct {
	Ip       string `form:"ip" binding:"required"`
	ChanName string `form:"channame" binding:"required"`
	Zone     string `form:"zone" binding:"required"`
	Target   string `form:"target" binding:"required"`
}

// 操作区服表单参数校验
type Zos struct {
	Zones []Ozs `form:"zones" binding:"required"`
}

// 主机资源表单参数校验
type Hrs struct {
	Ips []string `form:"ips" binding:"required"`
}
