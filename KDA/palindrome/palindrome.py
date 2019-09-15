import cv2
import numpy as np

secret_img = cv2.imread('aya_matsuura.pgm', 0)
cover_img = cv2.imread('azumi_kawashima2.ppm')
random_img1 = cv2.imread('anonymous1.ppm')
random_img2 = cv2.imread('anonymous2.ppm')
random_img3 = cv2.imread('brian_kernighan.ppm')


cv2.imshow('base_img', cover_img)
cv2.imshow('random1', random_img1)
cv2.imshow('random2', random_img2)
cv2.imshow('random3', random_img3)

# 3 digit numbers such that no number is palindrome
for i in range(cover_img.shape[0]):
    for j in range(cover_img.shape[1]):
        if(cover_img[i, j, 0] / 100) == 0 or (cover_img[i, j, 0] / 10) == 0:
            cover_img[i, j, 0] = 100
            # cover_img[i,j,0] + (100 - cover_img[i,j,0]);
        else:
            if cover_img[i, j, 0] % 10 == (int(cover_img[i, j, 0] / 100)) % 10:
                cover_img[i, j, 0] = cover_img[i, j, 0] + 1
cv2.imshow('cover_img', cover_img)

# making the base image monochrome
for i in range(secret_img.shape[0]):
    for j in range(secret_img.shape[1]):
        if secret_img[i, j] < 128:
            secret_img[i, j] = 0
        else:
            secret_img[i, j] = 255
cv2.imshow('message', secret_img)

# converting all the numbers corresponding a black pixel in secret image a palindrome (3 digit) in the cover image
for i in range(secret_img.shape[0]):
    for j in range(secret_img.shape[1]):
        if secret_img[i, j] == 0:
            cover_img[i, j, 0] = cover_img[i, j, 0] + (((int(cover_img[i, j, 0] / 100)) % 10) - (cover_img[i, j, 0] % 10))
cv2.imshow('cover_img_treatment', cover_img)


# breaking the 0th layer of cover image into binary equivalent of the decimal numbers
# in 2:3:3 number of bits
# in each share of the random images in their 0th layer
for i in range(random_img1.shape[0]):
    for j in range(random_img1.shape[1]):
        random_img1[i, j, 0] = (random_img1[i, j, 0] | 7) & (248 + (cover_img[i, j, 0] >> 5))
        random_img2[i, j, 0] = (random_img2[i, j, 0] | 7) & (248 + ((cover_img[i, j, 0] & 28) >> 2))
        random_img3[i, j, 0] = (random_img3[i, j, 0] | 3) & (252 + (cover_img[i, j, 0] & 3))

cv2.imshow('share1', random_img1)
cv2.imshow('share2', random_img2)
cv2.imshow('sahre3', random_img3)

# r1 = np.array(random_img1[:,:,0])
# r2 = np.array(random_img2[:,:,0])
# r3 = np.array(random_img3[:,:,0])


# reversing the process of encryption to get back the 0th layer matrix of the initial cover image
retrieve = cv2.imwrite('retrieved_img.pgm', (((random_img1[:, :, 0] & 7) << 5) + ((random_img2[:, :, 0] & 7) << 2) + (random_img3[:, :, 0] & 3)))
retrieve = cv2.imread('retrieved_img.pgm', 0)
cv2.imshow('retrieve', retrieve)


# for every palindrome in that matrix we put a zero and others a one to get the initial monochrome secret message
for i in range(random_img1.shape[0]):
    for j in range(random_img2.shape[1]):
        if retrieve[i, j] % 10 == (int(retrieve[i, j] / 100)) % 10:
            retrieve[i, j] = 0
        else:
            retrieve[i, j] = 255

cv2.imshow('original', retrieve)

'''
img1 = cv2.imwrite('test.pgm',cover_img[:,:,0])
img1 = cv2.imread('test.pgm',0)
for i in range(cover_img.shape[0]):
    for j in range(cover_img.shape[0]):
        if cover_img[i,j,0]%10 == (int(cover_img[i,j,0]/100))%10:
            img1[i,j] = 0
        else:
            img1[i,j] = 255

cv2.imshow('recovered',img1)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()
