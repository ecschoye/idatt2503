# Use an official base image
FROM ubuntu:latest

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=non-interactive

# Install necessary packages and add Kitware repository for latest CMake
RUN apt-get update && \
    apt-get install -y wget software-properties-common lsb-release gnupg && \
    wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor -o /usr/share/keyrings/kitware-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu/ $(lsb_release -cs) main" > /etc/apt/sources.list.d/kitware.list && \
    apt-get update && \
    apt-get -y install clang cmake make git

# Copy the entire project
COPY . /app

# Set working directory
WORKDIR /app

# Build the project
RUN mkdir build && cd build && \
    CC=clang cmake .. && \
    make

# Command to keep the container running
CMD ["bash"]
