import cv2
import numpy as np
import time
import os
import sys

#code courtesy: answer 24 on https://stackoverflow.com/questions/6090399/get-hog-image-features-from-opencv-python
def feature_generation(image):
    winSize = (64,64)
    blockSize = (16,16)
    blockStride = (8,8)
    cellSize = (8,8)
    nbins = 9
    derivAperture = 1
    winSigma = 4.
    histogramNormType = 0
    L2HysThreshold = 2.0000000000000001e-01
    gammaCorrection = 0
    nlevels = 64
    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,
                            histogramNormType,L2HysThreshold,gammaCorrection,nlevels)
    winStride = (8,8)
    padding = (16,16)
    locations = ((0,0),)
    h = hog.compute(image,winStride,padding,locations)
    #hog.save("hog.xml")
    #print h.shape
    return h

def main():
    None
    
if __name__ == "__main__":
    main()
