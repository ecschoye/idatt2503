# Task 2 Give a brief comparison of MACs and digital signatures, with respect to purpose, use cases, type of encryption, etc.

### MAC

Purpose 
- Ensure data integrity and authenticity of a message
- Verify that the message has not been tampered with
- Verify that the message is from the sender

Use cases
- MACs are used in different protocols, such as TLS and SSH, and many more.
- Used in storage of data to ensure that the data has not been tampered with

Type of encryption
- Symmetric encryption. Same key is used for encryption and decryption.


### Digital Signatures

Purpose
- Ensure data integrity, authenticity and non-repudiation of a message
- Verify that the message has not been tampered with
- Verify that the message is from the sender
- Prevent the sender from denying that they sent the message

Use cases
- Used in document signing
- Used in legal documents where non-repudiation is important

Type of encryption
- Asymmetric encryption. Sender signs with their private key, and recipient verifies with the sender's public key.


# Task 3

## Task 3.1 Name the two parts/ layers of TLS 1.3, and what their purposes are.

### TLS Handshake Protocol

Purpose
- Establish a shared secret key between the client and the server
- Authenticate of the server and optionally the client
- Session key information exchange

### TLS Record Protocol

Purpose
- Divide the data into manageable blocks
- Compression of the outgoing blocks and decompression of the incoming blocks
- Apply MAC to the outgoing blocks and verify the MAC of the incoming blocks
- Encrypt the outgoing blocks and decrypt the incoming blocks
-

## Task 3.2 Explain how TLS uses both symmetric and asymmetric cryptography.

Asymmetric encryption is utilized to set up a secure connection between the client and the server. They exchange their public keys and use them to encrypt the data.

Symmetric encryption is used to encrypt the data. The symmetric key is generated during the handshake, and is used to encrypt the data.
The symmetric key is encrypted with the public key of the recipient, and sent to the recipient. The recipient can then decrypt the symmetric key with their private key, and use the symmetric key to decrypt the data.

# Task 4

## Task 4.1 What are the two main types of password attacks?

The two main types of password attacks are:
- Brute force attack
- Dictionary attack

## Task 4.2 Why should password not be stored encrypted?

The password should not be stored encrypted because then the password can be decrypted. If the password is stored hashed, it is much harder to find the password.

## Task 4.3 What is the advantage to use a specialized password algorithms over general cryptographic hash functions using a salt?

The advantage is that the specialized password algorithm is designed to be slow. This makes it harder for an attacker to brute force the password.