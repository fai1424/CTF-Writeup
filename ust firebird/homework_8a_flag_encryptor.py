import hashlib
import random
from z3 import *
from pwn import xor

flag = '<**CENSORED**>'

key = '<**CENSORED**>'
output = 'ce1ebc8451d4e8e1918df3ef5f40fcad8b334d06e4a91a524bf2726bc6d27404d7bebad7036c68a5cc32a3a3371adb530f06ddaa77010ed64a4dd4d2743592df238ec92962d79a8f3f21a44b15dfe827b39a24a1810ef3673fcc426bff06669f0df5'
# print("97",output[97])

output = bytes.fromhex(output)
output = list(output)
print(len(output))
# print(output)
# print(len(output))

newoutput = []
for i in range(1, 98):
    # print(i)
    a = output[i-1] ^ output[i]
    newoutput.append(a)

newoutput.insert(0, output[0] ^ output[96] ^ output[97])

print(newoutput[0])
print(newoutput[65])
print(ord('|'))
print(newoutput[66:98])
# print(len(newoutput))
# print(newoutput[66])
# print(ord('|'))

b = [71, 224, 75, 181, 77, 21, 176, 30, 133, 239, 94, 202, 55, 207, 148, 41,
     190, 133, 32, 143, 253, 148, 88, 243, 142, 41, 148, 249, 96, 249, 146, 248]
k = [52]
print('aaaaaa', ord('|'), newoutput[65], newoutput[64])

for i in range(31):

    num = b[i] - newoutput[65+i] - k[i]
    while (num < 0):
        num += 255
    k.append(num)

print('k', k)
print(newoutput[97] == k[31]+k[0]+54)
print(newoutput[97])
print(k[31], k[0])
print(len(k))

c = []
for i in range(97):
    # print(newoutput)
    num = int(newoutput[i+1])-newoutput[i]-int(k[(i) % 32])

    while (num < 0):
        num += 255
    # print(num)
    c.append(num)
    # print(c)
for i in range(len(c)):
    c[i] = chr(c[i])
print(str(c))

print("".join(c[i] for i in range(len(c))))


# output = list(output)
# newoutput= []
# for i in range(len(output)):
#     output[i] = ord(output[i])
# for i in range(1,196):
#     newoutput.append(output[i] ^ output[i-1])
# print(newoutput)
# newoutput.insert(0,output[195]^output[0])
# print(newoutput)

# print(newoutput[164:196])
# print(ord('|'))
# print(chr(120))
# print(newoutput[164:196])
# keyy=[,,133,,,121,,,57,,,115,,,55,,,119,,,56,,,117,,,53,,,,,119]


def decrypt_flag():
    enc2 = bytes.fromhex(output)
    findkey = [83, 6, 85, 80, 9, 9, 1, 85, 3, 85, 5, 1, 4, 85, 5,
               0, 87, 6, 4, 84, 4, 0, 86, 6, 0, 0, 15, 95, 86, 84, 2, 83]
    s.add()
    real_enc2 = enc2[0:97]
    # print(real_enc2)
    # print(enc2)
    enc1 = [BitVec(f"enc1_{i}", 8) for i in range(len(enc2))]
    key = [BitVec(f"key_{i}", 8) for i in range(len(enc2))]
    message = [BitVec(f"message_{i}", 8) for i in range(len(enc2))]

    randomnum = 86

    s = z3.Solver()
    s.add(enc2[0:97] == bytes.fromhex(output)[98:195])
    # s.add([enc2[i] = enc2[(i-1)%len(enc2)] ^ enc2[i] for i in range(len(enc2))])


def encrypt_flag(flag, key):
    key = hashlib.md5(key.encode()).hexdigest().encode()
    message = (flag.encode() + b'|' + key)
    enc1 = chr(random.randrange(0xff)).encode()
    for i in range(len(message)):

        enc1 += (((message[i] + key[i % len(key)] + enc1[i]) %
                 0xff)).to_bytes(1, 'little')
        # print(enc1)
    enc2 = list(enc1)
    # print(enc2)
    # print(len(enc2))

    for i in range(len(enc2)):
        # print(i,(i-1)%len(enc2))
        enc2[i] = enc2[(i-1) % len(enc2)] ^ enc2[i]

    a = (bytes(enc2).hex())
    a = bytes.fromhex(a)
    a = list(a)
    # print((a))
    return bytes(enc2).hex()

# print(bytes(b'f').hex()-bytes(b'|').hex())


'''
key[0] = 92
message[0] + key[0] = 10
key[0]+key[1] = f
total 196
random number is 5
between flag and key have a |
enc[0] = 5
enc[1] = message[0] + key[0] + 5 % 255 = f
enc[2] = message[1] + key[1] +5 %255
enc[195] = message[194] + key[194] + 5 % 255
enc[98] = message[97] + key[97%97] + 5%255 = f
| + key[0]
message[97] = '|'

assume len = 10
enc2[0] = enc2[9] ^ enc2[0]
enc[1] = enc2[8] ^ enc2[1]
72
63
54
45
36
27
18
09
0-97
98-196 = enc2[0]-enc2[97]
enc[9] = enc2'[0] ^ enc2[9]
enc[9] = enc2[9] ^ enc2[0] ^ enc2[9]
enc[9] = enc2[0]
last bit is the first random 




'''


def main():
    # print(encrypt_flag(flag, key))
    # print(decrypt_flag())
    encrypt_flag(flag, key)


if __name__ == "__main__":
    main()


key = 'abc'

a = hashlib.md5(key.encode()).hexdigest().encode()
