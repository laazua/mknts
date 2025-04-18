// 反射会降低代码运行效率,经常被调用的代码不要使用反射！
package main

import(
    "fmt"
    "reflect"
    "os"
)

// 一个配置类 Config，每个字段是一个配置项
type Config struct {
	Name    string `json:"server-name"` // CONFIG_SERVER_NAME
	IP      string `json:"server-ip"`   // CONFIG_SERVER_IP
	URL     string `json:"server-url"`  // CONFIG_SERVER_URL
	Timeout string `json:"timeout"`     // CONFIG_TIMEOUT
}

func main() {
	os.Setenv("CONFIG_SERVER_NAME", "global_server")
	os.Setenv("CONFIG_SERVER_IP", "10.0.0.1")
	os.Setenv("CONFIG_SERVER_URL", "geektutu.com")
	c := readConfig()
	fmt.Printf("%+v", c)
}

func readConfig() *Config {
	// read from xxx.json，省略
	config := Config{}
	typ := reflect.TypeOf(config)
	value := reflect.Indirect(reflect.ValueOf(&config))
	for i := 0; i < typ.NumField(); i++ {
            f := typ.Field(i)
	    if v, ok := f.Tag.Lookup("json"); ok {
	        key := fmt.Sprintf("CONFIG_%s", strings.ReplaceAll(strings.ToUpper(v), "-", "_"))
		if env, exist := os.LookupEnv(key); exist {
		    value.FieldByName(f.Name).Set(reflect.ValueOf(env))
		}
	    }
	}
	return &config
}
