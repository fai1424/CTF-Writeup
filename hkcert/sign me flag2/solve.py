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


def get_flag(r, key_server: bytes):

    signature = sign_message(b'\0'*16, key_server, 'gib flag pls')

    r.sendlineafter('🎬 '.encode(), b'verify')
    r.sendlineafter('💬 '.encode(), b'gib flag pls')
    r.sendlineafter('📝 '.encode(), signature.hex().encode())


if __name__ == '__main__':
    r = remote('chal.hkcert23.pwnable.hk', 28009)

    key_server = b''

    for i in range(1):
        s = sign(r, b'\0'*(i+1), "testing")
        for j in range(256):

            if sign_message(0, b'\0',  int.to_bytes(j, 1, 'big'), "testing") == s:
                print("hereeeeeee")

        print("fuck")
        continue
        for guess in range(256):
            key_server_guess = key_server + int.to_bytes(guess, 1, 'big')

            if sign_message(3, b'\0'*(i+1), key_server_guess, f'{"testing"}') != s:
                continue
            key_server = key_server_guess
            break
        print(f'{key_server = }')

    # print(len(key_server))

    get_flag(r, key_server)

    r.interactive()
