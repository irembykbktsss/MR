import cv2
import numpy as np
from matplotlib import pyplot as plt
import pydicom
#import Image
import pylab
import numpy.matlib
import sys
from PIL import Image



images = map(Image.open, ['000000.jpg', '000001.jpg', '000002.jpg','000003.jpg','000004.jpg'])
images2 = map(Image.open, ['000005.jpg', '000006.jpg', '000007.jpg','000008.jpg','000009.jpg'])
images3 = map(Image.open, ['000010.jpg', '000011.jpg', '000012.jpg','000013.jpg','000014.jpg'])
images4 = map(Image.open, ['000015.jpg', '000016.jpg', '000017.jpg','000018.jpg','000019.jpg'])
images5 = map(Image.open, ['000020.jpg', '000021.jpg', '000022.jpg'])

new_im = Image.new('RGB', (1250,1250)) 
new_im2 = Image.new('RGB', (1250,1250))
new_im3 = Image.new('RGB', (1250,1250))
new_im4 = Image.new('RGB', (1250,1250))
new_im5 = Image.new('RGB', (1250,1250))


x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

y_offset = 0
for im2 in images2:
  new_im2.paste(im2, (y_offset,0))
  y_offset += im2.size[0]

z_offset = 0
for im3 in images3:
  new_im3.paste(im3, (z_offset,0))
  z_offset += im3.size[0]

t_offset = 0
for im4 in images4:
  new_im4.paste(im4, (t_offset,0))
  t_offset += im4.size[0]

v_offset = 0
for im5 in images5:
  new_im5.paste(im5, (v_offset,0))
  v_offset += im5.size[0]

new_im.paste(new_im2,(0,250))
new_im.paste(new_im3 , (0,500))
new_im.paste(new_im4, (0,750))
new_im.paste(new_im5, (0,1000))
new_im.save('Hasta5.jpg')


#########################################################################################################

image = cv2.imread('Hasta5.jpg')
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
"""
bilateral_filtered_image = cv2.bilateralFilter(opening3, 5, 175, 175)
cv2.imshow('Bilateral', bilateral_filtered_image)
cv2.waitKey(0)
"""

edge_detected_image = cv2.Canny(opening5, 75, 200)                #EDGE DETECTION
cv2.imshow('Edge', edge_detected_image)
cv2.waitKey(0)

######################################################################################################

contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                                                                       #CONTOURS
contour_list = []
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
        contour_list.append(contour)

cv2.drawContours(opening5, contour_list,  -1, (65,0 ,100), 2)
cv2.imshow('Objects Detected',opening5)
cv2.waitKey(0)