import cv2
import os
import numpy
import math
from lockA import lockA
from lockB import lockB
from unlockA import unlockA
from unlockB import unlockB

res = open('result.txt', 'w')

for f in os.listdir():
    name = os.path.basename(f)
    if '.pgm' in name or '.bmp' in name:
        la = lockA(name)
        la.lock()
        lb = lockB('lockA_rotate.pgm')
        lb.lock()
        ua = unlockA('lockB_pixel.pgm')
        ua.unlock()
        ub = unlockB('unlockA_img.pgm')
        ub.unlock()

        original = cv2.imread(name)
        contrast = cv2.imread('restored.pgm')
        #Computing PNSR
        mse = numpy.mean((original-contrast)**2)
        if mse==0:
            psnr = 100
        else:
            psnr = 20 * math.log10(255.0/math.sqrt(mse))
        res.write(str(name) + '\t' + str(psnr) + '\n')

res.close()

