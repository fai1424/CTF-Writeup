import binascii
from base64 import b64encode, b64decode
from Cryptodome.Util.number import long_to_bytes, bytes_to_long


def HexToBase64(a):
    return b64encode(bytes.fromhex(a)).decode()


def xor(a, b):
    a = bytes_to_long(bytes.fromhex(a))
    b = bytes_to_long(bytes.fromhex(b))
    c = a ^ b
    return bytes.hex(long_to_bytes(c))


a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"
print(bytes.fromhex('b'))

print(xor(a, b))
c = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
print(xor(c, "a"))
