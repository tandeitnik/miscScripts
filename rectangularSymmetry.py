# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:53:31 2023

@author: tandeitnik

this code checks the rectangular symmetry of a 2D image
"""

import numpy as np
import os
import imageio.v3 as iio
import matplotlib.pyplot as plt

rootFolder = r"D:\photos" #where the files are saved

root, dump, files = next(os.walk(rootFolder))

file = os.path.join(root,files[-1]) #getting name of the file
im = np.array(iio.imread(file)) #importing file

r, c = im.shape
x = np.linspace(0,c-1,c)
y = np.linspace(0,r-1,r)
X,Y = np.meshgrid(x,y)
centX = int(np.sum(X*im)/np.sum(im)) #central column
centY = int(np.sum(Y*im)/np.sum(im)) #central row

plt.imshow(im)
plt.scatter(centX,centY)

if centX <= c/2 and centY <= r/2:
    
    centeredImage = im[0:2*centY,0:2*centX]
    
elif centX <= c/2 and centY > r/2:
    
    centeredImage = im[r-2*(r-centY):r,0:2*centX]
    
elif centX > c/2 and centY <= r/2:
    
    centeredImage = im[0:2*centY,c-2*(c-centX):c]
    
elif centX > c/2 and centY > r/2:
    
    centeredImage = im[r-2*(r-centY):r,c-2*(c-centX):c]

xSymmetry = np.fliplr(centeredImage+0.1)/(centeredImage+0.1) #checks parity simmetry alonx x
ySymmetry = np.flipud(centeredImage+0.1)/(centeredImage+0.1) #checks parity simmetry along y

meanXsymmetry = np.mean(xSymmetry)
stdXsymmetry = np.std(xSymmetry)

meanYsymmetry = np.mean(ySymmetry)
stdYsymmetry = np.std(ySymmetry)

#for retangular symmetry, you want the means as close as possible of 1 with minimum spread
print(r"x symmetry = %.3f +- %.3f" % (meanXsymmetry, stdXsymmetry))
print(r"y symmetry = %.3f +- %.3f" % (meanYsymmetry, stdYsymmetry))
