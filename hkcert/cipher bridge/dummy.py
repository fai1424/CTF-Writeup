import signal
import base64
import os
from gmpy2 import is_prime
from Cryptodome.Cipher import AES as _AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Util.number import long_to_bytes, bytes_to_long
import sys


class AES:
    def __init__(self):
        self.key = os.urandom(16)

    def encrypt(self, m: bytes) -> bytes:
        iv = os.urandom(16)
        cipher = _AES.new(self.key, _AES.MODE_CBC, iv=iv)
        return iv + cipher.encrypt((m))

    def decrypt(self, c: bytes) -> bytes:
        iv, c = c[:16], c[16:]
        cipher = _AES.new(self.key, _AES.MODE_CBC, iv=iv)
        return unpad(cipher.decrypt(c), 16)


aes = AES()
c0 = aes.encrypt(b"1234567812345678")

print(len(c0))
