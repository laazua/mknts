### LayerShow


- **说明**

```txt
layershow/
├── cmd/         # 入口 (main.go)
├── internal/    # 内部业务逻辑
│   ├── api/     # http handler 层
│   ├── dao/     # 数据访问实现
│   ├── dto/     # 请求/响应 DTO
│   ├── mapper/  # DTO <-> Model 转换
│   ├── model/   # 持久化实体
│   └── service/ # 业务逻辑
├── pkg/         # 公共工具包
```

- **依赖流程图**
```txt
                ┌───────────┐
                │   cmd/    │   (应用入口，组装依赖)
                └─────┬─────┘
                      │
                      ▼
                ┌───────────┐
                │   api/    │   (HTTP Handler 层)
                └─────┬─────┘
                      │
                      ▼
                ┌───────────┐
                │ service/  │   (业务逻辑层)
                └─────┬─────┘
          ┌───────────┼───────────┐
          │                       │
          ▼                       ▼
    ┌───────────┐          ┌───────────┐
    │   dao/    │          │ mapper/   │   (DTO ↔ Model 转换)
    └─────┬─────┘          └─────┬─────┘
          │                       │
          ▼                       ▼
    ┌───────────┐          ┌───────────┐
    │  model/   │          │   dto/    │
    └───────────┘          └───────────┘

```

- **依赖说明**

```txt
cmd/
  依赖 api/、service/、dao/，用来组装依赖并启动应用

api/
  依赖 service/（调用业务逻辑）
  使用 dto/ 作为输入/输出

service/
  依赖 dao/（持久化访问）
  依赖 mapper/（DTO ↔ Model 转换）

dao/
  依赖 model/（数据库实体）

mapper/
  依赖 dto/ 和 model/（做结构转换）

model/
  仅包含数据库结构体，不依赖其他层

dto/
  仅包含请求/响应对象，不依赖其他层
```