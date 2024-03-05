import argparse
import socket
# from dnslib import *
from base64 import b64decode, b32decode
import sys


# ======================================================================================================
# HELPERS FUNCTIONS
# ======================================================================================================

# ------------------------------------------------------------------------
# Class providing RC4 encryption/decryption functions
# ------------------------------------------------------------------------


class RC4:
    def __init__(self, key=None):
        # initialisation de la table de permutation
        self.state = list(range(256))
        self.x = self.y = 0  # les index x et y, au lieu de i et j

        if key is not None:
            self.key = key
            self.init(key)

    # Key schedule
    def init(self, key):
        for i in range(256):
            self.x = (ord(key[i % len(key)]) + self.state[i] + self.x) & 0xFF
            self.state[i], self.state[self.x] = self.state[self.x], self.state[i]
        self.x = 0

    # Decrypt binary input data
    def binaryDecrypt(self, data):
        output = [None]*len(data)
        for i in range(len(data)):
            self.x = (self.x + 1) & 0xFF
            self.y = (self.state[self.x] + self.y) & 0xFF
            self.state[self.x], self.state[self.y] = self.state[self.y], self.state[self.x]
            output[i] = (data[i] ^ self.state[(
                self.state[self.x] + self.state[self.y]) & 0xFF])
        return bytearray(output)

# ------------------------------------------------------------------------


def progress(count, total, status=''):
    """
    Print a progress bar - https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
    """
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s\t%s\t\r' % (bar, percents, '%', status))
    sys.stdout.flush()

# ------------------------------------------------------------------------


def fromBase64URL(msg):
    msg = msg.replace('_', '/').replace('-', '+')
    if len(msg) % 4 == 3:
        return b64decode(msg + '=')
    elif len(msg) % 4 == 2:
        return b64decode(msg + '==')
    else:
        return b64decode(msg)

# ------------------------------------------------------------------------


def fromBase32(msg):
    # Base32 decoding, we need to add the padding back
    # Add padding characters
    mod = len(msg) % 8
    if mod == 2:
        padding = "======"
    elif mod == 4:
        padding = "===="
    elif mod == 5:
        padding = "==="
    elif mod == 7:
        padding = "="
    else:
        padding = ""

    return b32decode(msg.upper() + padding)


# ------------------------------------------------------------------------
def color(string, color=None):
    """
    Author: HarmJ0y, borrowed from Empire
    Change text color for the Linux terminal.
    """

    attr = []
    # bold
    attr.append('1')

    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

    else:
        if string.strip().startswith("[!]"):
            attr.append('31')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[+]"):
            attr.append('32')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[?]"):
            attr.append('33')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[*]"):
            attr.append('34')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        else:
            return string

# ======================================================================================================
# MAIN FUNCTION
# ======================================================================================================


qname = "init.ONSWG4TFORZS45DYOQXHI6DUPQZA.base64.igotoschoolbybus.online"

while True:
    if qname.upper().startswith("INIT."):
        msgParts = qname.split(".")
        msg = fromBase32(msgParts[1])
        fileName = msg.decode().split('|')[0]
        nbChunks = int(msg.decode().split('|')[1])

        if msgParts[2].upper() == "BASE32":
            useBase32 = True

        fileData = ''
        chunkIndex = 0

        qname = "0.EO6ylFlsUc_7u_QD8gBDp8L8iFiGZGkhptC_QwnSem_ivrO3zFUgj-nfi9hMhgL.khV2U6tVzJq5EWnz-yXZhBWFmKMaKaM65qclb77kF5MWxV6mdVGDyj9BdDJS6uC.49h41eLONT5V_UHgksMdORol-2cYgWkzWj6H6ae8uRzgRMJjDmYss8XBOekyibe.tQVMNb2669ZzoRFkDZWIylBaJ5C.igotoschoolbybus.online"
    else:
        msg = qname[0:-(len("igotoschoolbybus.online")+1)]
        chunkNumber, rawData = msg.split('.', 1)

        if (int(chunkNumber) == chunkIndex):
            # print("y")
            fileData += rawData.replace('.', '')
            chunkIndex += 1
            # print(fileData)

            qname = "1.Lp8co2gYHOgdIDqj7CIEWkM.igotoschoolbybus.online"

        if chunkIndex == nbChunks:
            print(fileData)
            print(bytes.hex((fromBase64URL(fileData))))
            rc4Decryptor = RC4("K#2dF!8t@1qZ")

        #     print()
        #     try:
        #         rc4Decryptor = RC4("K#2dF!8t@1qZ")
        #         if useBase32:
        #             print(rc4Decryptor.binaryDecrypt(
        #                 bytearray(fromBase32(fileData))))
        #         else:
            print(rc4Decryptor.binaryDecrypt(
                bytearray(fromBase64URL(fileData))).hex())
            break
        #         print(fileData)
        #         break

        #     except IOError:
        #         print("ero")
        # break
key = "K#2dF!8t@1qZ"
state = list(range(256))
x = 0
for i in range(256):
    x = (ord(key[i % len(key)]) + state[i] + x) & 0xFF
    state[i], state[x] = state[x], state[i]
