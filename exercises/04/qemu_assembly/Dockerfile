# Using an x86 Ubuntu base image
FROM --platform=linux/amd64 ubuntu:latest

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=non-interactive

# Install packages required for assembly programming
RUN apt-get update && \
    apt-get install -y nasm gcc binutils && \
    apt-get clean

# Set the working directory
WORKDIR /workspace

# Default command
CMD [ "bash" ]
