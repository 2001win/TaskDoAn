from os import path
import numpy as np
import cv2
import glob

"""Tính trung bình size ảnh"""

sumWidth = 0
sumHeight = 0
#D:\My Dataset\Classification\Butterfly
path = glob.glob('Train\Butterfly\*.jpg')
print(path)
cv_img = []
for img in path:
    n = cv2.imread(img)
    #print(n.shape)
    cv_img.append(n)
    sumWidth += np.size(n,0)
    sumHeight += np.size(n,1) 
print(sumWidth//len(cv_img))
print(sumHeight//len(cv_img))