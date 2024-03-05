from PIL import Image


im = Image.open("source.png")
pix = im.load()
lines = []


for x in range(47):
    line = ""
    for y in range(47):
        line += str(int(pix[x, y] == (0, 0, 0, 255)))
    lines += [line]


with open("out.enc", "w") as f:
    cnt = 0
    for i in lines:
        if cnt % 2 == 0:
            f.write(i)
        else:
            f.write(i[::-1])
        cnt += 1
