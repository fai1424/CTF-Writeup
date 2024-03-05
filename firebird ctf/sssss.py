import os
import sys
assests = []
with open("/Users/lamhungfai/Documents/GitHub/CTF-Writeup/firebird ctf/filterlist.txt") as fh:
    for line in fh:
        print(line.strip().split('\t')[0])
        try:

            ip_to_attack = str(line).strip().split(
                '\t')[0]+":"+str(line).strip().split('\t')[1]

            assests.append(ip_to_attack)

        except:
            pass

for items in assests:
    ip, port = items.split(":")
    print("trying")
    msg = os.popen('nmap -sV --script rtsp-* -p' + port+' '+ip)
    print(msg.read())
