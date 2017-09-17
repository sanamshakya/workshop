import cv2
import os
import fcntl
import mmap
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np
import time

cam = PiCamera()
cam.resolution = (320,240)
cam.framerate = 15
raw_cap = PiRGBArray(cam,(320,240))
frame_cnt = 0
frame = cam.capture_continuous(raw_cap,format="bgr",use_video_port=True,splitter_port=2,resize=(320,240))
time.sleep(5.0)
print "done warming up"
while(True):
    image = frame.next()
    color_image = image.array
    cv2.imshow("Video",color_image)
    cv2.waitKey(1)
    raw_cap.truncate(0)
    #raw_cap.seek(0)
    frame_cnt = frame_cnt + 1
    if(frame_cnt> 100):
        break

print "Ending...."
cv2.destroyAllWindows()
#print "now opencv"
#camera = cv2.VideoCapture()
#camera.set(cv2.cv.CV_CAP_PROP_FPS, 15)
#os.system("sudo modprobe bcm2835-v4l2 max_video_width=2952 max_video_height=1944")
#os.system("v4l2-ctl -p 15")
#os.system("v4l2-ctl --set-fmt-video=width=320,height=480,pixelformat=I420")
#camera.open(os.system("v4l2-ctl --stream-mmap=3 --stream-count=1000 --stream-to=/dev/null"))
#ret, frame = camera.read()
#print ret
#frame_cnt = 0
#while(ret):
#    ret, frame = camera.read()
#    cv2.imshow("Video", frame)
#    cv2.waitKey(1)
#    frame_cnt = frame_cnt+1
#    if(frame_cnt > 60):
#        break

#cv2.destroyAllWindows()    
    


