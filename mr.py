import cv2
import numpy as np
from matplotlib import pyplot as plt
import pydicom
import Image
import pylab
import numpy.matlib




dFile=pydicom.read_file("/Users/09531/Desktop/MR/000017.dcm") #path to filepython -m pip install matplotlib
pylab.imshow(dFile.pixel_array,cmap=pylab.cm.bone) # pylab readings and conversion
pylab.show() #Dispaly
    

#########################################################################################################

image = cv2.imread('Y10.jpg')
cv2.imshow('Original', image)

#########################################################################################################

img_median = cv2.medianBlur(image, 5)                                     #GÖRÜNTÜ BULANIKLAŞTIRMA
cv2.imshow('median filter', img_median) 
cv2.waitKey(0)       
cv2.destroyAllWindows 

########################################################################################################

ret,thresh1 = cv2.threshold(img_median,127,255,cv2.THRESH_BINARY)           #THRESHOLDİNG İŞLEMİ
ret,thresh2 = cv2.threshold(img_median,127,255,cv2.THRESH_BINARY_INV)                   
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

#######################################################################################################

opening1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernelMat)            #OPENING İŞLEMİ
opening2 = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernelMat)
opening3 = cv2.morphologyEx(thresh3, cv2.MORPH_OPEN, kernelMat)
opening4= cv2.morphologyEx(thresh4, cv2.MORPH_OPEN, kernelMat)                             
opening5= cv2.morphologyEx(thresh5, cv2.MORPH_OPEN, kernelMat)
titles2 = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images2 = [image, opening1, opening2, opening3, opening4, opening5]
for j in range(6):                                                                          
    plt.subplot(2,3,j+1),plt.imshow(images2[j],'gray')
    plt.title(titles[j])
    plt.xticks([]),plt.yticks([])
plt.show()

######################################################################################################

