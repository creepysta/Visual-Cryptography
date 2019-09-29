#!/D/Codes/Python/venv/Scripts python

import cv2
import numpy as np

img = cv2.imread('lena_gray.bmp',0)
cv2.imshow('image', img)
'''
# blurred = cv2.medianBlur(img, 5)
# blurred = cv2.blur(img, (5,5))
# blurred = cv2.blur(blurred, (5,5))
# blurred = cv2.GaussianBlur(img, (5,5), 0)
# blurred = cv2.GaussianBlur(blurred, (5,5), 0)
# edges = cv2.Canny(blurred, 10, 20)
# images = np.concatenate((blurred, edges, img), axis = 1)
img = blurred
th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
'''

rows = img.shape[0]
cols = img.shape[1]

for i in range(rows):
    for j in range(cols):
        if int(abs(img[i][j] - img[i][j+1])) > 20:
            img[i][j] = 255
            break
        else:
            img[i][j] = 0

    for k in range(cols-1, j, -1):    
        if int(abs(img[i][k] - img[i][k-1])) > 20:
            img[i][k] = 255
            break
        else:
            img[i][k] = 0

cv2.imshow('image', img)
#cv2.imshow('thresh', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
