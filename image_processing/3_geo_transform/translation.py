############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img= cv2.imread('lionBMP.jpg')
rows,cols, channels = img.shape
############################################

############################################
## Do the processing
############################################
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

############################################
## Show the image
cv2.imshow('image',img)
cv2.imshow('transform', dst)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
