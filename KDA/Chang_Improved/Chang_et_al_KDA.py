import cv2
import random
import numpy as np

secret = cv2.imread('aya_matsuura.pgm', 0)
random_img1 = cv2.imread('azumi_kawashima2.pgm',0)
random_img2 = cv2.imread('brian_kernighan.pgm',0)

total_pixels = secret.shape[0]*secret.shape[1]

# Sn*m : m = 8 and n = 2 for 2 * 2 sharing scheme
S = [[[[0 for j in range(8)] for i in range(2)] for k in range(secret.shape[1])] for l in range(secret.shape[0])]

# binary representation of every pixel of shared image
k = [[['0'] for Ij in range(secret.shape[1])]for Ii in range(secret.shape[0])]


# first row has one more 1 that 0
for Ii in range(secret.shape[0]):
    for Ij in range(secret.shape[1]):
        for i in range(5):
            S[Ii][Ij][0][i] = 1

    
for Ii in range(secret.shape[0]):
    for Ij in range(secret.shape[1]):
        temp_k = list(bin(secret[Ii][Ij]))
        temp_k = temp_k[2:]
        k[Ii][Ij] = temp_k.copy()
        for zeros in range(8 - len(temp_k)):
            k[Ii][Ij].insert(0, 0)
#        print(len(k[Ii][Ij]), end = ' ')
#    print()


for Ii in range(secret.shape[0]):
    for Ij in range(secret.shape[1]):
        for ki in range(len(k[Ii][Ij])):
            S[Ii][Ij][1][ki] = S[Ii][Ij][0][ki] ^ int (k[Ii][Ij][ki])



# creating 1B
for Oi in range(random_img1.shape[0]):
    for Oj in range(random_img1.shape[1]):
        temp_k = list(bin(random_img1[Oi][Oj]))
        temp_k = temp_k[2:]
        for zeros in range(8 - len(temp_k)):
            temp_k.insert(0, '0')
        for s in range(8):
            if S[Oi][Oj][0][s] == 1:
                temp_k[s] = k[Oi][Oj][s]
        dec = 0
        for i in range(len(temp_k)-1,-1,-1):
           dec = dec + int(temp_k[i])*2**(7-i)
        random_img1[Oi][Oj] = dec

cv2.imwrite('Cover1.pgm', random_img1)
cover1 = cv2.imread('Cover1.pgm', 0)
cv2.imshow('Cover1', cover1)
            
# creating 2B
for Oi in range(random_img2.shape[0]):
    for Oj in range(random_img2.shape[1]):
        temp_k = list(bin(random_img2[Oi][Oj]))
        temp_k = temp_k[2:]
        for zeros in range(8 - len(temp_k)):
            temp_k.insert(0, '0')
        for s in range(8):
            if S[Oi][Oj][1][s] == 1:
                temp_k[s] = k[Oi][Oj][s]
        dec = 0
        for i in range(len(temp_k)-1,-1,-1):
           dec = dec + int(temp_k[i])*2**(7-i)
        random_img2[Oi][Oj] = dec

cv2.imwrite('Cover2.pgm', random_img2)
cover2 = cv2.imread('Cover2.pgm', 0)
cv2.imshow('Cover2', cover2)

#Recovery

k_rev = [[0 for Ij in range(secret.shape[1])] for Ii in range(secret.shape[0])]


for Ii in range(random_img1.shape[0]):
    for Ij in range(random_img1.shape[1]):
        k_rev[Ii][Ij] = random_img1[Ii][Ij] ^ random_img2[Ii][Ij]


k_rev = np.array(k_rev)

cv2.imwrite('Chang_recovered.pgm', k_rev)
rec = cv2.imread('Chang_recovered.pgm',0)
cv2.imshow('recovered', rec)
print (rec)
'''
for i in range(secret.shape[0]):
    for j in range(secret.shape[1]):
        print(k[i][j])


for i in range(secret.shape[0]):
    for j in range(secret.shape[1]):
        print(k_rev[i][j])

'''

