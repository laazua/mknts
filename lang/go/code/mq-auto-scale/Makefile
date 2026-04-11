
target := mqAutoScale

build:
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 \
	go build  -C cmd/mq-auto-scale -mod=readonly -trimpath -ldflags "-s -w" -o ../../$(target)

clean:
	rm -f $(target)