cmake_minimum_required(VERSION 3.22.1)

project(calc)

# 搜索指定目录下源文件
file(GLOB SRC ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cc)

# 包含头文件路径
include_directories(${PROJECT_SOURCE_DIR}/include)

if (STATIC)

  message(STATUS "加载静态库")
  # 包含静态库路径
  link_directories(${PROJECT_SOURCE_DIR}/lib)

  # 链接静态库
  #link_libraries(calc)

endif()

if (SHARED)

  message(STATUS "加载动态库")
  # 链接动态库
  target_link_libraries(app calc)

endif()

add_executable(app ${SRC})
