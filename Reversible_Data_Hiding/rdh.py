import random
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

cover = cv2.imread('lena_gray.bmp', 0)

cv2.imshow('cover0', cover)

a = 0
b = cover.shape[0]*cover.shape[1]

temp_a = 0
temp_b =  cover.shape[0]*cover.shape[1]


pixels = [0 for i in range(256)]

for i in range(cover.shape[0]):
    for j in range(cover.shape[1]):
       pixels[cover[i][j]] += 1

#print(pixels)

for i in range(255):
    if temp_a <= pixels[i]:
        temp_a = pixels[i]
        a = i
    if temp_b >= pixels[i]:
        temp_b = pixels[i]
        b = i

'''
print(a)
print(pixels[a])
print(b)
print(pixels[b])

cover = np.array(cover)
plt.hist(cover)
plt.show()
'''


for i in range(cover.shape[0]):
    for j in range(cover.shape[1]):
        if cover[i][j] >= a and cover[i][j] <= b:
            cover[i][j] += 1


cv2.imshow('cover', cover)
cv2.waitKey(1000)
