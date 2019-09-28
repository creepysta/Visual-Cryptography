#!/usr/bin/python
'''
offset needs to exchanged in a recieved channel

'''

import cv2 
import numpy as np
import random

recieved = cv2.imread('rotated_lena.pgm',0)
cv2.imshow('recieved', recieved)
rows = recieved.shape[0]
cols = recieved.shape[1]

flat = [0 for i in range(rows*cols)]

#offset_val = random.randint(1, 8)
offset_val = 256
print(offset_val)
layers = min(rows, cols) // 2
c = 0

# Step 1
#
# rotating the layers of the matrix
for i in range(layers):
    for j in range(i, cols-i):
        flat[c] = recieved[i][j]
        c += 1
    for j in range(i+1, rows - i):
        flat[c] = recieved[j][cols-i-1]
        c += 1
    for j in range(cols-i-2, i+1, -1):
        flat[c] = recieved[rows-i-1][j]
        c += 1
    for j in range(rows-i-2, i, -1):
        flat[c] = recieved[j][i]
        c += 1

ri = 0
rotated = [0 for i in range(rows * cols)]
while(True):
    st = rows*cols - (rows-2)*(cols-2)
    for rj in range(st):
       rotated[ri+(rj+offset_val)%st] = flat[ri+rj]
    if not min(rows, cols):
        break
    ri += rows*cols - (rows-2)*(cols-2)
    rows, cols = rows -2, cols -2

c = 0 
rows = recieved.shape[0]
cols = recieved.shape[1]

for i in range(layers):
    for j in range(i, cols-i):
        recieved[i][j] = rotated[c]
        c += 1
    for j in range(i+1, rows - i):
        recieved[j][cols-i-1] = rotated[c]
        c += 1
    for j in range(cols-i-2, i+1, -1):
        recieved[rows-i-1][j] = rotated[c]
        c += 1
    for j in range(rows-i-2, i, -1):
        recieved[j][i] = rotated[c]
        c += 1


# Step 2
#
# rotating the pixels right
# limiting offset by the length of representation of a single pixel
pixel_offset = 1#offset_val % 7 + 1
for i in range(rows):
    for j in range(cols):
        p_str = bin(recieved[i][j]).replace('0b', '')
        p_str = '0'*(8-len(p_str)) + p_str
        lp = p_str[0:len(p_str)-pixel_offset]
        rp = p_str[len(p_str)-pixel_offset:]
        p_str = rp + lp
        recieved[i][j] = int(p_str,2)

cv2.imwrite('recovered_lena.pgm', recieved)
original = cv2.imread('recovered_lena.pgm',0)
cv2.imshow('recovered_lena', original)

cv2.waitKey(0)
cv2.destroyAllWindows()
