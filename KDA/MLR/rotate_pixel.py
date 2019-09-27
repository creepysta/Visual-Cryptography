#!/usr/bin/python
import cv2
import numpy
import random

secret = cv2.imread('lena_gray.bmp',0)
rows = secret.shape[0]
cols = secret.shape[1]
#offset_val = random.randint(1,8)
offset_val = 3
print(offset_val)

for i in range(rows):
    for j in range(cols):
        p_str = bin(secret[i][j]).replace('0b','')
        lp = p_str[0:offset_val]
        rp = p_str[offset_val:]
        p_str = rp + lp
        secret[i][j] = int(p_str, 2)

cv2.imwrite('rotated_lena_pixel.pgm', secret)
rotated_pixel = cv2.imread('rotated_lena_pixel.pgm',0)
cv2.imshow('rotated_lena_pixel', rotated_pixel)

cv2.waitKey(0)
cv2.destroyAllWindows()

