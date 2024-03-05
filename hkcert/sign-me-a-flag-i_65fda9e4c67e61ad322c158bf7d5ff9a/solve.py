import hmac
import hashlib
from pwn import *
import itertools
from Cryptodome.Util.number import bytes_to_long


def sign_message(key_client: bytes, key_server: bytes, message: str) -> bytes:
    key_combined = xor(key_client, key_server)

    signature = hmac.new(key_combined, message.encode(),
                         hashlib.sha256).digest()
    return signature


def sign(r, key_client: bytes, message: str):
    r.sendlineafter('🎬 '.encode(), b'sign')
    r.sendlineafter('🔑 '.encode(), key_client.hex().encode())
    r.sendlineafter('💬 '.encode(), message.encode())
    r.recvuntil('📝 '.encode())
    return bytes.fromhex(r.recvline().decode().strip())


def get_flag(r, key_server: bytes):
    signature = sign_message(b'\0'*16, key_server, 'gib flag pls')

    r.sendlineafter('🎬 '.encode(), b'verify')
    r.sendlineafter('💬 '.encode(), b'gib flag pls')
    r.sendlineafter('📝 '.encode(), signature.hex().encode())


if __name__ == '__main__':
    r = remote('chal.hkcert23.pwnable.hk', 28029)

    key_server = b''

    for i in range(0, 16, 2):
        s = sign(r, b'\0'*(i+2), 'testing')

        for guess in range(65536):
            key_server_guess = key_server + int.to_bytes(guess, 2, 'big')
            if sign_message(b'\0'*(i+2), key_server_guess, 'testing') != s:
                continue
            key_server = key_server_guess
            break
        print(f'{key_server = }')

    print(len(key_server))

    get_flag(r, key_server)

    r.interactive()
# aaf31c12b9efa86a3f49
# print(hex(ord('I')))
# key_server = b'\xaa\xf3\x1c\x12\xb9\xef\xa8j?I'
# print(xor(key_server, 0x00000000000000000000000000000000))
# # key_server = (bytes_to_long(key_server))
# print(bytes.hex(key_server))
# # print(xor(key_server, 0))
# print(hmac.new(key_server, b"gib me flag", hashlib.sha256).digest())
