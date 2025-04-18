cmake_minimum_required(VERSION 3.22.1)

project(calc)

set(LIB_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib)
# 头文件目录
set(HEAD_PATH ${CMAKE_CURRENT_SOURCE_DIR}/include)

set(APP_NAME app)
set(CALC_NAME calc)
set(SORT_NAME sort)

# 添加子目录
add_subdirectory(src)
add_subdirectory(test)

