# Use an x86 base image
FROM amd64/ubuntu:latest

# Set environment to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=noninteractive

# Install essential packages
RUN apt-get update \
    && apt-get install -y \
    gcc \
    gdb \
    python3 \
    python3-pip \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/pwndbg/pwndbg.git \
    && cd pwndbg \
    && ./setup.sh