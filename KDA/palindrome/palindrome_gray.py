import cv2
import numpy as np

s_img = cv2.imread('aya_matsuura.pgm', 0)
c_img = cv2.imread('azumi_kawashima2.pgm', 0)
r_img1 = cv2.imread('anonymous1.pgm', 0)
r_img2 = cv2.imread('abe_natsumi.pgm', 0)
r_img3 = cv2.imread('brian_kernighan.pgm', 0)

cv2.imshow('cover', c_img)

# making all the pixels 3 digit non palindromes
for i in range(c_img.shape[0]):
    for j in range(c_img.shape[1]):
        if (c_img[i, j] / 100) == 0 or (c_img[i, j] / 10) == 0:
            c_img[i, j] = 100
        else:
            if c_img[i, j] % 10 == (int(c_img[i, j] / 100)) % 10:
                c_img[i, j] = c_img[i, j] + 1

# making the base image monochrome
for i in range(s_img.shape[0]):
    for j in range(s_img.shape[1]):
        if s_img[i, j] < 128:
            s_img[i, j] = 0
        else:
            s_img[i, j] = 255

cv2.imshow('cover after making the pixels 3digit non palindrome', c_img)
cv2.imshow('secret image', s_img)

for i in range(s_img.shape[0]):
    for j in range(s_img.shape[1]):
        if s_img[i, j] == 0:
            c_img[i, j] = c_img[i, j] + (((int(c_img[i, j]/100)) % 10) - (c_img[i, j] % 10))
cv2.imshow('cover img after making the corresponding black pixels palindrome', c_img)

# hiding the cover image in 3 random images
for i in range(r_img1.shape[0]):
    for j in range(r_img1.shape[1]):
        r_img1[i, j] = (r_img1[i, j] | 7) & (248 + (c_img[i, j] >> 5))
        r_img2[i, j] = (r_img2[i, j] | 7) & (248 + ((c_img[i, j] & 28) >> 2))
        r_img3[i, j] = (r_img3[i, j] | 3) & (252 + (c_img[i, j] & 3))

cv2.imshow('share 1', r_img1)
cv2.imshow('share 2', r_img2)
cv2.imshow('share 3', r_img3)

# reversing the process of encryption to get back the 0th layer matrix of the initial cover image
cv2.imwrite('retrieved_img.pgm', (((r_img1[:, :] & 7) << 5)+((r_img2[:, :] & 7) << 2)+(r_img3[:, :] & 3)))
retrieve = cv2.imread('retrieved_img.pgm', 0)
cv2.imshow('retrieve', retrieve)


# for every palindrome in that matrix we put a zero and others a one to get the initial monochrome secret message
for i in range(r_img1.shape[0]):
    for j in range(r_img2.shape[1]):
        if retrieve[i, j] % 10 == (int(retrieve[i, j]/100)) % 10:
            retrieve[i, j] = 0
        else:
            retrieve[i, j] = 255

cv2.imshow('original', retrieve)

cv2.waitKey(0)
cv2.destroyAllWindows()
