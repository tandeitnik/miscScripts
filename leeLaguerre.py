# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 13:40:18 2023

@author: tandeitnik
"""

from math import factorial
import numpy as np
from scipy.special import eval_genlaguerre
import seaborn as sns
import matplotlib.image
import matplotlib.pyplot as plt

l = 2
p = 1
w_0 = 10e-4 #waist
wl = 1550e-9 #wavelength
z = 0

x = np.linspace(0,10.8e-6*911,912)-10.8e-6*911/2
y = np.linspace(0,10.8e-6*1139,1140)-10.8e-6*1139/2
X, Y = np.meshgrid(x, y)


r = np.sqrt(X**2+Y**2)
phi = np.arctan2(Y,X)

C = np.sqrt((2*factorial(p))/(np.pi*factorial(p+abs(l)))) #normalization constant
k = (2*np.pi)/wl
z_r = (k*w_0**2)/2
w = w_0*np.sqrt(1 + z**2/z_r**2)
laguerre = eval_genlaguerre(p, abs(l), 2*r**2/w**2)


if z != 0:
    R = (z_r**2 + z**2)/z
    
Phi = (2*p+abs(l)+1)*np.arctan2(z,z_r)

amplitude = (C/w)*np.exp(((-r**2)/w**2))*((np.sqrt(2)*r/w)**abs(l))*laguerre

if z != 0:
    phase = (-k*r**2)/(2*R) + Phi + l*phi - k*z -  (np.sign(np.sign(amplitude)+0.1)-1)*(np.pi/2)
else:
    phase =  (Phi + l*phi) - k*z - (np.sign(np.sign(amplitude)+0.1)-1)*(np.pi/2)
    
ampAbsNorm = abs(amplitude)/np.max(abs(amplitude))

x_0 = 10.8e-6*18

w = 1/np.pi*np.arcsin(ampAbsNorm)
p = 1/np.pi*phase

T = 1/2+1/2*np.sign(np.cos(2*np.pi*X/x_0+np.pi*p) - np.cos(np.pi*w))

sns.heatmap(T)
plt.gray()
matplotlib.image.imsave('teste.png', T)
plt.close()