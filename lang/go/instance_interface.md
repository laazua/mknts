###

- 检查类型是否实现了某个接口: _ = 接口(类型实例):
```golang
var buffer bytes.Buffer

_ = io.Reader(&buffer)
```
