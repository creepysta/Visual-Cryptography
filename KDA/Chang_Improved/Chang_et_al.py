import cv2
import random
import numpy as np

secret = cv2.imread('aya_matsuura.pgm', 0)
random_img1 = cv2.imread('azumi_kawashima2.pgm',0)
random_img2 = cv2.imread('brian_kernighan.pgm',0)


# encryption
total_pixels = secret.shape[0]*secret.shape[1]

# generating an random number for each pixel
randList = [[random.randint(1, 9) for j in range(secret.shape[1])] for i in range(secret.shape[0])]

# Sn*m : m = 9 and n = 2 for 2 * 2 sharing scheme
S = [[[[0 for j in range(9)] for i in range(2)] for k in range(secret.shape[1])] for l in range(secret.shape[0])]

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
        for zeros in range(8 - len(k)):
            k[Ii][Ij].insert(0, '0')


for Ii in range(secret.shape[0]):
    for Ij in range(secret.shape[1]):
        rand_i = randList[Ii][Ij]
        for ki in range(len(k[Ii][Ij])):
            if ki < rand_i :
                # k[ki] = int(k[ki])
                S[Ii][Ij][1][ki] = S[Ii][Ij][0][ki] ^ int (k[Ii][Ij][ki])
            else :
                # k[ki] = int(k[ki])
                S[Ii][Ij][1][ki+1] = S[Ii][Ij][0][ki+1] ^ int (k[Ii][Ij][ki])


# creating 1B
for Oi in range(random_img1.shape[0]):
    for Oj in range(random_img1.shape[1]):
        for s in range(9):
            if S[Oi][Oj][0][s] == 1:
                S[Oi][Oj][0][s] = random_img1[Oi][Oj]

            
# creating 2B
for Oi in range(random_img2.shape[0]):
    for Oj in range(random_img2.shape[1]):
        for s in range(9):
            if S[Oi][Oj][1][s] == 1:
                S[Oi][Oj][1][s] = random_img2[Oi][Oj]


#Recovery

k_rev = [[[0 for ki in range(8)] for Ij in range(secret.shape[1])] for Ii in range(secret.shape[0])]


for Ii in range(random_img1.shape[0]):
    for Ij in range(random_img1.shape[1]):
        rand_i = randList[Ii][Ij]
        for i in range(8):
            if i < rand_i:
                k_rev[Ii][Ij][i] = S[Ii][Ij][0][i] ^ S[Ii][Ij][1][i]
            else:
                k_rev[Ii][Ij][i] = S[Ii][Ij][0][i+1] ^ S[Ii][Ij][1][i+1]


for i in range(secret.shape[0]):
    for j in range(secret.shape[1]):
        print(k[i][j])


for i in range(secret.shape[0]):
    for j in range(secret.shape[1]):
        print(k_rev[i][j])


