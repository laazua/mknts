// comm/config_test.go
package comm

import (
	"os"
	"reflect"
	"testing"
	"time"
)

func TestLoadEnv(t *testing.T) {
	// 准备测试用的.env文件内容
	envContent := `# 注释行
APP_NAME=TestApp
PORT=8080
DEBUG=true
TIMEOUT=30.5

# 列表测试
STR_LIST=["a", "b", "c"]
INT_LIST=[1, 2, 3, 4]
MIXED_LIST=[1, "two", true, 3.14]

# 对象测试
DB_CONFIG={host: "localhost", port: 5432, name: "testdb"}
CACHE={enabled: true, ttl: 3600, servers: ["redis1", "redis2"]}

# 引号测试
QUOTED_STR="hello world"
SINGLE_QUOTED='test string'
EMPTY_LIST=[]
EMPTY_OBJ={}
`

	// 创建临时.env文件
	tmpFile, err := os.CreateTemp(".", "test*.env")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tmpFile.Name())
	defer tmpFile.Close()

	if _, err := tmpFile.WriteString(envContent); err != nil {
		t.Fatal(err)
	}
	tmpFile.Close()

	// 重置全局配置
	defaultConfig = &Config{
		data: make(map[string]interface{}),
	}

	// 测试加载配置
	err = LoadEnv(tmpFile.Name())
	if err != nil {
		t.Fatalf("LoadEnv failed: %v", err)
	}

	// 测试基本类型
	tests := []struct {
		key      string
		expected interface{}
		getter   func(*Config) interface{}
	}{
		{
			key:      "APP_NAME",
			expected: "TestApp",
			getter:   func(c *Config) interface{} { return c.Str("APP_NAME") },
		},
		{
			key:      "PORT",
			expected: 8080,
			getter:   func(c *Config) interface{} { return c.Int("PORT") },
		},
		{
			key:      "DEBUG",
			expected: true,
			getter:   func(c *Config) interface{} { return c.Bool("DEBUG") },
		},
		{
			key:      "TIMEOUT",
			expected: 30.5,
			getter:   func(c *Config) interface{} { return c.Float("TIMEOUT") },
		},
		{
			key:      "QUOTED_STR",
			expected: "hello world",
			getter:   func(c *Config) interface{} { return c.Str("QUOTED_STR") },
		},
		{
			key:      "SINGLE_QUOTED",
			expected: "test string",
			getter:   func(c *Config) interface{} { return c.Str("SINGLE_QUOTED") },
		},
	}

	for _, tt := range tests {
		t.Run(tt.key, func(t *testing.T) {
			got := tt.getter(Env())
			if !reflect.DeepEqual(got, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, got)
			}
		})
	}
}

func TestConfigList(t *testing.T) {
	envContent := `STR_LIST=["a", "b", "c"]
INT_LIST=[1, 2, 3, 4]
MIXED_LIST=[1, "two", true, 3.14]
EMPTY_LIST=[]
`

	tmpFile, err := os.CreateTemp(".", "test*.env")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tmpFile.Name())
	defer tmpFile.Close()

	if _, err := tmpFile.WriteString(envContent); err != nil {
		t.Fatal(err)
	}
	tmpFile.Close()

	cfg := NewConfig()
	if err := cfg.LoadEnv(tmpFile.Name()); err != nil {
		t.Fatalf("LoadEnv failed: %v", err)
	}

	// 测试字符串列表
	strList := cfg.StrList("STR_LIST")
	expectedStrList := []string{"a", "b", "c"}
	if !reflect.DeepEqual(strList, expectedStrList) {
		t.Errorf("StrList: expected %v, got %v", expectedStrList, strList)
	}

	// 测试整数列表
	intList := cfg.IntList("INT_LIST")
	expectedIntList := []int{1, 2, 3, 4}
	if !reflect.DeepEqual(intList, expectedIntList) {
		t.Errorf("IntList: expected %v, got %v", expectedIntList, intList)
	}

	// 测试混合列表
	mixedList := cfg.List("MIXED_LIST")
	if len(mixedList) != 4 {
		t.Errorf("MixedList length: expected 4, got %d", len(mixedList))
	}

	// 测试空列表
	emptyList := cfg.List("EMPTY_LIST")
	if len(emptyList) != 0 {
		t.Errorf("EmptyList: expected length 0, got %d", len(emptyList))
	}
}

func TestConfigObject(t *testing.T) {
	envContent := `DB_CONFIG={host: "localhost", port: 5432, name: "testdb"}
CACHE={enabled: true, ttl: 3600, servers: ["redis1", "redis2"]}
EMPTY_OBJ={}
`

	tmpFile, err := os.CreateTemp(".", "test*.env")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tmpFile.Name())
	defer tmpFile.Close()

	if _, err := tmpFile.WriteString(envContent); err != nil {
		t.Fatal(err)
	}
	tmpFile.Close()

	cfg := NewConfig()
	if err := cfg.LoadEnv(tmpFile.Name()); err != nil {
		t.Fatalf("LoadEnv failed: %v", err)
	}

	// 测试基本对象
	dbConfig := cfg.Obj("DB_CONFIG")
	expectedHost := "localhost"
	if dbConfig["host"] != expectedHost {
		t.Errorf("DB host: expected %v, got %v", expectedHost, dbConfig["host"])
	}

	expectedPort := 5432
	if dbConfig["port"] != expectedPort {
		t.Errorf("DB port: expected %v, got %v", expectedPort, dbConfig["port"])
	}

	// 测试嵌套对象
	cacheConfig := cfg.Obj("CACHE")
	if cacheConfig["enabled"] != true {
		t.Errorf("Cache enabled: expected true, got %v", cacheConfig["enabled"])
	}

	if cacheConfig["ttl"] != 3600 {
		t.Errorf("Cache ttl: expected 3600, got %v", cacheConfig["ttl"])
	}

	// 测试嵌套列表
	if servers, ok := cacheConfig["servers"].([]interface{}); ok {
		if len(servers) != 2 {
			t.Errorf("Cache servers length: expected 2, got %d", len(servers))
		}
	}

	// 测试空对象
	emptyObj := cfg.Obj("EMPTY_OBJ")
	if len(emptyObj) != 0 {
		t.Errorf("EmptyObj: expected length 0, got %d", len(emptyObj))
	}
}

func TestDefaultValues(t *testing.T) {
	cfg := NewConfig()

	// 测试默认值
	tests := []struct {
		name     string
		got      interface{}
		expected interface{}
	}{
		{"Str default", cfg.Str("NON_EXISTENT", "default"), "default"},
		{"Int default", cfg.Int("NON_EXISTENT", 100), 100},
		{"Int64 default", cfg.Int64("NON_EXISTENT", 999), int64(999)},
		{"Float default", cfg.Float("NON_EXISTENT", 3.14), 3.14},
		{"Bool default", cfg.Bool("NON_EXISTENT", true), true},
		{"List default", cfg.List("NON_EXISTENT"), []interface{}{}},
		{"StrList default", cfg.StrList("NON_EXISTENT"), []string{}},
		{"IntList default", cfg.IntList("NON_EXISTENT"), []int{}},
		{"Obj default", cfg.Obj("NON_EXISTENT"), map[string]interface{}{}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if !reflect.DeepEqual(tt.got, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, tt.got)
			}
		})
	}
}

func TestConfigMethods(t *testing.T) {
	cfg := NewConfig()

	// 测试Set和Get
	cfg.Set("test_key", "test_value")
	if !cfg.Has("test_key") {
		t.Error("Has() returned false for existing key")
	}

	got := cfg.Get("test_key")
	if got != "test_value" {
		t.Errorf("Get: expected test_value, got %v", got)
	}

	// 测试Get带默认值
	got = cfg.Get("non_existent", "default")
	if got != "default" {
		t.Errorf("Get with default: expected default, got %v", got)
	}

	// 测试Keys
	cfg.Set("key1", "value1")
	cfg.Set("key2", "value2")
	keys := cfg.Keys()
	if len(keys) < 2 {
		t.Errorf("Keys: expected at least 2 keys, got %d", len(keys))
	}

	// 测试All
	all := cfg.All()
	if len(all) < 3 {
		t.Errorf("All: expected at least 3 items, got %d", len(all))
	}
}

func TestNumberParsing(t *testing.T) {
	envContent := `INT_VAL=42
NEG_INT=-100
LARGE_INT=9999999999
FLOAT_VAL=3.14159
NEG_FLOAT=-0.5
`

	tmpFile, err := os.CreateTemp(".", "test*.env")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tmpFile.Name())
	defer tmpFile.Close()

	if _, err := tmpFile.WriteString(envContent); err != nil {
		t.Fatal(err)
	}
	tmpFile.Close()

	cfg := NewConfig()
	if err := cfg.LoadEnv(tmpFile.Name()); err != nil {
		t.Fatalf("LoadEnv failed: %v", err)
	}

	tests := []struct {
		key      string
		expected interface{}
	}{
		{"INT_VAL", 42},
		{"NEG_INT", -100},
		{"LARGE_INT", int64(9999999999)},
		{"FLOAT_VAL", 3.14159},
		{"NEG_FLOAT", -0.5},
	}

	for _, tt := range tests {
		t.Run(tt.key, func(t *testing.T) {
			got := cfg.Get(tt.key)
			if !reflect.DeepEqual(got, tt.expected) {
				t.Errorf("expected %v (%T), got %v (%T)", tt.expected, tt.expected, got, got)
			}
		})
	}
}

func TestBooleanParsing(t *testing.T) {
	envContent := `TRUE_VAR=true
FALSE_VAR=false
TRUE_CAPS=TRUE
FALSE_CAPS=FALSE
TRUE_MIXED=True
FALSE_MIXED=False
`

	tmpFile, err := os.CreateTemp(".", "test*.env")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tmpFile.Name())
	defer tmpFile.Close()

	if _, err := tmpFile.WriteString(envContent); err != nil {
		t.Fatal(err)
	}
	tmpFile.Close()

	cfg := NewConfig()
	if err := cfg.LoadEnv(tmpFile.Name()); err != nil {
		t.Fatalf("LoadEnv failed: %v", err)
	}

	tests := []struct {
		key      string
		expected bool
	}{
		{"TRUE_VAR", true},
		{"FALSE_VAR", false},
		{"TRUE_CAPS", true},
		{"FALSE_CAPS", false},
		{"TRUE_MIXED", true},
		{"FALSE_MIXED", false},
	}

	for _, tt := range tests {
		t.Run(tt.key, func(t *testing.T) {
			got := cfg.Bool(tt.key)
			if got != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, got)
			}
		})
	}
}

func TestErrorHandling(t *testing.T) {
	// 测试文件不存在
	err := LoadEnv("non_existent_file.env")
	if err == nil {
		t.Error("Expected error for non-existent file, got nil")
	}

	// 测试无效格式
	invalidContent := `INVALID_LINE_NO_EQUAL_SIGN
KEY=valid
ANOTHER=valid
`

	tmpFile, err := os.CreateTemp(".", "test*.env")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tmpFile.Name())
	defer tmpFile.Close()

	if _, err := tmpFile.WriteString(invalidContent); err != nil {
		t.Fatal(err)
	}
	tmpFile.Close()

	cfg := NewConfig()
	err = cfg.LoadEnv(tmpFile.Name())
	if err == nil {
		t.Error("Expected error for invalid format, got nil")
	}

	// 测试空key
	emptyKeyContent := `=value`
	tmpFile2, err := os.CreateTemp(".", "test*.env")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tmpFile2.Name())
	defer tmpFile2.Close()

	if _, err := tmpFile2.WriteString(emptyKeyContent); err != nil {
		t.Fatal(err)
	}
	tmpFile2.Close()

	err = cfg.LoadEnv(tmpFile2.Name())
	if err == nil {
		t.Error("Expected error for empty key, got nil")
	}
}

func TestTypeConversion(t *testing.T) {
	cfg := NewConfig()
	cfg.Set("test_int", 42)
	cfg.Set("test_float", 3.14)
	cfg.Set("test_string", "hello")
	cfg.Set("test_bool", true)

	// 测试类型转换
	tests := []struct {
		name     string
		got      interface{}
		expected interface{}
	}{
		{"Int to Int64", cfg.Int64("test_int"), int64(42)},
		{"Int to Float", cfg.Float("test_int"), 42.0},
		{"Float to Int", cfg.Int("test_float"), 3},
		{"String to Int", cfg.Int("test_string"), 0},
		{"String to Bool", cfg.Bool("test_string"), false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if !reflect.DeepEqual(tt.got, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, tt.got)
			}
		})
	}
}

func BenchmarkConfigGet(b *testing.B) {
	cfg := NewConfig()
	cfg.Set("bench_key", "bench_value")

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		cfg.Str("bench_key")
	}
}

func BenchmarkConfigParse(b *testing.B) {
	envContent := `APP_NAME=TestApp
PORT=8080
DEBUG=true
TIMEOUT=30.5
STR_LIST=["a", "b", "c"]
DB_CONFIG={host: "localhost", port: 5432}
`

	tmpFile, err := os.CreateTemp(".", "bench*.env")
	if err != nil {
		b.Fatal(err)
	}
	defer os.Remove(tmpFile.Name())
	defer tmpFile.Close()

	if _, err := tmpFile.WriteString(envContent); err != nil {
		b.Fatal(err)
	}
	tmpFile.Close()

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		cfg := NewConfig()
		cfg.LoadEnv(tmpFile.Name())
	}
}

// 测试并发安全（注意：当前实现不是并发安全的，这个测试会失败）
// 如果需要并发安全，需要添加互斥锁
func TestConcurrentAccess(t *testing.T) {
	cfg := NewConfig()
	cfg.Set("test_key", "test_value")

	// 并发读取
	done := make(chan bool)
	for i := 0; i < 100; i++ {
		go func() {
			_ = cfg.Str("test_key")
			done <- true
		}()
	}

	for i := 0; i < 100; i++ {
		<-done
	}
	// 如果没有panic，测试通过
}

// 测试 Duration 类型
func TestConfigDuration(t *testing.T) {
	envContent := `TIMEOUT=30
REQUEST_TIMEOUT=5.5
CACHE_TTL=300
SHUTDOWN_TIMEOUT="30s"
CONNECT_TIMEOUT="5m"
IDLE_TIMEOUT="1h30m"
COMPLEX_TIMEOUT="1h30m15s"
MS_TIMEOUT="500ms"
DURATION_LIST=[10, 30.5, "5s", "1m"]
`

	tmpFile, err := os.CreateTemp(".", "test*.env")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tmpFile.Name())
	defer tmpFile.Close()

	if _, err := tmpFile.WriteString(envContent); err != nil {
		t.Fatal(err)
	}
	tmpFile.Close()

	cfg := NewConfig()
	if err := cfg.LoadEnv(tmpFile.Name()); err != nil {
		t.Fatalf("LoadEnv failed: %v", err)
	}

	// 测试整数秒数
	timeout := cfg.Duration("TIMEOUT")
	expected := 30 * time.Second
	if timeout != expected {
		t.Errorf("TIMEOUT: expected %v, got %v", expected, timeout)
	}

	// 测试浮点秒数
	requestTimeout := cfg.Duration("REQUEST_TIMEOUT")
	expectedFloat := 5500 * time.Millisecond
	if requestTimeout != expectedFloat {
		t.Errorf("REQUEST_TIMEOUT: expected %v, got %v", expectedFloat, requestTimeout)
	}

	// 测试缓存TTL（整数）
	cacheTTL := cfg.Duration("CACHE_TTL")
	expectedTTL := 300 * time.Second
	if cacheTTL != expectedTTL {
		t.Errorf("CACHE_TTL: expected %v, got %v", expectedTTL, cacheTTL)
	}

	// 测试字符串格式 "30s"
	shutdownTimeout := cfg.Duration("SHUTDOWN_TIMEOUT")
	expectedShutdown := 30 * time.Second
	if shutdownTimeout != expectedShutdown {
		t.Errorf("SHUTDOWN_TIMEOUT: expected %v, got %v", expectedShutdown, shutdownTimeout)
	}

	// 测试 "5m"
	connectTimeout := cfg.Duration("CONNECT_TIMEOUT")
	expectedConnect := 5 * time.Minute
	if connectTimeout != expectedConnect {
		t.Errorf("CONNECT_TIMEOUT: expected %v, got %v", expectedConnect, connectTimeout)
	}

	// 测试 "1h30m"
	idleTimeout := cfg.Duration("IDLE_TIMEOUT")
	expectedIdle := 1*time.Hour + 30*time.Minute
	if idleTimeout != expectedIdle {
		t.Errorf("IDLE_TIMEOUT: expected %v, got %v", expectedIdle, idleTimeout)
	}

	// 测试 "1h30m15s"
	complexTimeout := cfg.Duration("COMPLEX_TIMEOUT")
	expectedComplex := 1*time.Hour + 30*time.Minute + 15*time.Second
	if complexTimeout != expectedComplex {
		t.Errorf("COMPLEX_TIMEOUT: expected %v, got %v", expectedComplex, complexTimeout)
	}

	// 测试毫秒
	msTimeout := cfg.Duration("MS_TIMEOUT")
	expectedMs := 500 * time.Millisecond
	if msTimeout != expectedMs {
		t.Errorf("MS_TIMEOUT: expected %v, got %v", expectedMs, msTimeout)
	}

	// 测试DurationList
	durationList := cfg.DurationList("DURATION_LIST")
	expectedList := []time.Duration{
		10 * time.Second,
		30500 * time.Millisecond,
		5 * time.Second,
		1 * time.Minute,
	}
	if len(durationList) != len(expectedList) {
		t.Errorf("DurationList length: expected %d, got %d", len(expectedList), len(durationList))
	}
	for i := range durationList {
		if durationList[i] != expectedList[i] {
			t.Errorf("DurationList[%d]: expected %v, got %v", i, expectedList[i], durationList[i])
		}
	}

	// 测试默认值
	defaultDuration := cfg.Duration("NON_EXISTENT", 10*time.Second)
	if defaultDuration != 10*time.Second {
		t.Errorf("Default duration: expected 10s, got %v", defaultDuration)
	}

	// 测试DurationDefault便捷方法
	defaultDuration2 := cfg.DurationDefault("NON_EXISTENT", 5*time.Second)
	if defaultDuration2 != 5*time.Second {
		t.Errorf("DurationDefault: expected 5s, got %v", defaultDuration2)
	}
}

// 测试 Duration 的错误处理
func TestConfigDurationErrors(t *testing.T) {
	cfg := NewConfig()

	// 设置无效的duration字符串
	cfg.Set("INVALID_DURATION", "invalid")

	// 应该返回0（默认值）
	duration := cfg.Duration("INVALID_DURATION")
	if duration != 0 {
		t.Errorf("Invalid duration should return 0, got %v", duration)
	}

	// 测试带默认值的情况
	durationWithDefault := cfg.Duration("INVALID_DURATION", 15*time.Second)
	if durationWithDefault != 15*time.Second {
		t.Errorf("Invalid duration with default should return 15s, got %v", durationWithDefault)
	}
}
