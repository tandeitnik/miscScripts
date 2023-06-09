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
w0 = 25e-4 #waist
wl = 1550e-9 #wavelength
z = 0

x = np.linspace(0,10.8e-6*911,912)-10.8e-6*911/2
y = np.linspace(0,10.8e-6*1139,1140)-10.8e-6*1139/2
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

x_0 = 10.8e-6*18

w = 1/np.pi*np.arcsin(ampAbsNorm)
p = 1/np.pi*phase

T = 1/2+1/2*np.sign(np.cos(2*np.pi*X/x_0+np.pi*p) - np.cos(np.pi*w))

sns.heatmap(T)
plt.gray()
matplotlib.image.imsave('teste.png', T)
plt.close()