############################################
## Import OpenCV
import numpy
import cv2
############################################

############################################
## Read the image
img = cv2.imread('lion.jpg')
############################################

############################################
## Do the processing
height, width, channels = img.shape
res = cv2.resize(img,(width/2, height/2), interpolation = cv2.INTER_CUBIC)
############################################

############################################
## Show the image
cv2.imshow('image',res)
cv2.imshow('original', img)
############################################

############################################
## Close and exit
while(1):
   key= cv2.waitKey(1)
   if (key & 0xFF) == 27:
       break

cv2.destroyAllWindows()
############################################
