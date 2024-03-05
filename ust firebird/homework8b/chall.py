from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from secret import flag

def enc1(m, key):
    p = key.p
    q = key.q
    e = key.e
    d = pow(e, -1, (p-1)*(q-1))

    dp = d%(p-1)
    dq = d%(q-1) + getPrime(32)
    qInv = pow(q, -1, p)

    s1 = pow(m, dp, p)
    s2 = pow(m, dq, q)
    h = (qInv*(s1-s2))%p
    s = s2+h*q
    return [s, e, p*q, p, q]

key = RSA.generate(2048)
m = bytes_to_long(flag)
enc = enc1(m, key)
s = enc[0]
e =  enc[1]
n =  enc[2]
p = enc[3]
print("se-m = ", (s**e-m)%n) # why?

print("(e_enc1, n_enc1) = ", (enc[1], enc[2]))

c = []
n_lst = []
for _ in range(3):
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    e = 3
    assert s**e > n
    n_lst.append(n)
    c.append(pow(s, e, n))

print("c = ", c)
print("n = ", n_lst)

