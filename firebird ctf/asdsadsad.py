from pwn import *


for i in range(1000000000000000):
    p = remote("ash-chal.firebird.sh", 36015)
    print(p.recvline())
    p.sendline(b'149490402558130')
    a = p.recvline().decode()
    if ("firebird" in a):
        print(a)

        break
    print(a)
    p.close()
