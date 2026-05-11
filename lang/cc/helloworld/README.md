### helloworld

##### 生成grpc代码
```bash
cd protps
protoc -I ./ --grpc_out=./apis/ --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` ./helloworld.proto
protoc -I ./ --cpp_out=./apis/ ./helloworld.proto
```

##### 编译项目
```bash
mkdir build && cd build
cmake -DBUILD_CLIENT=ON .. && make
cmake -DBUILD_SERVER=ON .. && make
```
