### 初始化结构体字段

- **结构体**
```go
type Config struct {
    Name string
    Addr String
    Age  int
}
```

- **构造函数**
```go
// 适用于简单场景
func NewConfig(name, addr string, age int) *Config {
    return &Config{
        Name: name,
        Addr: addr,
        Age:  age
    }
}
// 使用: cfg := NewConfig("zhangsan", "Chengdu", 18)
```

- **函数式选项**
```go
// 适用于需要可选参数的场景,灵活性高
type Option func(*Config)

func NewConfig(opts ...Option) *Config {
    // 默认值
    cfg :== &Config{
        Name: "zhangsan",
        Addr: "Chengdu",
        Age:  18,
    }
    for _, opt := range opts {
        opt(cfg)
    }
    return cfg
}

func WithName(name string) Option {
    return func(cfg *Cofnig) {
        cfg.Name = name
    }
}

func WithAddr(addr string) Option {
    return func(cfg *Config) {
        cfg.Addr = addr
    }
}

func WithAge(age int) Option {
    return func(cfg *Config) {
        cfg.Age = age
    }
}

// 使用: cfg := NewConfig(WithName("lis"))
```

- **Builder模式**
```go
// 适用于链式配置
type ConfigBuilder struct {
    config Config
}

func NewConfigBuilder() *ConfigBuilder {
    return &ConfigBuilder {
        config: Config {
            Name: "zhangsan",
            Addr: "Chengdu",
            Age:  18,
        },
    }
}

func (cb *ConfigBuilder) WithName(name string) *ConfigBuilder {
    cb.config.Name = name
    return cb
}

func (cb *ConfigBuilder) WithAddr(addr string) *ConfigBuilder {
    cb.config.Addr = addr
    return cb
}

func (cb *ConfigBuilder) WithAge(age int) *ConfigBuilder {
    cb.config.Age = age
    return cb
}

func (cb *ConfigBuilder) Build() *Config {
    return &cb.config 
}

// 使用: cfg := NewConfigBuilder().WithName("lisi").WithAddr("Beijing").Build()
```
- **配置结构&&默认值**
```go
// 适用于配置管理
type Config struct {
    Name string `json:"name"`
    Addr string `json:"addr"`
    Age  int    `json:"age"`
}

func DefaultConfig() *Config {
    return &Config {
        Name: "zhangsan",
        Addr: "Chengdu",
        Age:  18,
    }
}

// 使用:
// cfg := DefaultConfig()
// cfg.Name = "lisi"
// cfg.Addr = "Beijing"
```

- **从配置文件加载**
```go
// 适用于配置管理
type Config struct {
    Name string `yaml:"name"`
    Addr string `yaml:"addr"`
    Age  int    `yaml:"age"`
}

func LoadYaml(fileName string) (*Config, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, err
    }
    
    var cfg Config
    if err := yaml.Unmarshal(data, &cfg); err != nil {
        return nil, err
    }
    
    return &cfg, nil
}
```