import cv2
import random

class lockB(object):
    def __init__(self, filename):
        self.filename = filename
    
    def lock(self):
        secret = cv2.imread(self.filename, 0)
        rows = secret.shape[0]
        cols = secret.shape[1]
        randKey = random.randint(100,250)

        f = open('lockB_secret.txt', 'w')
        f.write(str(randKey)+'\n')

        mr = rows*cols - (rows-2)*(cols-2)
        layers = min(rows, cols) // 2

        flat = [0 for i in range(rows*cols)]
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
        while(True):
            key = random.randint(0, 1)
            offset_val = random.randint(1, mr - 1)
            pixel_offset = offset_val % 8  # 1#offset_val % 7 + 1
            st = rows*cols - (rows-2)*(cols-2)
            for rj in range(st):
                # rotating the pixels
                if not key:
                    flat[ri+rj] = (flat[ri+rj] <<
                                   pixel_offset) | (flat[ri+rj] >> (8-pixel_offset))
                    flat[ri+rj] ^= randKey
                else:
                    flat[ri+(rj+offset_val) % st] = (flat[ri+(rj+offset_val) % st] >>
                                                     pixel_offset) | (flat[ri+(rj+offset_val) % st] << (8-pixel_offset))
                    flat[ri+(rj+offset_val) % st] ^= randKey
            if not min(rows, cols):
                break
            ri += rows*cols - (rows-2)*(cols-2)
            rows, cols = rows - 2, cols - 2
            f.write(str(key) + " " + str(offset_val) + '\n')

        c = 0
        rows = secret.shape[0]
        cols = secret.shape[1]

        for i in range(layers):
            for j in range(i, cols-i):
                secret[i][j] = flat[c]
                c += 1
            for j in range(i+1, rows - i):
                secret[j][cols-i-1] = flat[c]
                c += 1
            for j in range(cols-i-2, i+1, -1):
                secret[rows-i-1][j] = flat[c]
                c += 1
            for j in range(rows-i-2, i, -1):
                secret[j][i] = flat[c]
                c += 1

        f.close()

        cv2.imwrite('lockB_pixel.pgm', secret)
        #enc = cv2.imread('lockB_pixel.pgm', 0)
        #cv2.imshow('rot.pgm', enc)

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

if __name__ == '__main__':
    lb = lockB('lockA_rotate.pgm')
    lb.lock()

