############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img= cv2.imread('lionBMP.jpg')
rows,cols,channels = img.shape
############################################

############################################
## Do the processing
############################################
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
############################################
## Show the image
cv2.imshow('image',img)
cv2.imshow('transform', dst)
cv2.imwrite('transformLion.jpg',dst) #saving the transformed image
############################################

############################################
## Close and exit
while(1):
       key= cv2.waitKey(1)
       if (key & 0xFF) == 27:
           break

cv2.destroyAllWindows()
############################################
