#!/usr/bin/python

'''
offset needs to exchanged in a secret channel

'''

import cv2
import numpy as np
import random

secret = cv2.imread('lena_gray.bmp',0)
rows = secret.shape[0]
cols = secret.shape[1]

flat = [0 for i in range(rows * cols)]

#offset_val = random.randint(1, 8)
offset_val = 256
print(offset_val)
layers = min(rows, cols) // 2
c = 0

# Step 1
#
# rotating the pixels left
# limiting offset by the length of representation of a single pixel
pixel_offset = 1#offset_val % 7 + 1
for i in range(rows):
    for j in range(cols):
        p_str = bin(secret[i][j]).replace('0b', '')
        p_str = '0'*(8-len(p_str)) + p_str
        lp = p_str[0:pixel_offset]
        rp = p_str[pixel_offset:]
        p_str = rp + lp
        secret[i][j] = int(p_str,2)


# Step 2
#
# rotating the layers of the matrix
for i in range(layers):
    for j in range(i, cols-i):
        flat[c] = secret[i][j]
        c += 1
    for j in range(i+1, rows - i):
        flat[c] = secret[j][cols-i-1]
        c += 1
    for j in range(cols-i-2, i+1, -1):
        flat[c] = secret[rows-i-1][j]
        c += 1
    for j in range(rows-i-2, i, -1):
        flat[c] = secret[j][i]
        c += 1

ri = 0
rotated = [0 for i in range(rows * cols)]
while(True):
    st = rows*cols - (rows-2)*(cols-2)
    for rj in range(st):
       rotated[ri+rj] = flat[ri+(rj+offset_val)%st]
    if not min(rows, cols):
        break
    ri += rows*cols - (rows-2)*(cols-2)
    rows, cols = rows -2, cols -2

c = 0 
rows = secret.shape[0]
cols = secret.shape[1]

for i in range(layers):
    for j in range(i, cols-i):
        secret[i][j] = rotated[c]
        c += 1
    for j in range(i+1, rows - i):
        secret[j][cols-i-1] = rotated[c]
        c += 1
    for j in range(cols-i-2, i+1, -1):
        secret[rows-i-1][j] = rotated[c]
        c += 1
    for j in range(rows-i-2, i, -1):
        secret[j][i] = rotated[c]
        c += 1

cv2.imwrite('rotated_lena.pgm', secret)
rotated_lena = cv2.imread('rotated_lena.pgm', 0)
cv2.imshow('rotated_lena', rotated_lena)

cv2.waitKey(0)
cv2.destroyAllWindows()
