cmake_minimum_required(VERSION 3.24)
project(c C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11 -Wall -Wextra")

add_library(replace STATIC replace.c)
target_include_directories(replace INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(c main.c replace.c)
target_link_libraries(c replace)

enable_testing()
add_subdirectory(tests)
