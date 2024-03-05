from Crypto.Util.number import bytes_to_long
from Crypto.PublicKey import RSA
from secret import flag

def main():
    key = RSA.generate(2048, e=17)
    key = key.public_key() # Oops, I lost the private key...
    print(key.export_key().decode())
    c = pow(bytes_to_long(flag), key.e, key.n)
    print("Can you help me? I've lost my private key ;-;")
    print(f"The encrypted flag is {c}")
    print("Bye!")

if __name__ == "__main__":
    main()
