// 加载配置
package config

import (
	"fmt"
	"strings"
	"sync"
	"time"

	"github.com/spf13/viper"
)

var (
	config *Config
	once   sync.Once
)

type Config struct {
	// 数据库配置
	Database struct {
		Driver   string `mapstructure:"driver" default:"mysql"`
		Host     string `mapstructure:"host" default:"localhost"`
		Port     int    `mapstructure:"port" default:"3306"`
		Username string `mapstructure:"username" default:"root"`
		Password string `mapstructure:"password" default:"123465"`
		DBName   string `mapstructure:"dbname" default:"test"`
		Charset  string `mapstructure:"charset" default:"utf8mb4"`
		MaxIdle  int    `mapstructure:"max_idle" default:"10s"`
		MaxOpen  int    `mapstructure:"max_open" default:"100s"`
	}

	// 服务器配置
	Server struct {
		Port            int           `mapstructure:"port" default:"9080"`
		Mode            string        `mapstructure:"mode" default:"debug"`
		ReadTimeout     time.Duration `mapstructure:"read_timeout" default:"30s"`
		WriteTimeout    time.Duration `mapstructure:"write_timeout" default:"30s"`
		CertCrtFile     string        `mapstructure:"cert_crt_file"`
		CertKeyFile     string        `mapstructure:"cert_key_file"`
		JwtSecret       string        `mapstructure:"jwt_secret" default:"dkndn2M5L#L"`
		TokenExpireTime time.Duration `mapstructure:"token_expire_time" default:"1h"`
	}

	// Redis配置
	Redis struct {
		Host     string `mapstructure:"host" default:"localhost"`
		Port     int    `mapstructure:"port" default:"6379"`
		Password string `mapstructure:"password" default:"123456"`
		DB       int    `mapstructure:"db" default:"0"`
	}

	// 日志配置
	Log struct {
		Level      string `mapstructure:"level"`
		Filename   string `mapstructure:"filename"`
		MaxSize    int    `mapstructure:"max_size"`
		MaxBackups int    `mapstructure:"max_backups"`
		MaxAge     int    `mapstructure:"max_age"`
		Compress   bool   `mapstructure:"compress" default:"true"`
		Formatter  string `mapstructure:"formatter" default:"text"`
	}
}

// 自动根据文件扩展名加载配置
func loadConfigAuto(configPath string) (*Config, error) {
	v := viper.New()
	// 设置配置文件路径
	v.SetConfigFile(configPath)
	// 读取配置文件
	if err := v.ReadInConfig(); err != nil {
		return nil, err
	}
	// 启用环境变量覆盖
	v.AutomaticEnv()
	// 设置环境变量前缀
	v.SetEnvPrefix("APP")
	// 替换环境变量中的点号为下划线
	// 例如: APP_DATABASE_HOST 对应配置文件中的 database.host
	v.SetEnvKeyReplacer(strings.NewReplacer(".", "_"))
	var config Config
	if err := v.Unmarshal(&config); err != nil {
		return nil, err
	}
	return &config, nil
}

// 初始化配置（支持配置文件路径）
func InitConfig(configPath string) error {
	cfg, err := loadConfigAuto(configPath)
	if err != nil {
		return err
	}
	config = cfg
	return nil
}

// 获取配置实例（线程安全）
func Get() *Config {
	if config == nil {
		once.Do(func() {
			// 默认加载config.yaml
			if err := InitConfig("config.yaml"); err != nil {
				panic("加载默认配置失败: " + err.Error())
			}
		})
	}
	return config
}

// 重新加载配置
func Reload(configPath string) error {
	cfg, err := loadConfigAuto(configPath)
	if err != nil {
		return err
	}
	config = cfg
	return nil
}

// 获取数据库DSN
func (c *Config) DbDSN() string {
	return fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=%s&parseTime=True&loc=Local",
		c.Database.Username,
		c.Database.Password,
		c.Database.Host,
		c.Database.Port,
		c.Database.DBName,
		c.Database.Charset,
	)
}

// 获取Redis地址
func (c *Config) RdsAddr() string {
	// redis://<user>:<pass>@localhost:6379/<db>
	return fmt.Sprintf("redis://:%s@%s:%d/%d", c.Redis.Password, c.Redis.Host, c.Redis.Port, c.Redis.DB)
}

// 获取服务地址
func (c *Config) SrvAddr() string {
	return fmt.Sprintf(":%d", c.Server.Port)
}
