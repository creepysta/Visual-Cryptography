import cv2
import numpy as np
import random

recieved= cv2.imread('pixel_rot.pgm', 0)
rows = recieved.shape[0]
cols = recieved.shape[1]

f = open('pixel_rot.txt', 'r')
for i in range(rows):
    for j in range(cols):
        p_str = bin(recieved[i][j]).replace('0b','')
        p_str = '0'*(8-len(p_str)) + p_str
        key, offset_val = f.readline().split()
        key = int(key)
        offset_val = int(offset_val)
        if key == 0:
            lp = p_str[0:len(p_str)-offset_val]
            rp = p_str[len(p_str)-offset_val: ]
        else:
            lp = p_str[0:offset_val]
            rp = p_str[offset_val:]
        p_str = rp + lp
        recieved[i][j] = int(p_str, 2)

f.close()

cv2.imwrite('dec_pixel_rot.pgm', recieved)
org = cv2.imread('dec_pixel_rot.pgm',0)
cv2.imshow('original' ,org)

cv2.waitKey(0)
cv2.destroyAllWindows()
