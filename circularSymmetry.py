# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:02:02 2023

@author: tandeitnik

this code checks the circular symmetry of a 2D image
"""

import numpy as np
import os
import imageio.v3 as iio
import matplotlib.pyplot as plt

rootFolder = r"D:\photos" #where the files are saved
res = 100 #resolution of the circle used to evaluate symmetry

root, dump, files = next(os.walk(rootFolder))

file = os.path.join(root,files[0]) #getting name of the file
im = np.array(iio.imread(file)) #importing file

row, col = im.shape
x = np.linspace(0,col-1,col)
y = np.linspace(0,row-1,row)
X,Y = np.meshgrid(x,y)
centX = int(np.sum(X*im)/np.sum(im)) #central column
centY = int(np.sum(Y*im)/np.sum(im)) #central row

theta = np.linspace(0,2*np.pi,res)
r = np.linspace(1,1000,1000)
stds = []

for j in range(len(r)):
    
    if (centX + r[j] >= col) or (centY + r[j] >= row) or (centX - r[j] < 0) or (centY - r[j] < 0): #if the circle is bigger than the image
        
        break
    
    pointsInCircle = np.zeros(res)
    
    for i in range(res):
        
        pointsInCircle[i] = im[int(centY + r[j]*np.sin(theta[i])),int(centX + r[j]*np.cos(theta[i]))]
        
    stds.append(np.std(pointsInCircle)) #the std will be low if there is circular simmetry

meanStds = np.mean(stds)
stdStds = np.std(stds)

#for circular symmetry, you want the mean as close as possible of 0 with minimum spread
print(r"circular symmetry = %.3f +- %.3f" % (meanStds, stdStds))

