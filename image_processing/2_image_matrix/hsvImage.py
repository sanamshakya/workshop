
############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img= cv2.imread('color_image.jpg')
print "original image matrix = ", img.shape
############################################

############################################
## Do the processing
############################################
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print "hsv image matrix = ", hsv.shape

(width, height, channel)= hsv.shape
canvas = np.zeros((width,height), np.uint8)

canvas = hsv[:, :, 2]
############################################
## Show the image
cv2.imshow('image',img)
cv2.imshow('value', canvas)
############################################

############################################
## Close and exit
while(1):
       key= cv2.waitKey(1)
       if (key & 0xFF) == 27:
           break

cv2.destroyAllWindows()
############################################
