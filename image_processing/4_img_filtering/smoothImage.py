############################################
## Import OpenCV
import numpy
import cv2
############################################

############################################
## Read the image
img = cv2.imread('noisyImage.png')
############################################

############################################
## Do the processing
blur1 = cv2.GaussianBlur(img,(5,5),0)
blur2 = cv2.blur(img,(5,5))
blur3 = cv2.medianBlur(img,5)
############################################

############################################
## Show the image
cv2.imshow('image',blur3)
cv2.imshow('original',img)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
