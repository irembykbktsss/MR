import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy import*
import sys
from PIL import Image

"""
images = map(Image.open, ['000000.jpg', '000001.jpg', '000002.jpg','000003.jpg','000004.jpg'])
images2 = map(Image.open, ['000005.jpg', '000006.jpg', '000007.jpg','000008.jpg','000009.jpg'])
images3 = map(Image.open, ['000010.jpg', '000011.jpg', '000012.jpg','000013.jpg','000014.jpg'])
images4 = map(Image.open, ['000015.jpg', '000016.jpg', '000017.jpg','000018.jpg','000019.jpg'])
images5 = map(Image.open, ['000020.jpg', '000021.jpg', '000022.jpg'])


new_im = Image.new('RGB',  (1250,1250)) 
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


k_offset = 0
for im5 in images5:
  new_im5.paste(im5, (k_offset,0))
  k_offset += im5.size[0]

new_im.paste(new_im2,  (0,250))
new_im.paste(new_im3 , (0,500))
new_im.paste(new_im4 , (0,750))
new_im.paste(new_im5 , (0,1000))
new_im.save('Hasta3.jpg')

"""
#########################################################################################################
"""
image = cv2.imread('Hasta1y.jpg')                     #orijinal görüntü
cv2.imshow('Original', image)
"""
image = cv2.imread('Hasta11y.jpg')
plt.title('Orijinal')
plt.imshow(image)
plt.show()

########################################################################################################

bilateral_filtered_image = cv2.bilateralFilter(image, 5, 175, 175)    #GÖRÜNTÜ BULANIKLAŞTIRMA
#cv2.imshow('Bilateral', bilateral_filtered_image)
#cv2.waitKey(0)
plt.title('Bilateral Image')
plt.imshow(bilateral_filtered_image)
plt.show()

########################################################################################################

ret,thresh1 = cv2.threshold(bilateral_filtered_image,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(bilateral_filtered_image,127,255,cv2.THRESH_BINARY_INV)    #THRESHOLDİNG İŞLEMİİ
ret,thresh3 = cv2.threshold(bilateral_filtered_image,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(bilateral_filtered_image,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(bilateral_filtered_image,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [image, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):                                                                          
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show() 

#######################################################################################################

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)
#kernel = np.ones((5,5),np.uint8)                                  #EROSION

erosion = cv2.erode(thresh4 ,kernel,iterations = 1) 
#cv2.imshow('Erosion',erosion)
#cv2.waitKey(0)
plt.title('Erosion')
plt.imshow(erosion)
plt.show()


erosion2 = cv2.erode(erosion ,kernel,iterations = 1)                                   #EROSION
#cv2.imshow('Erosion',erosion2)
#cv2.waitKey(0)
plt.title('Erosion2')
plt.imshow(erosion2)
plt.show()

#########################################################################################################

gradient = cv2.morphologyEx(erosion2, cv2.MORPH_GRADIENT, kernel)     #GRADIENT
#cv2.imshow('Gradient',gradient)
#cv2.waitKey(0)
plt.title('Gradient')
plt.imshow(gradient)
plt.show()

#########################################################################################################

edge_detected_image = cv2.Canny(gradient, 75, 200)                   #EDGE DETECTION
#cv2.imshow('Edge', edge_detected_image)
#cv2.waitKey(0)
plt.title('Edge Detection')
plt.imshow(edge_detected_image)
plt.show()

########################################################################################################

contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                                                                                    #CONTOURS
contour_list = []
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
        contour_list.append(contour)

k = cv2.drawContours(gradient, contour_list,  -1, (65,0 ,200), 2)
#cv2.imshow('Objects Detected',gradient)
#cv2.waitKey(0)
plt.title('Contours')
plt.imshow(gradient)
plt.show()

#######################################################################################################
"""
erosion2 = cv2.erode(k ,kernel,iterations = 1)                                   #EROSION
#cv2.imshow('Erosion',erosion2)
#cv2.waitKey(0)
plt.title('Erosion')
plt.imshow(erosion2)
plt.show()

"""