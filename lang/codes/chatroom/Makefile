############################## 项目打包 ##################################
# 静态链接参数(不建议): -a -ldflags '-linkmode external -extldflags "-static"', 要求编译环境和运行环境一致

SERVER := chatroom
CLIENT := chatclient

# make
build:
	go build -o $(SERVER) cmd/server/main.go
	go build -o $(CLIENT) cmd/client/main.go

# run: make clean
clean:
	rm -fr $(SERVER) $(CLIENT)

.PHONY: all clean
