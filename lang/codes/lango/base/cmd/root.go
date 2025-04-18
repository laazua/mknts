package cmd

var cmdFlags struct {
	Name    string
	Address string
}

func init() {
	cmdFlags.Name = "ZhangSan"
	cmdFlags.Address = "ChengDu"
}
