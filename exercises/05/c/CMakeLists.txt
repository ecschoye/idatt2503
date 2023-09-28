cmake_minimum_required(VERSION 3.24)
project(c C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_COMPILER "/opt/homebrew/opt/llvm/bin/clang")
set(CMAKE_CXX_COMPILER "/opt/homebrew/opt/llvm/bin/clang++")

# Add these lines
link_directories("/opt/homebrew/opt/llvm/lib")
include_directories("/opt/homebrew/opt/llvm/include")

# Main executable
add_executable(c main.c replace.c)
target_compile_options(c PRIVATE -Wall -Wextra)

# Fuzzer executable
add_executable(replace_fuzzer fuzz_main.c replace.c)
target_compile_options(replace_fuzzer PRIVATE -fsanitize=fuzzer,address)
target_link_options(replace_fuzzer PRIVATE -fsanitize=fuzzer,address)
