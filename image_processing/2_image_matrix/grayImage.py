
############################################
## Import OpenCV
import numpy
import cv2
############################################

############################################
## Read the image
img = cv2.imread('lionBMP.jpg')
############################################

############################################
## Do the processing
print img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print gray.shape
############################################

############################################
## Show the image
cv2.imshow('image',gray)
cv2.imwrite("grayLion.jpg", gray)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
