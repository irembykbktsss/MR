import cv2
import numpy as np

frame = cv2.imread('Y18.jpg',0)
#Numpy ile kernel matris tanımı
kernelMat = np.ones((15,15),np.uint8)
#Aşındırma işlemi
closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernelMat)
morfolojik_gradient = cv2.morphologyEx(closing, cv2.MORPH_GRADIENT, kernelMat)

cv2.imshow("Morfolojik", morfolojik_gradient)
cv2.waitKey(0)
