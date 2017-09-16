############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img= cv2.imread('lionBMP.jpg')
rows,cols,ch = img.shape
############################################

############################################
## Do the processing
############################################
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))


############################################
## Show the image
cv2.imshow('input',img)
cv2.imshow('output', dst)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
