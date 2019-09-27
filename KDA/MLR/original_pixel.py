#!/usr/bin/python
import cv2
import numpy
import random

rec = cv2.imread('rotated_lena_pixel.pgm',0)
r = rec.shape[0]
c = rec.shape[1]
offset_val = 3

for i in range(r):
    for j in range(c):
        p_str = bin(rec[i][j]).replace('0b', '')
        lp = p_str[0:len(p_str)-offset_val]
        rp = p_str[len(p_str)-offset_val:]
        p_str = rp + lp
        rec[i][j] = int(p_str, 2)

cv2.imwrite('re_rotated_lena_pixel.pgm', rec)
rrp = cv2.imread('re_rotated_lena_pixel.pgm',0)
cv2.imshow('original', rrp)

cv2.waitKey()
cv2.destroyAllWindows()

