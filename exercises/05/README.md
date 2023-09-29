# Fuzzing Exercise for IDATT2503

## Overview
This repository contains code for a fuzzing exercise in the IDATT2503 course at NTNU, Trondheim. The code includes a C program that replaces special characters in a string (`&`, `<`, `>`), a fuzzer to test this program, and a Continuous Integration (CI) setup.

 ![C CI Fuzzing with Address Sanitizer](https://github.com/ecschoye/idatt2503/actions/workflows/c_fuzzing.yml/badge.svg)

## File Structure
- `main.c`: Main program to test the `replaceSpecialCharacters` function.
- `replace.c` / `replace.h`: Contains the `replaceSpecialCharacters` function.
- `CMakeLists.txt`: CMake build configuration.
- `tests/replace_fuzzer_test.c`: Contains the LLVM fuzzer test.
- `tests/replace_test.c`: Contains the unit tests.
- `tests/CMakeLists.txt`: CMake build configuration for tests.
- `c_fuzzing.yml`: GitHub Actions CI configuration.

## Build and Run

### Building Main Program
```bash
mkdir build
cd build
CC=clang cmake ..
make
```

Run the main program:

```bash
./build/c
```

### Building and Running the Fuzzer
```bash
mkdir build
cd build
CC=clang cmake ..
make
```

Run the fuzzer:

```bash
./build/tests/replace_fuzzer_test -max_total_time=60
```

Run tests:

```bash
./build/tests/replace_test
```

### Continuous Integration
The repository is configured to use GitHub Actions for CI. The workflow runs fuzzing tests with Address Sanitizer enabled.


## Using Address Sanitizer
Address Sanitizer is enabled by adding the `-fsanitize=address` flag in the `CMakeLists.txt` and during CI.
