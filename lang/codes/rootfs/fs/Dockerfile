## 多阶段构建

# 这里是构建应用
FROM someImage AS build

# ...


# 这里是生成最终镜像
FROM gcr.io/distroless/python3

COPY --from=build 
