############################################
## Import OpenCV
import numpy
import cv2
############################################

############################################
## Read the image
img = cv2.imread('test_image.jpg')
print img.shape

cv2.imshow('image_whole',img)

#img[:,:,0]=0 #Blue channel of image
img[:,:,1]=0 #Green channel of image
img[:,:,2]=0 #Red channel of image



############################################

############################################
## Do the processing
############################################

############################################
## Show the image
cv2.imshow('image_split',img)

############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
