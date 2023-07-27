# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:21:53 2023

@author: tandeitnik

this code evaluates the average of a set of images by cropping each image around
its centroid and taking the mean.
"""

import numpy as np
import os
import imageio.v3 as iio
import matplotlib.pyplot as plt
from tqdm import tqdm

rootFolder = r"D:\leeHolograms\correctionHologram\photos" #where the files are saved
boxLengthX = 170 #horizontal length of the cropping box
boxLengthY = 170 #vertical length of the cropping box


root, dump, files = next(os.walk(rootFolder))
meanImage = np.zeros([boxLengthY,boxLengthX])

for i in tqdm(range(len(files))):
    
    file = os.path.join(root,files[i]) #getting name of the file
    im = np.array(iio.imread(file)) #importing file
    
    #getting centroid
    r, c = im.shape
    x = np.linspace(0,c-1,c)
    y = np.linspace(0,r-1,r)
    X,Y = np.meshgrid(x,y)
    centX = int(np.sum(X*im)/np.sum(im)) #central column
    centY = int(np.sum(Y*im)/np.sum(im)) #central row
    
    #cropping and summing to the mean
    centeredImage = im[int(centY-boxLengthY/2):int(centY+boxLengthY/2), int(centX-boxLengthX/2):int(centX+boxLengthX/2)]
    meanImage += centeredImage
    
meanImage = meanImage/len(files) #final result

plt.imshow(meanImage) #plotting the final result
