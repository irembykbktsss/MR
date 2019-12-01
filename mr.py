import cv2
import numpy as np
from matplotlib import pyplot as plt

# Reading in and displaying our image
image = cv2.imread('Y9.jpg')
cv2.imshow('Original', image)
# Create our shapening kernel, it must equal to one eventually
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])                              #GÖRÜNTÜ KESKİNLEŞTİRME 
# applying the sharpening kernel to the input image & displaying it.
sharpened = cv2.filter2D(image, -1, kernel_sharpening)
cv2.imshow('Image Sharpening', sharpened)

img_median = cv2.medianBlur(sharpened, 5) # Add median filter to image         #GÖRÜNTÜ BULANIKLAŞTIRMA

cv2.imshow('median filter', img_median) # Display img with median filter
cv2.waitKey(0)        # Wait for a key press to
cv2.destroyAllWindows # close the img window.



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

opening1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernelMat)
opening2 = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernelMat)
opening3 = cv2.morphologyEx(thresh3, cv2.MORPH_OPEN, kernelMat)
opening4= cv2.morphologyEx(thresh4, cv2.MORPH_OPEN, kernelMat)                              #MORFOLOJİK İŞLEMLER
opening5= cv2.morphologyEx(thresh5, cv2.MORPH_OPEN, kernelMat)
titles2 = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images2 = [image, opening1, opening2, opening3, opening4, opening5]
for j in range(6):                                                                          
    plt.subplot(2,3,j+1),plt.imshow(images2[j],'gray')
    plt.title(titles[j])
    plt.xticks([]),plt.yticks([])
plt.show()


#cv2.imshow("Opening", opening)
