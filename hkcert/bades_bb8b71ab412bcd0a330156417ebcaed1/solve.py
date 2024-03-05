from pwn import *
import binascii


m1 = '9754b0b896d09ba2'
c0 = '8efc89ed2c2a9aaf'

c0 = '8efc89ed2c2a9aaf'

c1 = '9754b0b896d09ba2'
c2 = 'ca5e31c0262e3040'
c3 = 'c8aeb19e7ff17768'
c4 = '9a9ea03b91c8f486'
c5 = '40b24b7e75da8c3f'
c6 = 'fe682c8fc81f50ce'
c7 = 'd6fd830ddb8826d6'
c8 = '52627181b4b79241'
c9 = 'bfd3642ae2960b2f'

c0_c1 = bytes.hex((xor(bytes.fromhex(c0), bytes.fromhex(c1))))

a = '0ef2c66953d8fd57'
print(((xor(bytes.fromhex(c0), bytes.fromhex(a)))))


m1 = 'e697ea885e5ea89c'
print(bytes.fromhex(m1))


m1 = bytes.hex(((xor(bytes.fromhex(c0), bytes.fromhex(m1)))))
print(m1)

b = bytes.hex((xor(bytes.fromhex(c0), bytes.fromhex(m1), bytes.fromhex(c2))))


print(c0_c1+b)

c1_m2 = 'ec10f5ebc9b3afcc'
m2 = bytes.hex(((xor(bytes.fromhex(c1_m2), bytes.fromhex(c1)))))

# hkcert23{{DES_c4n_6e_34s1ly_d0wngr4d3d_6y_ch4ng31ng_l1t71e_th1n9s}
c = bytes.hex((xor(bytes.fromhex(c1), bytes.fromhex(m2), bytes.fromhex(c3))))

print(c0_c1+b+c)
c2_m3 = '9568549f151a4371'
m3 = bytes.hex(((xor(bytes.fromhex(c2_m3), bytes.fromhex(c2)))))
print(m3)

d = bytes.hex((xor(bytes.fromhex(c2), bytes.fromhex(m3), bytes.fromhex(c4))))
print(c0_c1+b+c+d)
c3_m4 = 'a4d7eefa4f86190f'
m4 = bytes.hex(((xor(bytes.fromhex(c3_m4), bytes.fromhex(c3)))))
print(m4)

e = bytes.hex((xor(bytes.fromhex(c3), bytes.fromhex(m4), bytes.fromhex(c5))))
print(c0_c1+b+c+d+e)
c4_m5 = 'e8aac408f597c2ff'
m5 = bytes.hex(((xor(bytes.fromhex(c4_m5), bytes.fromhex(c4)))))
print(m5)

f = bytes.hex((xor(bytes.fromhex(c4), bytes.fromhex(m5), bytes.fromhex(c6))))
print(c0_c1+b+c+d+e+f)
c5_m6 = '1fd1234a1bbdbf0e'
m6 = bytes.hex(((xor(bytes.fromhex(c5_m6), bytes.fromhex(c5)))))
print(m6)

g = bytes.hex((xor(bytes.fromhex(c5), bytes.fromhex(m6), bytes.fromhex(c7))))
print(c0_c1+b+c+d+e+f+g)
c6_m7 = '900f73e3f96b67ff'
m7 = bytes.hex(((xor(bytes.fromhex(c6_m7), bytes.fromhex(c6)))))
print(m7)

h = bytes.hex((xor(bytes.fromhex(c6), bytes.fromhex(m7), bytes.fromhex(c8))))
print(c0_c1+b+c+d+e+f+g+h)
c7_m8 = 'b3a2f765eae61fa5'
m8 = bytes.hex(((xor(bytes.fromhex(c7_m8), bytes.fromhex(c7)))))
print(m8)

i = bytes.hex((xor(bytes.fromhex(c7), bytes.fromhex(m8), bytes.fromhex(c9))))
print(c0_c1+b+c+d+e+f+g+h+i)
c8_m9 = '2f657686b3b09546'
m9 = (((xor(bytes.fromhex(c8_m9), bytes.fromhex(c8)))))
print(m9)
