import cv2
import numpy as np
import matplotlib.pyplot as plt

img_g = cv2.imread('aya_matsuura.pgm',0)
img_c = cv2.imread('azumi_kawashima2.ppm')
#img_t = cv2.imwrite('test_img.ppm')
#encrypting
for i in range(img_g.shape[0]):
    for j in range(img_g.shape[1]):
        img_c[i,j,0] = (img_c[i,j,0]|7)&(248+((img_g[i,j]&224)>>5))
        img_c[i,j,1] = (img_c[i,j,1]|7)&(248+((img_g[i,j]&28)>>2))
        img_c[i,j,2] = (img_c[i,j,2]|3)&(252+(img_g[i,j]&3))

cv2.imshow('gray',img_g)
cv2.imshow('color',img_c)
#cv2.imshow('test',img_t)

img_t1 = cv2.imwrite('Cover_1.ppm',img_c[:,:,:]/2)
img_t2 = cv2.imwrite('Cover_2.ppm',img_c[:,:,:]/2)

img_t1 = cv2.imread('Cover_1.ppm')
img_t2 = cv2.imread('Cover_2.ppm')

cv2.imshow('testCover1',img_t1)
cv2.imshow('testCover2',img_t2)

#decrypting
img_ret_array1 = np.array(img_t1)
img_ret_array2 = np.array(img_t2)

img_retrieved = cv2.imwrite('retrieved_img.ppm',img_ret_array1+img_ret_array2)
img_retrieved = cv2.imread('retrieved_img.ppm')

cv2.imshow('retrieved',img_retrieved)

red_channel_list = np.array(img_retrieved[:,:,2])
green_channel_list = np.array(img_retrieved[:,:,1])
blue_channel_list = np.array(img_retrieved[:,:,0])

#img_original_r = cv2.imread('original_img.pgm',0)

#for i in range(img_retrieved.shape[0]):
#    for j in range(img_retrieved.shape[1]):
#       img_original_r[i,j] = ((red_channel_list[i,j]&3)+((green_channel_list[i,j]&28)>>3)+(blue_channel_list[i,j]&224)>>5)

#original gray scale image
cv2.imwrite('original_img.pgm',(((blue_channel_list&7)<<5) + ((green_channel_list&7)<<2) + (red_channel_list&3)))
img_original_g = cv2.imread('original_img.pgm',0)
cv2.imshow('original_grayscale',img_original_g)
cv2.waitKey(0)
cv2.destroyAllWindows()
