from pwn import *



answer=["sloppytoppywithatwist","gingerdangerhermoinegranger"]
test="abcdefghijklmnopqrstuvwxyz"
print(test[0])
level=2
for i in range(100):
    answer.append("")

while True:
    r = remote('20.244.33.146', 4445)
    for i in range(level):
        r.sendline(answer[i])
    r.sendline(level)
    a = r.recvline()
    if a[0] == 'C':
        level+=1
        continue
    else:
        b = r.recvline()
        
        
    
    
        