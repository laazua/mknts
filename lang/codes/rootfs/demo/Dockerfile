FROM docker.io/golang:1.23 AS builder

WORKDIR /app

COPY . .

RUN go build -o demo

FROM gcr.io/distroless/base-debian10

WORKDIR /app

# 从构建阶段复制可执行文件到当前阶段
COPY --from=builder /app/demo .

CMD ["./demo"]
