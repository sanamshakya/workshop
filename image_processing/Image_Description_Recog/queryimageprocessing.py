import cv2
import numpy as np
import time
import os
import sys
import imagepreprocess as ipp
import feature_extract as fe
import xml.etree.ElementTree as et
from xml.etree.ElementTree import Element, tostring, parse

def process(image_name):
    try:
        image = cv2.imread(image_name, -1)
        edge_image, hist = ipp.preprocess(image)
        feat_h = fe.feature_generation(edge_image)
        feat_ht = np.transpose(feat_h)
        doc = parse("hog.xml")
        root = doc.getroot()
        names = []
        colors = []
        hog_desc = []
        #print root.tag
        for child in root:
            #print child.tag
            for c in child:
                #print c.tag, c.attrib
                if(c.tag == "name"):
                    names.append(c.get("num"))
                    #print names
                if(c.tag == "colors"):
                    colors.append(c.get("num"))
                if(c.tag == "desc"):
                    hog_desc.append(c.get("num"))

        #print colors
        for clr in colors:
            #print type(clr)
            c2 = [float(line) for line in clr[1:-1].split(',')]
            #print c2
            Rc = np.correlate(c2,hist,'full')
            #print max(R)

        D = None
        M = None
        for desc in hog_desc:
            print desc[1:-1].count(',')

            
            
                    
        cv2.imshow("Image",edge_image)
        cv2.waitKey(0)
    except(ValueError,IndexError) as e:
        print e

def main():
    path = "D:\\First5Dayworkshop2017\\PresentationImages\\QuerySample\\"
    process(path+"toy8.jpg")

if __name__ == "__main__":
    main()
