## 构建项目

.PHONY: clean, build

bin := show

# 设置静态编译
CLIB_ENABLE := $(go env CGO_ENABLED)
ifeq ($(CLIB_ENABLE),1)
	go env -w CGO_ENABLED=0
endif

build:
	go build -C cmd -trimpath -ldflags="-s -w " -o $(bin)

clean:
	rm -fr cmd/$(bin)