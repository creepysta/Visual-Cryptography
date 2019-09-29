import cv2
import random

class lockA(object):
    def __init__(self, filename):
        self.filename = filename

    def lock(self):
        secret = cv2.imread(self.filename, 0)
        rows = secret.shape[0]
        cols = secret.shape[1]

        mr = rows*cols - (rows-2)*(cols-2)
        layers = min(rows, cols) // 2
        flat = [0 for i in range(rows*cols)]


        f = open('lockA_secret.txt', 'w')

        c = 0
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
            key = random.randint(0,1)
            offset_val = random.randint(1, mr - 1)
            st = rows*cols - (rows-2)*(cols-2)
            if not key:
                for rj in range(st):
                    # rotating the layer
                    rotated[ri+rj] = flat[ri+(rj+offset_val)%st]
            else:
                for rj in range(st):
                    # rotating the layer
                    rotated[ri+(rj+offset_val)%st] = flat[ri+rj]
            if not min(rows, cols):
                break
            ri += rows*cols - (rows-2)*(cols-2)
            rows, cols = rows -2, cols -2
            f.write(str(key) + " " + str(offset_val) + '\n')

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

        f.close()

        cv2.imwrite('lockA_rotate.pgm',secret)
        #enc = cv2.imread('lockA_rotate.pgm',0)
        #cv2.imshow('rot.pgm', enc)

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

if __name__ == '__main__':
    lA = lockA('lena_gray.bmp')
    lA.lock()

