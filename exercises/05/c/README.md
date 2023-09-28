Split main.c into main.c, replace.c/ replace.h and fuzz_main.c

also made this Cmakelistxt file 

cmake_minimum_required(VERSION 3.24)
project(c C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11 -Wall -Wextra")

# Main executable
add_executable(c main.c replace.c)
target_compile_options(c PRIVATE -Wall -Wextra)

# Fuzzer executable
add_executable(replace_fuzzer fuzz_main.c replace.c)
target_compile_options(replace_fuzzer PRIVATE -fsanitize=fuzzer,address)
target_link_options(replace_fuzzer PRIVATE -fsanitize=fuzzer,address)

