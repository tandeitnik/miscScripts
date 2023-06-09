# -*- coding: utf-8 -*-
"""
Created on Fri May  5 06:45:05 2023

@author: tandeitnik
"""

import numpy as np
from scipy.special import hermite
import seaborn as sns
import matplotlib.pyplot as plt

n = 0
m = 1
w0 = 20e-4 #waist
wl = 1550e-9 #wavelength
z = 0

epsilon0 = 8.854187817e-12
c = 3e8

x = np.linspace((-9855e-6/2),(9855e-6/2),912)
y = np.linspace((-6161.4e-6/2),(6161.4e-6/2),1140)
X, Y = np.meshgrid(x, y)


k = (2*np.pi)/wl
z_r = (k*w0**2)/2
w = w0*np.sqrt(1 + z**2/z_r**2)
H_n = hermite(n, monic = True)
H_m = hermite(m, monic = True)

if z != 0:
    R = (z_r**2 + z**2)/z
    
amplitude = (w0/w)*np.exp(-(X**2+Y**2)/w**2)*H_m(np.sqrt(2)*X/w)*H_n(np.sqrt(2)*Y/w)

if z != 0:
    phase = (-k*(X**2+Y**2))/(2*R) + (1+n+m)*np.arctan2(z,z_r) - k*z - (np.sign(np.sign(amplitude)+0.1)-1)*(np.pi/2)
else:
    phase =  (1+n+m)*np.arctan2(z,z_r) - k*z -  (np.sign(np.sign(amplitude)+0.1)-1)*(np.pi/2)
    
ampAbsNorm = abs(amplitude)/np.max(abs(amplitude))

theta = 24 #degrees
phasePlane = -k*np.sin(theta*(np.pi/180))*X
#hologram = 1 + ampAbsNorm**2 + 2*ampAbsNorm*np.cos(phasePlane-phase)
hologram = 2 + 2*np.cos(phasePlane-phase)

ax = sns.heatmap(hologram)
ax = sns.heatmap(np.arctan2(np.sin(phasePlane),np.cos(phasePlane)))
ax.invert_yaxis()
cmap = sns.cubehelix_palette(255, hue=0.05, rot=0, light=0.9, dark=0, as_cmap=True,reverse=True)
ax = sns.heatmap(hologram, cmap = cmap)
ax.invert_yaxis()

def scaleConv(image,bits):
    
    hValue = 2**bits - 1
    
    return (hValue/(np.max(image)-np.min(image)))*(image - np.min(image))

def floydDithering(image, bits, s = 0):
    
    #if s = 1 it alternates de direction of the lines
    
    hValue = 2**bits - 1
    threshhold = hValue/2
    
    y,x = np.shape(image)
    
    if s == 0:
    
        for i in range(y):
            
            for j in range(x):
                
                oldpixel = image[i,j]
                if oldpixel <= threshhold:
                    newpixel = 0
                else:
                    newpixel = 1

                image[i,j] = newpixel
                quant_error = oldpixel - newpixel*hValue
                if j != x-1:
                    image[i,j+1] = image[i,j+1] + quant_error*(7/16)
                if (i != y-1) and (j != 0):
                    image[i+1,j-1] = image[i+1,j-1] + quant_error*(3/16)
                if i != y-1:
                    image[i+1,j] = image[i+1,j] + quant_error*(5/16)
                if (i != y-1) and (j != x-1):
                    image[i+1,j+1] = image[i+1,j+1] + quant_error*(1/16)
                
    if s == 1:
        
        for i in range(y):
            
            for j in range(x):
                
                if i % 2 == 0:
                
                    oldpixel = image[i,j]
                    if oldpixel <= threshhold:
                        newpixel = 0
                    else:
                        newpixel = 1
                        
                    image[i,j] = newpixel
                    quant_error = oldpixel - newpixel*hValue
                    if j != x-1:
                        image[i,j+1] = image[i,j+1] + quant_error*(7/16)
                    if (i != y-1) and (j != 0):
                        image[i+1,j-1] = image[i+1,j-1] + quant_error*(3/16)
                    if i != y-1:
                        image[i+1,j] = image[i+1,j] + quant_error*(5/16)
                    if (i != y-1) and (j != x-1):
                        image[i+1,j+1] = image[i+1,j+1] + quant_error*(1/16)
                        
                else:
                    
                    oldpixel = image[i,-1 - j]
                    if oldpixel <= threshhold:
                        newpixel = 0
                    else:
                        newpixel = 1
                        
                    image[i,-1 - j] = newpixel
                    quant_error = oldpixel - newpixel*hValue
                    if j != x-1:
                        image[i,-1 - j-1] = image[i,-1 - j-1] + quant_error*(7/16)
                    if (i != y-1) and (j != 0):
                        image[i+1,-1 - j+1] = image[i+1,-1 - j+1] + quant_error*(3/16)
                    if i != y-1:
                        image[i+1,-1 - j] = image[i+1,-1 - j] + quant_error*(5/16)
                    if (i != y-1) and (j != x-1):
                        image[i+1,-1 - j-1] = image[i+1,-1 - j-1] + quant_error*(1/16)
        
    return image
    

def jarvisDithering(image, bits, s = 0):
    
    #if s = 1 it alternates de direction of the lines
    
    hValue = 2**bits - 1
    threshhold = hValue/2
    
    y,x = np.shape(image)
    
    if s == 0:
    
        for i in range(y):
            
            for j in range(x):
                
                oldpixel = image[i,j]
                if oldpixel <= threshhold:
                    newpixel = 0
                else:
                    newpixel = 1

                image[i,j] = newpixel
                quant_error = oldpixel - newpixel*hValue
                if j != x-1:
                    image[i,j+1] = image[i,j+1] + quant_error*(7/48)
                if j < x-2:
                    image[i,j+2] = image[i,j+2] + quant_error*(5/48)
                
                if (i < y-1) and (j >= 2):
                    image[i+1,j-2] = image[i+1,j-2] + quant_error*(3/48)
                if (i < y-1) and (j >= 1):
                    image[i+1,j-1] = image[i+1,j-1] + quant_error*(5/48)
                if (i < y-1):
                    image[i+1,j] = image[i+1,j] + quant_error*(7/48)
                if i < y-1  and (j < x-1):
                    image[i+1,j+1] = image[i+1,j+1] + quant_error*(5/48)
                if (i < y-1) and (j < x-2):
                    image[i+1,j+2] = image[i+1,j+2] + quant_error*(3/48)
                    
                if (i < y-2) and (j >= 2):
                    image[i+2,j-2] = image[i+2,j-2] + quant_error*(1/48)
                if (i < y-2) and (j >= 1):
                    image[i+2,j-1] = image[i+2,j-1] + quant_error*(3/48)
                if (i < y-2):
                    image[i+2,j] = image[i+2,j] + quant_error*(5/48)
                if (i < y-2)  and (j < x-1):
                    image[i+2,j+1] = image[i+2,j+1] + quant_error*(3/48)
                if (i < y-2) and (j < x-2):
                    image[i+2,j+2] = image[i+2,j+2] + quant_error*(1/48)
                
    if s == 1:
        
        for i in range(y):
            
            for j in range(x):
                
                if i % 2 == 0:
                
                    oldpixel = image[i,j]
                    if oldpixel <= threshhold:
                        newpixel = 0
                    else:
                        newpixel = 1
                        
                    image[i,j] = newpixel
                    quant_error = oldpixel - newpixel*hValue
                    if j != x-1:
                        image[i,j+1] = image[i,j+1] + quant_error*(7/48)
                    if j < x-2:
                        image[i,j+2] = image[i,j+2] + quant_error*(5/48)
                    
                    if (i < y-1) and (j >= 2):
                        image[i+1,j-2] = image[i+1,j-2] + quant_error*(3/48)
                    if (i < y-1) and (j >= 1):
                        image[i+1,j-1] = image[i+1,j-1] + quant_error*(5/48)
                    if (i < y-1):
                        image[i+1,j] = image[i+1,j] + quant_error*(7/48)
                    if i < y-1  and (j < x-1):
                        image[i+1,j+1] = image[i+1,j+1] + quant_error*(5/48)
                    if (i < y-1) and (j < x-2):
                        image[i+1,j+2] = image[i+1,j+2] + quant_error*(3/48)
                        
                    if (i < y-2) and (j >= 2):
                        image[i+2,j-2] = image[i+2,j-2] + quant_error*(1/48)
                    if (i < y-2) and (j >= 1):
                        image[i+2,j-1] = image[i+2,j-1] + quant_error*(3/48)
                    if (i < y-2):
                        image[i+2,j] = image[i+2,j] + quant_error*(5/48)
                    if (i < y-2)  and (j < x-1):
                        image[i+2,j+1] = image[i+2,j+1] + quant_error*(3/48)
                    if (i < y-2) and (j < x-2):
                        image[i+2,j+2] = image[i+2,j+2] + quant_error*(1/48)
                        
                else:
                    
                    
                    
                    oldpixel = image[i,-1 - j]
                    if oldpixel <= threshhold:
                        newpixel = 0
                    else:
                        newpixel = 1
                    
                    image[i,-1 - j] = newpixel
                    quant_error = oldpixel - newpixel*hValue
                    
                    if j != x-1:
                        image[i,-1 - j-1] = image[i,-1 - j-1] + quant_error*(7/48)
                    if j < x-2:
                        image[i,-1 - j-2] = image[i,-1 - j-2] + quant_error*(5/48)
                    
                    if (i < y-1) and (j >= 2):
                        image[i+1,-1 - j+2] = image[i+1,-1 - j+2] + quant_error*(3/48)
                    if (i < y-1) and (j >= 1):
                        image[i+1,-1 - j+1] = image[i+1,-1 - j+1] + quant_error*(5/48)
                    if (i < y-1):
                        image[i+1,-1 - j] = image[i+1,-1 - j] + quant_error*(7/48)
                    if i < y-1  and (j < x-1):
                        image[i+1,-1 - j-1] = image[i+1,-1 - j-1] + quant_error*(5/48)
                    if (i < y-1) and (j < x-2):
                        image[i+1,-1 - j-2] = image[i+1,-1 - j-2] + quant_error*(3/48)
                        
                    if (i < y-2) and (j >= 2):
                        image[i+2,-1 - j+2] = image[i+2,-1 - j+2] + quant_error*(1/48)
                    if (i < y-2) and (j >= 1):
                        image[i+2,-1 - j+1] = image[i+2,-1 - j+1] + quant_error*(3/48)
                    if (i < y-2):
                        image[i+2,-1 - j] = image[i+2,-1 - j] + quant_error*(5/48)
                    if (i < y-2)  and (j < x-1):
                        image[i+2,-1 - j-1] = image[i+2,-1 - j-1] + quant_error*(3/48)
                    if (i < y-2) and (j < x-2):
                        image[i+2,-1 - j-2] = image[i+2,-1 - j-2] + quant_error*(1/48)
                    
    return image


hologramBitScale = scaleConv(hologram,8)
hologramBw = jarvisDithering(hologramBitScale,8, s= 1)

# cmap = sns.cubehelix_palette(1, hue=0.05, rot=0, light=0.9, dark=0, as_cmap=True,reverse=True)
# ax = sns.heatmap(hologramBw, cmap = cmap)
# ax.invert_yaxis()

import matplotlib.image
import matplotlib.pyplot as plt
plt.gray()
matplotlib.image.imsave('hermite01_P_24.png', hologramBw)
plt.close()