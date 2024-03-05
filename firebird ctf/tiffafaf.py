import cv2 as cv

img = cv.imread(
    "/Users/lamhungfai/Documents/GitHub/CTF-Writeup/firebird ctf/aura.tif")
cv.imshow("Display window", img)
k = cv.waitKey(0)
