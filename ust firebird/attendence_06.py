from Cryptodome.Cipher import AES		
from Cryptodome.Util.Padding import unpad
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
from pwn import xor
import multiprocessing
import os
import socket
import base64

Ciphertext= "c7b16adc30d89708bac5b651f3f879a0da86397d7a090b8715ba99daf7428eed"
# print(len(Ciphertext))

Ciphertext = bytes.fromhex(Ciphertext)
print(Ciphertext)
# (ciphertext above is in hex form, remember to convert it to bytes)

# Key: very_good_key (padded with PKCS#7 to 16 bytes)
key = b"very_good_key"
key += b'\x03\x03\x03'

# print(base64.b64encode(key))
# print(len(key))
# print(len(bin(bytes_to_long(key))[2:]))
# print(base64.b64decode(b'\x03'))
IV= b"aaaaaaaaaaAAAAAA"
# print(xor(IV,key).decode())
IV1 = b'0000000000000000'
trial = AES.new(key,AES.MODE_CBC,IV1)
cipher = b'\x91C\xd3\xca\x10tW\t\xfb\xe3\x1b\xb1\x00\xe2!\xb6'
# dec = trial.decrypt(b'\xa9\xe4\x98 \x12\x8c\x98\x94!1\xdc\x9bj\xbc\xd6\6')
# print(dec)
print(xor(cipher,IV1))
plaintext = b'flag{jglapoihnb}'
haah = AES.new(key,AES.MODE_CBC,IV1)
print(haah.decrypt(cipher))






enc = b'132500ed5fa5ff21b43aca3fb5b572e98abe3be4236830797f1e2eeece92af8fe4e3c78d796fa729979304427641cfd3'
IV = 'a1821b881035c48ca66c8de2a6691cec'
print(hex(IV))
key = b'1256789912345679'
# cipher = AES.new(key,AES.MODE_CBC,IV)
# print(cipher.decrypt(enc))
