#!/usr/bin/python
import cv2
import numpy
import random

recieved = cv2.imread('rotated.pgm',0)
cv2.imshow('rec', recieved)
rows = recieved.shape[0]
cols = recieved.shape[1]

f = open('secret_key.txt', 'r')

mr = rows*cols - (rows-2)*(cols-2)
layers = min(rows, cols) // 2

flat = [0 for i in range(rows*cols)]
c = 0
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
for i in range(layers):
    key, offset_val = f.readline().split()
    key = int(key)
    offset_val = int(offset_val)
    pixel_offset = offset_val % 8 #1#offset_val % 7 + 1
    st = rows*cols - (rows-2)*(cols-2)
    if not key:
        for rj in range(st):
            # rotating the layer
            rotated[ri+(rj+offset_val)%st] = flat[ri+rj]
            
            # rotating the pixels
            rotated[ri+(rj+offset_val)%st] = (rotated[ri+(rj+offset_val)%st] >> pixel_offset) | (rotated[ri+(rj+offset_val)%st] << (8-pixel_offset))
    else:
        for rj in range(st):
            # rotating the layer
            rotated[ri+rj] = flat[ri+(rj+offset_val)%st]
            
            # rotating the pixels
            rotated[ri+rj] = (rotated[ri+rj] << pixel_offset) | (rotated[ri+rj] >> (8-pixel_offset))
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

f.close()

cv2.imwrite('original.pgm',recieved)
enc = cv2.imread('original.pgm',0)
cv2.imshow('orignal.pgm', enc)

cv2.waitKey(0)
cv2.destroyAllWindows()
