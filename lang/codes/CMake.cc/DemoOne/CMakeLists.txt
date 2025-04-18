# 所需cmake最小版本
cmake_minimum_required(VERSION 3.22.1)

# 设置工程名字
project(calc)

# 定义私有变量
#set(SRC
#    src/main.cc
#    src/calc.cc
#)

# 设置g++版本(也可对其他内置宏进行设置)
set(DCMAKE_CXX_STANDARD 11)

# 设置输出的可执行文件的路径
set(EXECUTABLE_OUTPUT_PATH ../bin)

# 文件搜索
# GLOB: 
#  将指定目录下搜索到的满足条件的所有文件名生成一个列表，并将其存储到变量中
# GLOB_RECURSE: 
#  递归搜索指定目录，将搜索到的满足条件的文件名生成一个列表，并将其存储到变量中
file(GLOB SRC ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cc)

# 文件搜索
#aux_source_directory(src SRC)

# 生成可执行程序
add_executable(calc ${SRC})
