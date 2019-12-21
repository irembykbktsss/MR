import cv2
import numpy as np
from matplotlib import pyplot as plt
import pydicom
#import Image
import pylab
import numpy.matlib
import sys
from PIL import Image

#dFile=pydicom.read_file("TCGA-02-0003/06-08-1997-MRI BRAIN WWO CONTRAMR-81239/1-3-P Localizer-98688/000000.dcm") #path to filepython -m pip install matplotlib
#pylab.imshow(dFile.pixel_array,cmap=pylab.cm.bone) # pylab readings and conversion
#pylab.show() #Dispaly

import sys
from PIL import Image

images = map(Image.open, ['000000.jpg', '000001.jpg', '000002.jpg','000003.jpg','000004.jpg'])
images2 = map(Image.open, ['000005.jpg', '000006.jpg', '000007.jpg','000008.jpg','000009.jpg'])

new_im = Image.new('RGB', (1250,250)) #creates a new empty image, RGB mode, and size 444 by 95
new_im2 = Image.new('RGB', (1250,250))
new_im3 = Image.new('RGB' , (1250,250))

import sys
from PIL import Image

images = map(Image.open, ['000000.jpg', '000001.jpg', '000002.jpg' , '000003.jpg', '000004.jpg' , '000005.jpg', '000006.jpg', '000007.jpg','000008.jpg' , '000009.jpg'])
images2 = map(Image.open, ['000005.jpg', '000006.jpg', '000007.jpg','000008.jpg' , '000009.jpg'])

new_im = Image.new('RGB', (1250,250)) 
new_im2 = Image.new('RGB', (1250,250)) 
new_im3 = Image.new('RGB', (1250,250)) 

""""
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
    """"

x_offset = 0
y_offset = 0
for im in range(len(images)):
    for im2 in range(len(images[im]))
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
    new_im2.paste(im2, (y_offset,0))
    y_offset += im2.size[0]


new_im2.save('test.jpg')

"""
y_offset = 0
for im2 in images2:
  new_im2.paste(im2, (y_offset,0))
  y_offset += im2.size[0]

new_im2.save('test2.jpg')

new_im.paste(new_im2 , (4,5))
new_im.save('test3.jpg')

"""



 


#########################################################################################################
"""
image = cv2.imread('test.jpg')
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