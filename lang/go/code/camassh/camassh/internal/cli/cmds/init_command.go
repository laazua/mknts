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
	excutor *comm.CommandExecutor
}

func NewInitCommand() cli.Command {
	cmd := &InitCommand{
		BaseCommand: cli.NewBaseCommand("init", "初始化CA、堡垒机或节点"),
		excutor:     comm.NewCommandExecutor(),
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
	// 添加标志
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
		return initCa(ctx, c)
	}
	if *target == "bastion" {
		ctx.Printf("初始化堡垒机目标: %s\n", *target)
		return initBastion(ctx, c)
	}
	return nil
}

// 初始化ca
func initCa(ctx cli.Context, cmd *InitCommand) error {
	// ctx.Printf("%v\n", shellContext)
	// 创建CA目录结构和密钥对
	result := cmd.excutor.RunShell(initCaScript)
	if result.Err != nil {
		return fmt.Errorf("初始化CA失败: %v", result.Stderr)
	}
	ctx.Printf("CA初始化成功,路径: %s\n", config.Get().CA().Path())

	// 创建用户证书签发脚本
	result = cmd.excutor.RunShell(issueUserCertScript)
	if result.Err != nil {
		return fmt.Errorf("初始化用户证书失败: %v", result.Stderr)
	}
	result = cmd.excutor.RunShell(issueHostCertScript)
	if result.Err != nil {
		return fmt.Errorf("初始化主机证书失败: %v", result.Stderr)
	}
	result = cmd.excutor.RunShell(revokeCertScript)
	if result.Err != nil {
		return fmt.Errorf("初始化吊销证书脚本失败: %v", result.Stderr)
	}
	result = cmd.excutor.RunShell(distributeCaPubKeyScript)
	if result.Err != nil {
		return fmt.Errorf("初始化分发CA公钥脚本失败: %v", result.Stderr)
	}
	return nil
}

// 初始化堡垒机
func initBastion(ctx cli.Context, cmd *InitCommand) error {
	var name, ipAddress, port string
	fmt.Print("请输入堡垒机IP地址: ")
	fmt.Scan(&ipAddress)
	fmt.Print("请输入堡垒机SSH端口: ")
	fmt.Scan(&port)
	fmt.Print("请输入登录堡垒机用户名: ")
	fmt.Scan(&name)
	// 安全的输入密码方式
	password, err := getPassword("请输入堡垒机用户密码: ")
	if err != nil {
		return fmt.Errorf("获取密码失败: %v", err)
	}
	// 配置SSH连接
	sshConfig := &sshx.Config{
		Host:     strings.TrimSpace(ipAddress),
		Port:     strToInt(strings.TrimSpace(port), 22),
		Username: strings.TrimSpace(name),
		Password: strings.TrimSpace(password),
	}
	// 创建客户端
	client, err := sshx.NewClient(sshConfig)
	if err != nil {
		return fmt.Errorf("创建SSH客户端失败: %v", err)
	}
	defer client.Close()
	var userExist, optUser string
	fmt.Print("请确认是否存在堡垒机操作用户[yes|no]: ")
	fmt.Scan(&userExist)
	if strings.TrimSpace(userExist) != "yes" {
		return fmt.Errorf("请先创建堡垒机操作用户后再执行此操作")
	}
	fmt.Print("请输入堡垒机操作用户: ")
	fmt.Scan(&optUser)

	// 生成密钥
	certCmd := fmt.Sprintf(`ssh-keygen -t rsa -b 4096  -f ~/.ssh/id_rsa -C "%v@client-server" -N ""`, strings.TrimSpace(optUser))
	catCmd := "cat ~/.ssh/id_rsa.pub"
	cmds := []string{certCmd, catCmd}
	_, err = client.RunMultiple(cmds)
	if err != nil {
		return fmt.Errorf("执行生成密钥命令失败: %v", err)
	}
	return nil
}

// 初始化节点
func initNode(ctx cli.Context, cmd *InitCommand) error {
	var name, ipAddress, port string
	fmt.Print("请输入节点IP地址: ")
	fmt.Scan(&ipAddress)
	fmt.Print("请输入节点SSH端口: ")
	fmt.Scan(&port)
	fmt.Print("请输入登录节点用户名: ")
	fmt.Scan(&name)
	// 安全的输入密码方式
	password, err := getPassword("请输用户入密码: ")
	if err != nil {
		return fmt.Errorf("获取密码失败: %v", err)
	}
	// 配置SSH连接
	sshConfig := &sshx.Config{
		Host:     strings.TrimSpace(ipAddress),
		Port:     strToInt(strings.TrimSpace(port), 22),
		Username: strings.TrimSpace(name),
		Password: strings.TrimSpace(password),
	}
	// 创建客户端
	client, err := sshx.NewClient(sshConfig)
	if err != nil {
		return fmt.Errorf("创建SSH客户端失败: %v", err)
	}
	defer client.Close()
	// 连接
	ctx.Printf("连接堡垒机成功\n")
	err = client.UploadFile(fmt.Sprintf("%v/users/public/user-ca.pub", config.Get().CA().Path()), "/etc/ssh/")
	if err != nil {
		return fmt.Errorf("上传CA公钥失败: %v", err)
	}
	// 配置信任CA
	cmds := []string{
		"sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup.$(date +%Y%m%d)",
		`sudo cat >> /etc/ssh/sshd_config << 'EOF'

# === SSH CA 配置 ===
# 信任的用户 CA
TrustedUserCAKeys /etc/ssh/user-ca.pub

# 可选：配置吊销列表（如果需要）
# RevokedKeys /etc/ssh/revoked_keys

# 可选：禁用密码认证（推荐）
PasswordAuthentication no
ChallengeResponseAuthentication no

# 可选：限制只有特定组的用户可以使用证书登录
# Match User *,!root
#    AuthenticationMethods publickey
EOF`,
		"sudo sshd -t",
		"sudo systemctl restart sshd || sudo systemctl restart ssh",
	}
	_, err = client.RunMultiple(cmds)
	if err != nil {
		return fmt.Errorf("配置信任CA失败: %v", err)
	}

	return nil
}
