cmake_minimum_required(VERSION 3.14)
project(GreeterServer)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 指定查找路径
list(APPEND CMAKE_PREFIX_PATH /usr/local)
set(Protobuf_USE_STATIC_LIBS ON)  # 使用静态库
set(gRPC_USE_STATIC_LIBS ON)      # 使用静态库

# 首先查找 protobuf
find_package(Protobuf REQUIRED CONFIG)

# 然后查找 gRPC
find_package(gRPC REQUIRED CONFIG)

# 公共的 protobuf 生成文件
set(PROTO_SRCS
    protos/apis/helloworld.pb.cc
    protos/apis/helloworld.grpc.pb.cc
)

# 根据命令行宏决定编译哪个目标
if(BUILD_SERVER)
    message(STATUS "Building SERVER")
    add_executable(server
        server.cc
        ${PROTO_SRCS}
    )
    target_include_directories(server PRIVATE
        protos/apis
        ${Protobuf_INCLUDE_DIRS}
    )
    target_link_libraries(server
        gRPC::grpc++
        gRPC::grpc++_reflection
        protobuf::libprotobuf
        Threads::Threads
    )
endif()

if(BUILD_CLIENT)
    message(STATUS "Building CLIENT")
    add_executable(client
        client.cc
        ${PROTO_SRCS}
    )
    target_include_directories(client PRIVATE
        protos/apis
        ${Protobuf_INCLUDE_DIRS}
    )
    target_link_libraries(client
        gRPC::grpc++
        gRPC::grpc++_reflection
        protobuf::libprotobuf
        Threads::Threads
    )
endif()

# 如果既没有指定 BUILD_SERVER 也没有指定 BUILD_CLIENT，报错
if(NOT BUILD_SERVER AND NOT BUILD_CLIENT)
    message(FATAL_ERROR "Please specify -DBUILD_SERVER=ON or -DBUILD_CLIENT=ON")
endif()
