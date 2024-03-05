import binascii
import hashlib
from Cryptodome.Cipher import AES

from Cryptodome.Util.number import *
from pwn import xor

enc_gift1 = binascii.unhexlify(
    "bad7dbcff968d7cdbf51da011fe94e176fc8e7528e4dd85d2d5fc20ba69cefb7bfd03152a2874705bd2d857ea75b3216a830215db74772d9b9e9c218271d562694d3642d2917972fdb8c7363d8125730a50824cd8dc7e34cd4fa54be427cca".strip())
enc_flag = binascii.unhexlify(
    "c1c78891e30cd4c0aa5ed65c17e8550429c4e640881f9f1d6a56df".strip())
enc_gift2 = "********c********b**************4***5********3****6a*****a**2********c*8******7***********3***5***2********e*5*************a******5**c***74***********fee046b4d2918096cfa3b76d6622914395c7e28eef".strip()
gift1 = b'***********************************************************************************************'
b = b'I AM DEATHWING, THE DESTROYER, THE END OF ALL THINGS, INEVITABLE, INDOMITABLE; I AM THE CATACLYSM!'
a = b'I am Deathwing, the Destroyer, the end of all things! Inevitable. Indomitable. I AM THE CATACLYSM'
# print(len(b, len(gift1))
# print(b[:27])
# # print(enc_gift1)
# print(len(enc_flag))
# print(binascii.unhexlify("45"))
# blob = xor(enc_flag, enc_gift1)
# print(xor(b'I am Deathwing, the Destroy', blob[:27]))
# flag = xor(blob, b'2023: flag{4ff732dd2B7445fd'[:27])[:27]
# before = "flag{4ff732ddE2B744E5fd"
# print(flag)
# # print(xor(GxorF, gift1))
# key2 = b'tn*-ix6L*tCa*}i*'
# print(gift2)

key2 = b'tn*-ix6L*tCa*}i*'
key_len = len(key2)
h = binascii.unhexlify(hashlib.sha256(key2).hexdigest())[:11]

gift2 = b'I tell you this,Afor when my days have come to an end , you, shall be King.'+h


def encrypt2(message, key, iv):
    padding = bytes((key_len - len(message) % key_len) * '&', encoding='utf-8')
    # print(padding)
    message += padding
    # print(message)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(message)
    return ciphertext.hex()


def decrypt2(cipher, key):
    message = AES.new(key, AES.MODE_ECB)
    plaintext = message.decrypt(cipher)
    print("plaintext: ", plaintext)
    return plaintext.hex()


def encrypt3(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(message)
    return ciphertext.hex()


IV = b'E0000E005000000}'
ECBcipher = encrypt3(gift2[:16], key2)
CBCcipher = xor(binascii.unhexlify(ECBcipher.strip()), IV)
print(CBCcipher.hex())


gift2 = gift2[:16]
# print(gift2)
enc_gift2 = "********c********b**************4***5********3****6a*****a**2********c*8******7***********3***5***2********e*5*************a******5**c***74***********fee046b4d2918096cfa3b76d6622914395c7e28eef".strip()
# flag2 = b'ECFFFEFFFFFFFFF}'
flag2 = b'0000000000000000'


# print(len("40bf230656650349886d8c51943d87a5"))

a = encrypt2(gift2, key2, IV)

print(a[:32])

# #     if a[-42:] == "fee046b4d2918096cfa3b76d6622914395c7e28eef":
# #         print(a)
# b = binascii.unhexlify(
#     "de50f27c72a1c03a870c42739fa5d032a06114035d5cec3a63487b5a54275269")
# print(len(b))
# print(xor(b, binascii.unhexlify(decrypt2(b, key2))))
# print(decrypt2(b, key2))
# print(binascii.unhexlify(decrypt2(b, key2)))
