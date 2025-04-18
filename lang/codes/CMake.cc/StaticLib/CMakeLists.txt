cmake_minimum_required(VERSION 3.22.1)

project(calc)

# 添加头文件
include_directories(${PROJECT_SOURCE_DIR}/include)

file(GLOB SRC "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cc")

# 设置静态库输出位置
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

# 生成静态库
add_library(calc STATIC ${SRC})

