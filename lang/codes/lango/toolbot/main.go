package main

func main() {
	if cmdFlag.Mod == "web" && cmdFlag.Ip == "" {
		RunToolBot(":8083")
	}

	// mod: cli
	ips := parseIpFlag(cmdFlag.Ip)
	SearchIp(ips)
}
