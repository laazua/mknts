### 依赖注入

*说明*
```
Consumer 结构体依赖于 Service 接口，
并通过 NewConsumer 函数来进行依赖注入。
这种方式使得 Consumer 结构体可以轻松地与不同的 Service 实现交互，
从而实现了依赖注入的灵活性和可测试性
```
