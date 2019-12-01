import cv2
import numpy as np

frame = cv2.imread('Y195.jpg',0)
cv2.imshow("orjinal",frame)

#Numpy ile kernel matris tanımı
kernel = np.ones((5,5),np.uint8)
#Aşındırma işlemi
sonuc = cv2.erode(frame,kernel,iterations = 1)
cv2.imshow("Sonuc", sonuc)




#frame = cv2.imread('Y195.jpg',0)
#cv2.imshow("orjinal",frame)
#Numpy ile kernel matris tanımı
kernel1 = np.ones((15,15),np.uint8)
#Aşındırma işlemi
sonuc1 = cv2.dilate(sonuc,kernel1,iterations = 1)
cv2.imshow("Sonuc1", sonuc1)
cv2.waitKey(0)