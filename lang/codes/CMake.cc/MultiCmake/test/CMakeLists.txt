cmake_minimum_required(VERSION 3.22.1)


include_directories(${HEAD_PATH})

file(GLOB SRC "${CMAKE_CURRENT_SOURCE_DIR}/*.cc")

target_link_libraries(${APP_NAME} ${CALC_NAME} ${SORT_NAME})

add_executable(${APP_NAME} ${SRC})
