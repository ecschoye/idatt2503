cmake_minimum_required(VERSION 3.24)
project(01)

set(CMAKE_CXX_STANDARD 17)

if(APPLE)
    if(EXISTS /opt/homebrew/opt/openssl)
        set(OPENSSL_ROOT_DIR /opt/homebrew/opt/openssl)
        set(OPENSSL_LIBRARIES ${OPENSSL_ROOT_DIR}/lib)
        set(OPENSSL_INCLUDE_DIR ${OPENSSL_ROOT_DIR}/include)
        set(OPENSSL_CRYPTO_LIBRARY ${OPENSSL_ROOT_DIR}/lib/libcrypto.dylib)
    endif()
endif()

find_package(OpenSSL REQUIRED)
include_directories(${OPENSSL_INCLUDE_DIR})

add_executable(01 main.cpp)
target_link_libraries(01 ${OPENSSL_CRYPTO_LIBRARY})
