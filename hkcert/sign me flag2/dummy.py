import hmac
import hashlib
from pwn import *
import itertools
from Cryptodome.Util.number import bytes_to_long


def sign_message(id: int, key_client: bytes, key_server: bytes, message: str) -> bytes:
    key_combined = xor(key_client, key_server)
    full_message = f'{id}{message}'.encode()

    signature = hmac.new(key_combined, full_message, hashlib.sha256).digest()
    return signature


def sign(r, key_client: bytes, message: str):
    r.sendlineafter('🎬 '.encode(), b'sign')
    r.sendlineafter('🔑 '.encode(), key_client.hex().encode())
    r.sendlineafter('💬 '.encode(), message.encode())
    r.recvuntil('📝 '.encode())
    return bytes.fromhex(r.recvline().decode().strip())


# print(xor(b'00000000', b'12345678'))

# print(xor(b'0000000000000000', b'1234567812345678'))
# print(xor(b'000000000000000000', b'1234567812345678'))

# print(bytes.hex(sign_message(0, b'0000000000000000', b'1234567812345678', "0")))
# print(bytes.hex(sign_message(0, b'0000000000000000', b'1234567812345678', "0t")))
# print(bytes.hex(sign_message(0, b'0000000000000000', b'1234567812345678', "0te")))
# print(bytes.hex(sign_message(0, b'0000000000000000', b'1234567812345678', "0tes")))
# print(bytes.hex(sign_message(0, b'0000000000000000', b'1234567812345678', "0test")))
# print(bytes.hex(sign_message(0, b'0000000000000000', b'1234567812345678', "0testi")))
# print(bytes.hex(sign_message(0, b'0000000000000000', b'1234567812345678', "0testin")))
# print(bytes.hex(sign_message(0, b'0000000000000000', b'1234567812345678', "0testing")))
print(bytes.hex(sign_message(0, b'00000000',
      b'12345678', "gib flag pls")))


# print(bytes.hex(sign_message(
#     0, b'00000000000000000000000000000000', b'11111111', "testing")))

# print(sign_message(0, b'00000000', b'12345678', ""))
