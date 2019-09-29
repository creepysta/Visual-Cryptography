import cv2
import math
import numpy

original = cv2.imread('lena_gray.bmp')
contrast = cv2.imread('restored.pgm')

#Computing PNSR
mse = numpy.mean((original-contrast)**2)
if mse==0:
    psnr = 100
else:
    psnr = 20 * math.log10(255.0/math.sqrt(mse))
print(psnr)
    
