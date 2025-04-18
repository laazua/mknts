cmake_minimum_required(VERSION 3.22.1)

project(calc)

set(CMAKE_CXX_STANDARD 11)

set(EXECUTABLE_OUTPUT_PATH ../bin)

# 添加头文件
include_directories(${PROJECT_SOURCE_DIR}/include)

file(GLOB SRC ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cc)

add_executable(calc  ${SRC})
