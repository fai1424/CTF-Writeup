def xor(a, b):
    return bytes(u ^ v for u, v in zip(a, b))


print(xor(b'0', b'12345678'))
