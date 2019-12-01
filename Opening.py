import cv2
import numpy as np

frame = cv2.imread('Y195.jpg',0)
#Numpy ile kernel matris tanımı
kernelMat = np.ones((15,15),np.uint8)
#Aşındırma işlemi
opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernelMat)
#morfolojik_gradient = cv2.morphologyEx(opening, cv2.MORPH_GRADIENT, kernelMat)

cv2.imshow("Morfolojik", opening)
cv2.waitKey(0)


