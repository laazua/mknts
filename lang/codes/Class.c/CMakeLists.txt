cmake_minimum_required (VERSION 3.22.1)

project(calculate)

# 正则匹配c源码文件
file(GLOB c_files "src/*.c")
# 正则匹配cc源码文件
file(GLOB cc_files "src/*.cc")

# 将源码文件赋值给source_files
#set(source_files
#	src/main.cc
#	src/calculate.cc
#	src/person.c
#)

add_executable(calculate ${c_files} ${cc_files})
