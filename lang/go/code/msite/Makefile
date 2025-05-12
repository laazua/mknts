# 项目打包

.PHONY: build
build:
	@go build -C cmd/main/ \
		-ldflags='-s -w' \
		-o ../../msite

.PHONY: clean
clean:
	rm -f msite

.PHONY: test
test:
	go test -v ./...