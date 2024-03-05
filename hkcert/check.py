

flag = "hkcert23{y0u_n3d3_sn1dkn6d3n1z1h3h_y}"

sum = 0
for i in flag:
    sum += ord(i)
print(sum % 65)
print(chr(ord('y')-5))
