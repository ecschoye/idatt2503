add_executable(replace_test replace_test.c)
target_link_libraries(replace_test replace)
target_compile_options(replace_test PRIVATE -fsanitize=address)
target_link_options(replace_test PRIVATE -fsanitize=address)
add_test(NAME replace_test COMMAND replace_test)

add_executable(replace_fuzzer_test replace_fuzzer_test.c)
target_link_libraries(replace_fuzzer_test replace)
target_compile_options(replace_fuzzer_test PRIVATE -fsanitize=fuzzer,address)
target_link_options(replace_fuzzer_test PRIVATE -fsanitize=fuzzer,address)
