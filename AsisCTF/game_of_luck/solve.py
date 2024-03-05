from pwn import *
from Cryptodome.Util.number import *

i = 1
while True:
    r = remote('65.109.182.44', 5000)
    print(r.readline())
    print(r.readline())

    print(r.readline())
    print(r.readline())
    print(r.readline())
    print(r.readline())
    r.sendline(b'1')
    print(r.readline())
    r.sendline(b'1')
    see = r.readline()
    print(see)
    if (see == b'Enter your guess: You lost :(\n'):
        i += 1
        r.close()
        continue
    else:
        print("correct")
        print(i)
        print(r.readline())
        print(r.readline())
        print(r.readline())

        break
