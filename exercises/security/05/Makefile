# Variables
CC=clang
CMAKE=cmake
BUILD_DIR=build

# Targets
all: build-main build-fuzzer build-tests

# Build the main program
build-main:
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) && CC=$(CC) $(CMAKE) .. && make

# Build and run the fuzzer
build-fuzzer:
	cd $(BUILD_DIR) && make
	$(BUILD_DIR)/tests/replace_fuzzer_test -max_total_time=60

# Build and run the unit tests
build-tests:
	cd $(BUILD_DIR) && make
	$(BUILD_DIR)/tests/replace_test

# Docker Compose Commands
up:
	docker-compose up -d

down:
	docker-compose down

compose-build:
	docker-compose build

logs:
	docker-compose logs -f

bash:
	docker-compose exec fuzzing-exercise bash

# Docker commands for convenience
docker-build:
	docker build -t idatt2503-fuzzing-exercise .

docker-run:
	docker run -it idatt2503-fuzzing-exercise

.PHONY: all build-main build-fuzzer build-tests up down compose-build logs bash docker-build docker-run
