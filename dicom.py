import cv2
import numpy as np
#import pydicom
#import pylab
#from skimage.filters import median

#dFile=pydicom.read_file("/Users/90531/Desktop/MR/dicom/000015.dcm") #path to file
#pylab.imshow(dFile.pixel_array,cmap=pylab.cm.bone) # pylab readings and conversion
#pylab.show() #Dispaly

#skimage.filters.median(dFile, selem=np.ones((5, 5)))

import SimpleITK as sitk

img = sitk.ReadImage("/Users/90531/Desktop/MR/dicom/000015.dcm")
# rescale intensity range from [-1000,1000] to [0,255]
img = sitk.IntensityWindowing(img, -1000, 1000, 0, 255)
# convert 16-bit pixels to 8-bit
img = sitk.Cast(img, sitk.sitkUInt8)

image = sitk.WriteImage(img, "000015.png")

img_median = cv2.medianBlur(image, 5)                                     #GÖRÜNTÜ BULANIKLAŞTIRMA
cv2.imshow('median filter', img_median) 
cv2.waitKey(0)       
cv2.destroyAllWindows 





