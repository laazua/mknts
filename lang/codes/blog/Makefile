bin := mblog

.PHONY: clean, vendor, build

build:
	go build -C main -mod=vendor -o ../$(bin)

vendor:
	go work vendor

clean:
	rm -fr $(bin)
