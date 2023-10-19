# Exercise 6: Password Cracking and Authentication

## Overview
This repository contains two main tasks:

1. **Task 1: Password Cracking** - Given a hash and salt, your mission is to figure out the original password.
2. **Task 2: Web Client and Server Authentication** - Create a simple web application where a client authenticates against a server using PBKDF2.

## Pre-requisites

- OpenSSL library for Task 1
- Node.js for Task 2 (optional)
- Knowledge of PBKDF2 and SHA1 algorithms

---

## Task 1: Password Cracking

### Objective
You are provided with a hashed password and its salt. Your job is to find the original password. The hash algorithm used is PBKDF2 with SHA1.

### Information

- **Hash (Key):** `ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6`
- **Salt:** `Saltet til Ola`
- **Iterations:** `2048`

### Steps

1. Clone the [ntnu-tdat3020/openssl-example](https://gitlab.com/ntnu-tdat3020/openssl-example) repository.
2. Implement your password-cracking logic by iterating over possible passwords and using PBKDF2 with SHA1 to hash them.
3. Compare the generated hash with the given hash to identify the original password.

---

## Task 2: Web Client and Server Authentication

### Objective
Build a web client and server where the client authenticates against the server using PBKDF2.

### Technology Stack

- Use JavaScript on both client and server sides.
- Optional: Use Node.js Crypto (openssl bindings) for the server-side hashing.

### Steps

1. Set up a basic web server and client using your preferred framework.
2. Implement PBKDF2 hashing in both the client and server to secure password transmissions.
3. Once authenticated, issue an access token to the client for subsequent requests.

#### Optional
Design your access token as per your preference. Assume HTTPS is used, allowing you to use simple access/bearer tokens.
