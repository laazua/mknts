// init子命令实现
package cmds

import (
	"fmt"
	"strings"

	"camassh/internal/cli"
	"camassh/internal/comm"
	"camassh/internal/config"
	"camassh/internal/sshx"
)

type InitCommand struct {
	*cli.BaseCommand
}

func NewInitCommand() cli.Command {
	cmd := &InitCommand{
		BaseCommand: cli.NewBaseCommand("init", "初始化CA、堡垒机或节点"),
	}
	return cmd
}

func (c *InitCommand) Configure(cfg *cli.CommandConfig) {
	c.BaseCommand.Configure(cfg)
	// 	cfg.SetUsage(`Usage: camassh init --target <name>
	// Example:
	//   camassh init --target ca
	//   camassh init --target bastion
	//   camassh init --target node
	// `)
	// 添加flag
	c.StringFlag("target", "ca", "目标名称 (必需: ca, bastion, node)")
}

// Help 返回命令帮助信息
func (c *InitCommand) Help() string {
	// 调用父类的 Help() 方法
	helpText := c.BaseCommand.Help()

	// 可以在这里添加额外的帮助信息
	extraHelp := "\n可用目标类型:\n" +
		"  ca      初始化证书颁发机构\n" +
		"  bastion 初始化堡垒机\n" +
		"  node    初始化普通节点\n\n" +
		"示例:\n" +
		"  camassh init --target ca\n" +
		"  camassh init --target bastion\n" +
		"  camassh init --target node\n"

	return helpText + extraHelp
}

func (c *InitCommand) Run(ctx cli.Context) error {
	target := c.GetFlag("target").(*string)

	// 验证必需参数
	if *target == "" {
		return fmt.Errorf("必须指定 --target 参数")
	}
	// 执行命令逻辑
	// ctx.Printf("初始化目标: %s\n", *target)
	if *target == "ca" {
		ctx.Printf("初始化CA目标: %s\n", *target)
		return initCa(ctx)
	}
	if *target == "bastion" {
		ctx.Printf("初始化堡垒机目标: %s\n", *target)
		return initBastion(ctx)
	}
	if *target == "node" {
		ctx.Printf("初始化节点目标: %s\n", *target)
		return initNode(ctx)
	}
	return nil
}

// 初始化ca
func initCa(ctx cli.Context) error {
	excutor := comm.NewCommandExecutor()
	// ctx.Printf("%v\n", shellContext)
	cmds := []string{
		fmt.Sprintf("sudo mkdir -p %v", config.Get().CA().Path()),
		fmt.Sprintf("sudo chmod 700 %v", config.Get().CA().Path()),
		fmt.Sprintf("sudo ssh-keygen -t ed25519 -f %v/host_ca -C 'OpenSSH Host CA'", config.Get().CA().Path()),
		fmt.Sprintf("sudo chmod 600 %v/host_ca", config.Get().CA().Path()),
	}
	result := excutor.RunMultipleCommands(cmds)
	if result.Err != nil {
		return fmt.Errorf("初始化CA失败: %v", result.Err)
	}
	ctx.Printf("初始化CA成功,CA路径: %s\n", config.Get().CA().Path())
	return nil
}

// 初始化堡垒机
func initBastion(ctx cli.Context) error {
	excutor := comm.NewCommandExecutor()
	client, err := getSshClient()
	if err != nil {
		return fmt.Errorf("获取SSH登录会话失败")
	}
	defer client.Close()
	// 拷贝CA 公钥到堡垒机
	cmds := []string{fmt.Sprintf("sudo test -f %v/host_ca.pub", config.Get().CA().Path())}
	result := excutor.RunMultipleCommands(cmds)
	if result.ExitCode != 0 {
		// 带进度显示的上传
		progressCallback := func(p *sshx.FileTransferProgress) {
			fmt.Printf("Uploading %s: %.2f%%\n", p.Filename, p.Percentage)
		}
		err = client.UploadFileWithProgress(fmt.Sprintf("%v/host_ca.pub", config.Get().CA().Path()), "/etc/ssh/host_ca.pub", progressCallback)
		if err != nil {
			return fmt.Errorf("上传 CA 公钥到堡垒机失败: %v", err.Error())
		}
	}
	// 配置信任主机
	var nodeIp string
	fmt.Print("输入信任节点IP: ")
	fmt.Scan(&nodeIp)
	cmds = []string{
		fmt.Sprintf(`echo "@cert-authority %v $(cat /etc/ssh/host_ca.pub)" >/etc/ssh/ssh_known_hosts`, strings.TrimSpace(nodeIp)),
		// 备份
		"sudo cp /etc/ssh/ssh_config /etc/ssh/ssh_config.bak-$(date +%Y%m%d)",
		// 清空文件并逐行写入
		"sudo echo 'Include /etc/ssh/ssh_config.d/*.conf' >/etc/ssh/ssh_config",
		fmt.Sprintf(`sudo echo "Host %v" >/etc/ssh/ssh_config`, strings.TrimSpace(nodeIp)),
		"sudo echo '    StrictHostKeyChecking yes' >/etc/ssh/ssh_config",
		"sudo echo '    UserKnownHostsFile /etc/ssh/ssh_known_hosts' >/etc/ssh/ssh_config",
	}
	_, err = client.RunMultiple(cmds)
	if err != nil {
		return fmt.Errorf("配置信任主机失败: %v", err.Error())
	}
	ctx.Printf("更新堡垒机sshd成功\n")
	return nil
}

// 初始化节点
func initNode(ctx cli.Context) error {
	excuter := comm.NewCommandExecutor()
	client, err := getSshClient()
	if err != nil {
		return fmt.Errorf("创建SSH登录客户端会话失败")
	}
	defer client.Close()
	// 登录被管理节点
	ctx.Printf("连接被管理节点成功\n")
	var hostnameChaged string
	fmt.Print("节点是否更改hostname: [yes|no]: ")
	fmt.Scan(&hostnameChaged)
	if strings.TrimSpace(hostnameChaged) != "yes" {
		var hostname string
		fmt.Print("请输出主机名: ")
		fmt.Scan(&hostname)
		cmd := fmt.Sprintf("sudo hostnamectl %v", strings.TrimSpace(hostname))
		_, err := client.Run(cmd)
		if err != nil {
			return fmt.Errorf("设置主机名失败")
		}
	}
	var hostname, myip string
	result, err := client.Run("sudo hostname")
	if err != nil {
		return fmt.Errorf("获取主机名失败: %v", err.Error())
	}
	hostname = strings.TrimSpace(result.Stdout)
	result, err = client.Run("sudo hostname -I")
	if err != nil {
		return fmt.Errorf("获取主机IP失败: %v", err.Error())
	}
	myip = strings.TrimSpace(result.Stdout)
	// 生成管理节点的主机密钥
	cmd := "sudo test ! -f /etc/ssh/ssh_host_ed25519_key && sudo ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N ''"
	_, err = client.Run(cmd)
	if err != nil {
		return fmt.Errorf("创建主机密钥失败")
	}
	// 将被管理节点的主机公钥拷贝到CA服务器
	// err = client.DownloadFile("/etc/ssh/ssh_host_ed25519_key.pub", fmt.Sprintf("%v/%v", config.Get().CA().Path(), hostname))
	// 带进度显示下载
	progressCallback := func(p *sshx.FileTransferProgress) {
		fmt.Printf("Downloading %s: %.2f%%\n", p.Filename, p.Percentage)
	}
	err = client.DownloadFileWithProgress("/etc/ssh/ssh_host_ed25519_key.pub", fmt.Sprintf("%v/%v.pub", config.Get().CA().Path(), hostname), progressCallback)
	if err != nil {
		return fmt.Errorf("下载主机公钥失败: %v", err.Error())
	}
	// 在 CA 上签发证书
	caPath := config.Get().CA().Path()
	cmds := []string{
		fmt.Sprintf(
			`sudo ssh-keygen -s %v/host_ca -I "%v-$(date +%%Y%%m%%d)" -h -n "%v,%v"  -V +180d %v/%v.pub`,
			caPath, hostname, hostname, myip, caPath, hostname),
	}
	r := excuter.RunMultipleCommands(cmds)
	if r.Err != nil {
		return fmt.Errorf("CA 签发证书失败: %v", r.Err.Error())
	}
	// 把证书上传到node节点
	err = client.UploadFile(fmt.Sprintf("%v/%v-cert.pub", caPath, hostname), "/etc/ssh/ssh_host_ed25519_key-cert.pub")
	if err != nil {
		return fmt.Errorf("回传CA颁发的证书失败: %v", err.Error())
	}
	// 配置sshd,并重启
	cmds = []string{
		// 备份
		"sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak-$(date +%Y%m%d)",

		// 清空文件并逐行写入
		`sudo sh -c 'cat > /etc/ssh/sshd_config << "ENDSSHDCONFIG"
Include /etc/ssh/sshd_config.d/*.conf
Subsystem sftp /usr/libexec/openssh/sftp-server
PermitRootLogin no
PasswordAuthentication no
PermitEmptyPasswords no
GSSAPIAuthentication no
UsePAM yes
ChallengeResponseAuthentication no
UseDNS no
AddressFamily inet
ENDSSHDCONFIG'`,

		// 验证并重启
		"sudo sshd -t && sudo systemctl restart sshd",
	}
	_, err = client.RunMultiple(cmds)
	if err != nil {
		return fmt.Errorf("配置sshd失败")
	}
	ctx.Printf("初始化被管理节点成功\n")
	return nil
}
