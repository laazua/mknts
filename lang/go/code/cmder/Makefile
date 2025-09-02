# 项目打包

agent := cmd-agent
proxy := cmd-proxy

.PHONY: clean, build, agent, proxy

# 设置静态编译
CLIB_ENABLE := $(go env CGO_ENABLED)
ifeq ($(CLIB_ENABLE),1)
	go env -w CGO_ENABLED=0
endif

build:
	go build -C cmd/agent -o $(agent)
	go build -C cmd/proxy -o $(proxy)

	@ [ ! -d bin ] && mkdir -p bin/agent && \
	  mkdir -p bin/proxy && \
	  cp cmd/agent/$(agent) bin/agent/$(agent) && \
	  cp cmd/proxy/$(proxy) bin/proxy/$(proxy) && \
	  cp docs/agent.yaml bin/agent/config.yaml && \
	  cp docs/proxy.yaml bin/proxy/config.yaml

agent:
	cd bin/agent && ./$(agent)

proxy:
	cd bin/proxy && ./$(proxy)

clean:
	rm -f cmd/agent/cmd-agent
	rm -f cmd/proxy/cmd-proxy
	rm -rf bin
