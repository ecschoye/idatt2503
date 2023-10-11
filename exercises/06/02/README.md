# Web Client and Server with PBKDF2 Authentication

## Introduction
This project aims to create a web client and server that utilize PBKDF2 for password hashing and authentication. Both the client and server-side will hash the password. The server is optionally implemented using Node.js and can utilize openssl bindings through Node.js Crypto.

## Prerequisites

- Node.js and npm OR Bun

## Getting Started

First, clone the repository and navigate into the project directory.

### Installation

To install the required packages, use the following command:

```bash
make install
```

This will automatically check for either Bun or npm on your system and use it to install dependencies.

### Running the Application

To run the application, use the following command:

```bash
make run
```

This will run both the client and server.

## Makefile Explained

The Makefile includes two main targets: `install` and `run`.

- `install`: Installs the required dependencies. It checks for the presence of Bun or npm and uses whichever is found.
- `run`: Runs the application after installing dependencies. Similar to the install command, it uses either Bun or npm based on availability.

## Technologies Used

- JavaScript
- PBKDF2 for password hashing
- Node.js Crypto (optional)
