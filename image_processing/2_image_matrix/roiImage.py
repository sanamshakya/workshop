############################################
## Import OpenCV
import numpy
import cv2
############################################

############################################
## Read the image
img = cv2.imread('lion.jpg')
print img.shape
h,w,c = img.shape
left_half = img[:,:(w/2),:]
print left_half.shape
############################################

############################################
## Do the processing
############################################

############################################
## Show the image
cv2.imshow('image',left_half)
############################################

############################################
## Close and exit
while(1):
       key= cv2.waitKey(1)
       if (key & 0xFF) == 27:
           break

cv2.destroyAllWindows()
############################################
