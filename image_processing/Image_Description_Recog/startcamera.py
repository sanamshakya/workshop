import cv2
import numpy as np
import time
import os
import sys
import imagepreprocess as ipp
import feature_extract as fe
import xml.etree.ElementTree as et
from xml.etree.ElementTree import Element, tostring, parse
import matplotlib
from matplotlib import pyplot as pp
from skimage.feature import hog
from skimage import data, color, exposure

def process(path):
    path_query = "D:\\First5Dayworkshop2017\\PresentationImages\\QuerySample\\toy8.jpg" #parakeet1.jpg
    image = cv2.imread(path_query, -1)
    edge_image, hist = ipp.preprocess(image)
    feat_h = fe.feature_generation(edge_image)
    name = os.listdir(path)
    Hist_colors = []
    Desc = []
    name_arr = []
    for n in name:
        hist2 = []
        feat_h2 = []
        image2 = cv2.imread(path+n, -1)
        edge_image2, hist2 = ipp.preprocess(image2)
        feat_h2 = fe.feature_generation(edge_image2)
        ch = np.corrcoef(hist,hist2)
        #print ch[0,1]
        cf = np.corrcoef(np.transpose(feat_h),np.transpose(feat_h2))
        #print cf[0,1]
        Hist_colors.append(ch[0,1])
        Desc.append(cf[0,1])
        name_arr.append(n)

    d_arr = np.asarray(Desc)
    pics_idx = np.where(d_arr >= (0.85*d_arr.max()))#0.85 for toy8.jpg
    #print d_arr.max()
    h_arr = np.asarray(Hist_colors)
    n_arr = []
    #print d_arr
    pics_hist_idx = np.where(h_arr>=(0.95*h_arr.max()))#0.85 for toy8.jpg
    #print pics_hist_idx, pics_idx
    for i in range(0,len(pics_idx[0])):
        for j in range(0,len(pics_hist_idx[0])):
            if(pics_idx[0][i]==pics_hist_idx[0][j]):
                n_arr.append(name_arr[pics_idx[0][i]])

    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    fd,hog_image = hog(image_gray, 9, (32, 32), (3, 3), 'L2-Hys', True, False, True)
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))
    cv2.imshow("hog",hog_image_rescaled)
    cv2.waitKey(0)
    pp.subplot(1,2,1),pp.imshow(cv2.cvtColor(cv2.imread(path_query,-1),cv2.COLOR_BGR2RGB)),pp.title('Query Image')
    pp.subplot(1,2,2),pp.imshow(hog_image_rescaled,'gray'),pp.title('HOG of Query Image')
    pp.show()

    print len(n_arr)
    
    
def main():
    path = "D:\\First5Dayworkshop2017\\PresentationImages\\all\\"
    d = process(path)
    

if __name__ == "__main__":
    main()
