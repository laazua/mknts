### dddsshow

- **说明**
1. go项目工程实践


- **项目结构**
```
dddsshow/
├── cmd                              # 启动层：程序入口，初始化依赖、路由和服务
│   ├── grpc-server
│   │   └── main.go                  # gRPC 服务入口，注入 application 服务，注册 gRPC handler
│   └── http-server
│       └── main.go                  # HTTP 服务入口，注入 application 服务，注册 HTTP handler
├── go.mod
├── internal
│   ├── application                 # 应用层 / 用例层：编排业务逻辑，调用 domain 接口
│   │   ├── task                     # Task 相关用例服务
│   │   └── user                     # User 相关用例服务
│   ├── domain                      # 领域层：核心业务模型、领域服务、领域事件、Repository 接口
│   │   ├── task                     # Task 聚合根、实体、事件、领域服务、Repository接口
│   │   └── user
│   │       ├── entity.go            # User 实体 / 聚合根
│   │       ├── event.go             # 领域事件
│   │       ├── repository.go        # Repository 接口（抽象存储行为）
│   │       └── service.go           # 领域服务，封装跨实体业务逻辑
│   ├── infrastructure              # 基础设施层：技术实现，提供 Repository 接口实现及其他基础资源
│   │   ├── cache
│   │   │   ├── task.go              # Task 相关缓存实现
│   │   │   └── user.go              # User 相关缓存实现
│   │   ├── db                        # 数据库连接池 / ORM 初始化
│   │   ├── mq
│   │   │   ├── task.go              # Task 相关消息队列实现
│   │   │   └── user.go              # User 相关消息队列实现
│   │   └── persistence
│   │       ├── task.go              # Task Repository 实现（DAO）
│   │       └── user.go              # User Repository 实现（DAO）
│   └── interface                    # 接口层：对外接口实现，DTO/Mapper/Handler
│       ├── grpc
│       │   ├── dto                   # gRPC 请求/响应 DTO
│       │   ├── mapper                # DTO <-> Domain Entity 转换工具
│       │   ├── task.go               # Task gRPC handler
│       │   └── user.go               # User gRPC handler
│       └── http
│           ├── dto                   # HTTP 请求/响应 DTO
│           ├── mapper                # DTO <-> Domain Entity 转换工具
│           ├── task.go               # Task HTTP handler
│           └── user.go               # User HTTP handler
├── pkg                               # 公共库 / 工具函数 / 跨模块可复用代码
├── proto                             # gRPC proto 文件定义
│   ├── task.proto
│   └── user.proto
└── README.md
```

- **项目结构说明**

```
1. cmd/（启动层）
    职责：
        启动服务程序：HTTP 或 gRPC
        初始化依赖注入（DI）、路由、日志、配置
    关键任务：
        构建 application 层 service 并注入 Repository 实现
        注册 handler（HTTP/gRPC）
    依赖：
        调用 internal/interface 注册接口
        调用 internal/application 构建服务

2. internal/domain/（领域层）
    职责：
        核心业务模型（Entity、聚合根）
        领域事件（Event）
        领域服务（Domain Service）实现业务逻辑
        Repository 接口（抽象存储，不依赖 DB）
    关键文件：
        entity.go → 定义聚合根和实体属性
        service.go → 领域服务，封装跨实体逻辑
        event.go → 领域事件
        repository.go → Repository 接口
    依赖：
        不依赖任何外部库或infrastructure
        被 application 层调用

3. internal/application/（应用层/用例层）
    职责：
        编排业务用例
        调用 Domain 层 Entity、Service 和 Repository 接口
        处理跨聚合逻辑
    关键任务：
        组合多个 Domain Service 或 Repository 进行操作
        转换外部请求（DTO）到 Domain Entity（可调用 Mapper）
    依赖：
        依赖 domain 层接口和实体
        不依赖 infrastructure 或 interface

4. internal/infrastructure/（基础设施层）
    职责：
        提供技术实现（数据库、缓存、消息队列）
        实现 domain Repository 接口（DAO）
    子模块说明：
        db/ → 数据库连接池，ORM 初始化
        cache/ → Redis 或本地缓存
        mq/ → 消息队列实现
        persistence/ → Repository 实现（DAO）
    依赖：
        可以依赖 domain 接口
        不依赖 application 或 interface

5. internal/interface/（接口层）
    职责：
        提供 HTTP / gRPC 对外接口
        接收请求 DTO → Mapper → Application Service → Domain → Repository → 返回 DTO
    子模块：
        dto/ → 请求和响应结构体
        mapper/ → DTO ↔ Domain Entity 转换
        task.go/user.go → Handler 注册和处理
    依赖：
        调用 application 层 service
        使用 mapper 转换数据
        不直接依赖 domain 或 infrastructure 实现

6. pkg/（公共库）
    职责：
        公共工具、日志、辅助函数等
    依赖：
        可被任意层使用，但不要让 domain 或 application 依赖 infrastructure

7. proto/
    gRPC 接口文件
    生成 DTO / gRPC 接口代码，可配合 interface 层使用
```

- **请求逻辑**
```
客户端 HTTP Request / gRPC Request
        │
        ▼
[DTO: CreateUserRequest]  <- interface/dto
        │
        ▼
[Mapper]  DTO -> Domain Entity <- interface/mapper
        │
        ▼
[Application Service]  <- internal/application/user/service.go
        │
        ▼
[Domain Entity + Domain Service]  <- internal/domain/user
        │
        ▼
[Repository Interface] <- domain/repository.go
        │
        ▼
[Persistence/DAO 实现] <- infrastructure/persistence/user.go
        │
        ▼
[Database / Cache / MQ] <- infrastructure/db/cache/mq
        │
        ▼
[Domain Entity] 返回
        │
        ▼
[Application Service] 返回
        │
        ▼
[Mapper] Domain Entity -> DTO <- interface/mapper
        │
        ▼
[DTO: CreateUserResponse] 返回给客户端

```