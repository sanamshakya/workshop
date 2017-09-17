import cv2
import numpy as np
import time
import os
import sys
from sklearn.cluster import KMeans
from sklearn import metrics

def preprocess(image):
    image_256x256 = cv2.resize(image,(128,128))
    colors = getcolors(image_256x256)
    #print colors
    image_gray = cv2.cvtColor(image_256x256,cv2.COLOR_BGR2GRAY)
    image_cleanup = cv2.medianBlur(image_gray,3)
    edges = cv2.Canny(image_cleanup,50,180)
    return edges, colors

#code courtesy: http://www.alanzucconi.com/2015/05/24/how-to-find-the-main-colours-in-an-image/
def getcolors(image):
    image_array = image.reshape((image.shape[0] * image.shape[1], 3))
    clusters = KMeans(n_clusters = 8)
    clusters.fit(image_array)
    
    hist = centroid_histogram(clusters)
 
    # Sort the clusters according to how many pixel they have
    zipped = zip (hist, clusters.cluster_centers_)
    zipped.sort(reverse=True, key=lambda x : x[0])
    hist, clusters.cluster_centers = zip(*zipped)

    return hist
     
def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def main():
    None
    
if __name__ == "__main__":
    main()
