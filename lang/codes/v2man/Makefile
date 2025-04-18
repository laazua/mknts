# 项目打包
# cat nodes.json | base64 -w 0 > subscription.txt

ENV := dev

ifeq ($(ENV), dev)
	BUILD_FLAGS = -race
endif

ifeq ($(ENV), pro)
	LDFLAGS = -w
endif

all: lint build

build:
	go build -C cmd/server -v -ldflags '$(LDFLAGS)' $(BUILD_FLAGS) -gcflags=all="-N -l" -o ../../v2man
	@upx --best v2man

lint:
	go fmt ./...
	go vet ./...
	# goimports -w .
	# golangci-lint run ./...

# cover:
# 	go test ./... -v -short -coverprofile .coverage.txt
#	go tool cover -func .coverage.txt

clean:
	rm -f v2man || true

help:
	@echo "make build          - 编译项目源码[dev]"
	@echo "make build ENV=pro  - 编译项目源码[pro]"
	@echo "make clean          - 清理编译文件"
	@echo "make lint           - 格式化项目代码"

.PHONY: clean help
