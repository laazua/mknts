# 添加子目录
add_subdirectory(sort)

cmake_minimum_required(VERSION 3.22.1)

project(${CALC_NAME})

# 添加头文件
include_directories(${HEAD_PATH})

file(GLOB SRC "${CMAKE_CURRENT_SOURCE_DIR}/*.cc")

# 设置动态库输出位置
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

# 生成动态库
add_library(${CALC_NAME} SHARED ${SRC})

