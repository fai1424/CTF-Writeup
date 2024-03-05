import signal
from gmpy2 import is_prime
import os
import sys


def generate_prime():
    while True:
        p = int.from_bytes(os.urandom(1024//8), 'big')
        if p % 0x10001 == 1:
            continue
        if p.bit_length() != 1024:
            continue
        if not is_prime(p):
            continue
        return p


p = generate_prime()
print(len(str(p)))
print(p)
