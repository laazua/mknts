#!/bin/bash

set -e
## 构建项目

export CGO_ENABLED=0
export GOOS=linux 
export GOARCH=amd64

if [ "$1" == "release" ];then
    echo "Building spoved-host..."
    cd spoved-host && go build -mod=readonly -trimpath -ldflags "-s -w" -o ../bin/hostspoved .

    echo "Building spoved-k8s..."
    cd ../spoved-k8s && go build -mod=readonly -trimpath -ldflags "-s -w" -o ../bin/k8sspoved .

    echo "Building spoved-user..."
    cd ../spoved-user && go build -mod=readonly -trimpath -ldflags "-s -w" -o ../bin/userspoved .

    echo "Upx compressing binaries..."
    upx --lzma --best ../bin/hostspoved ../bin/k8sspoved ../bin/userspoved

    exit
fi

# echo "Building spoved-host..."
# cd spoved-host && go build -o ../bin/hostspoved .

# echo "Building spoved-k8s..."
# cd ../spoved-k8s && go build -o ../bin/k8sspoved .

echo "Building spoved-user..."
cd spoved-user && go build -o ../bin/userspoved .