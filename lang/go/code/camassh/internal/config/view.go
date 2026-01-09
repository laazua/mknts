package config

// 获取CA视图
type CAView struct {
	cfg *config
}

func (v CAView) Host() string {
	return v.cfg.ca.host
}

func (v CAView) Path() string {
	return v.cfg.ca.path
}

func (v CAView) LogPath() string {
	return v.cfg.ca.logPath
}

func (v CAView) Nets() []string {
	return v.cfg.ca.nets
}

// 获取堡垒机视图
type BastionView struct {
	cfg *config
}

func (v BastionView) Host() string {
	return v.cfg.bastion.host
}
