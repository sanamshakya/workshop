############################################
## Import OpenCV
import numpy
import cv2
############################################

############################################
## Read the image
img = cv2.imread('test_image.jpg')
print img.shape

#cv2.imshow('image_whole',img)

#img[:,:,0]=128 #Blue channel of image
#img[:,:,1]=0 #Green channel of image
img[:,:,2]=0 #Red channel of image

img1=img[:,:,0]
print img1.shape
############################################

############################################
## Do the processing
############################################

############################################
## Show the image
#cv2.imshow('image_split',img)
cv2.imshow('image_bk', img1)
############################################

############################################
## Close and exit
while(1):
       key= cv2.waitKey(1)
       if (key & 0xFF) == 27:
           break

cv2.destroyAllWindows()
############################################
