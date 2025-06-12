### 热加载配置

- 代码
```go
package config

import (
	"log"
	"os"
	"sync"
	"time"

	"github.com/fsnotify/fsnotify"
	"gopkg.in/yaml.v3"
)

type AppConfig struct {
	Name string `yaml:"name"`
}

var (
	Cfg   AppConfig
	once  sync.Once
	mutex sync.RWMutex
)

func LoadConfig(path string) {
	once.Do(func() {
		readConfig(path)
		go watch(path)
	})
}

func readConfig(path string) {
	data, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("read config file error: %v", err)
	}
	mutex.Lock()
	defer mutex.Unlock()
	if err := yaml.Unmarshal(data, &Cfg); err != nil {
		log.Fatalf("parser config error: %v", err)
	}
	log.Println("配置加载完成:", Cfg)
}

func watch(path string) {
	watcher, err := fsnotify.NewWatcher()
	if err != nil {
		log.Fatalf("启动配置监听失败: %v", err)
	}
	defer watcher.Close()

	if err := watcher.Add(path); err != nil {
		log.Fatalf("监听配置文件失败: %v", err)
	}

	for {
		select {
		case ev := <-watcher.Events:
			if ev.Op&fsnotify.Write == fsnotify.Write {
				log.Println("检测到配置文件变化，重新加载中...")
				readConfig(path)
			}
		case err := <-watcher.Errors:
			log.Println("配置文件监听出错:", err)
		}
		time.Sleep(500 * time.Millisecond) // 防抖
	}
}

func GetConfig() AppConfig {
	mutex.RLock()
	defer mutex.RUnlock()
	return Cfg
}

```
