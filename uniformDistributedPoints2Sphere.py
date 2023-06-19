# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:32:05 2023

@author: tandeitnik

This code picks uniformily distributed points on the surface of a 2-sphere.
The first part
"""
import numpy as np
import matplotlib.pyplot as plt

#picking points
N = 1000 #number of points
radius = 1 #radius of the sphere
points = np.random.normal(loc=0.0, scale=1.0, size=(res,3))
normalization = np.diag(points@np.transpose(points))*(1/radius**2)
normPoints = np.transpose(points)/np.sqrt(normalization) #this is the final result, each column is a point on a sphere


#ploting just to show it worked
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
r = 0.05
u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
x = radius*np.cos(u) * np.sin(v)
y = radius*np.sin(u) * np.sin(v)
z = radius*np.cos(v)
ax.plot_surface(x, y, z, cmap=plt.cm.YlGnBu_r, alpha = 0.3)
ax.scatter(normPoints[0,:],normPoints[1,:],normPoints[2,:], alpha = 0.7, color = 'red')
