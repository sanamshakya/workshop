
############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img= cv2.imread('pcb_cropped.jpeg',0)
############################################



############################################
## Do the processing
############################################

kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)

opening = cv2.dilate(erosion, kernel, iterations = 1)
closing = cv2.erode(dilation, kernel, iterations = 1)


############################################
## Show the image
cv2.imshow('image',img)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
