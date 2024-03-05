#!/usr/bin/env sage

from Cryptodome.Util.number import *
# from flag import flag

flag = b"test"


def next_prime(r):
    while True:
        if isPrime(r):
            return r
        r += 1


def keygen(nbit):
    p = getPrime(nbit // 2)
    P, Q = [next_prime(p * getPrime(nbit // 2 - 10)) for _ in '01']
    print(P, Q)
    n, K = P * Q, 2 ** (nbit >> 1)
    u, y = getRandomRange(1, n), getRandomRange(1, K)
    v = - (p + u * y) % n

    pkey = (u, v, n)
    skey = (y, P, Q)

    return pkey, skey
mp+k1,op+k2
mop^2 + (k2m+k1o) p + (k1k2)

u < n
u < P*Q
u < (ap+k1)(bp*k2)

def encrypt(msg, pkey):
    u, v, n = pkey
    m = bytes_to_long(msg)
    assert m < n
    m0 = (u*m - v) % n
    while True:
        if isPrime(u + v):
            break
        else:
            u += 1
    e = u + v
    c = pow(m0, e, n)
    return c


'''
m0 = u*m-v mod n
c = m0**u'+v
'''

nbit = 1024
pkey, skey = keygen(nbit)
u, v, n = pkey
c = encrypt(flag, pkey)

print(f'u = {u}')
print(f'v = {v}')
print(f'n = {n}')
print(f'c = {c}')
