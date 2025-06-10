## 编译
.PHONY: clean build vetfix

TARGET := dpsup
CLIB_ENABLE := $(go env CGO_ENABLED)
ifeq ($(CLIB_ENABLE),1)
	go env -w CGO_ENABLED=0
endif

build:
	go build -ldflags="-w -s" -trimpath -o $(TARGET)

vetfix:
	go vet ./...
	go fix ./...

clean:
	rm -f $(TARGET)
