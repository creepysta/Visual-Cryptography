import cv2
import numpy as np
import random

secret = cv2.imread('lena_gray.bmp',0)
rows = secret.shape[0]
cols = secret.shape[1]

f = open('pixel_rot.txt', 'w')
for i in range(rows):
    for j in range(cols):
        key = random.randint(0,1)
        offset_val = random.randint(1,8)
        p_str = bin(secret[i][j]).replace('0b', '')
        p_str = '0'*(8-len(p_str)) + p_str
        if key == 0:
            lp = p_str[0:offset_val]
            rp = p_str[offset_val:]
        else:
            lp = p_str[0:len(p_str)-offset_val]
            rp = p_str[len(p_str)-offset_val:]
        p_str = rp + lp
        secret[i][j] = int(p_str,2)
        f.write(str(key) + " " + str(offset_val) + '\n')

f.close()

cv2.imwrite('pixel_rot.pgm',secret)
enc = cv2.imread('pixel_rot.pgm',0)
cv2.imshow('pixel_rot.pgm', enc)

cv2.waitKey(0)
cv2.destroyAllWindows()
