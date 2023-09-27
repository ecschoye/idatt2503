# Running x86 Assembly Code on Non-x86 Platforms Using Docker

## Introduction

This project provides a Docker-based solution for running x86 assembly code on non-x86 platforms, such as ARM-based MacBooks. It leverages Docker's ability to emulate different architectures, allowing you to bypass hardware limitations for running x86-specific code.

## Prerequisites

- Docker
  
- Docker Compose

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/ecschoye/idatt2503.git
    ```

2. Navigate to the project directory:

    ```bash
    cd exercises/04/qemu_assembly/
    ```

3. Build the Docker image and start the container:

    ```bash
    docker-compose up --build -d
    ```

4. Access the container's bash shell:

    ```bash
    docker-compose run x86-asm-env bash
    ```

    You should now be inside the `/workspace` directory of the Docker container.

## Usage

1. To compile your x86 assembly code, navigate to where your `.s` files are stored and use the following commands:

    ```bash
    nasm -f elf64 hello.s
    ld hello.o -o hello
    ```

2. To run your compiled code:

    ```bash
    ./hello
    ```

## Persistence

Using Docker volumes, any changes made in the `/workspace` folder within the Docker container will be synchronized with the `./workspace` folder on your host machine.

## Cleanup

To stop and remove the running container, navigate to the project directory and run:

```bash
docker-compose down
```
