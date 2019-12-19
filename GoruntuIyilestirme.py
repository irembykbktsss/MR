import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('Y1.jpg')
img_median = cv2.medianBlur(image, 5) 

def orijinalImage():
    cv2.imshow('Original', image)    
    cv2.waitKey(0)        
    cv2.destroyAllWindows 


def medianBlur():
    orijinalImage()
    img_median = cv2.medianBlur(image, 5)        #GÖRÜNTÜ BULANIKLAŞTIRMA
    cv2.imshow('median filter', img_median) 
    cv2.waitKey(0)        
    cv2.destroyAllWindows 


def thresholding():
    medianBlur()
    ret,thresh1 = cv2.threshold(img_median,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(img_median,127,255,cv2.THRESH_BINARY_INV)                   #THRESHOLDİNG İŞLEMİİ
    ret,thresh3 = cv2.threshold(img_median,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(img_median,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(img_median,127,255,cv2.THRESH_TOZERO_INV)
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [image, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in range(6):                                                                          
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

    kernelMat = np.ones((15,15),np.uint8)

thresholding()



        

    