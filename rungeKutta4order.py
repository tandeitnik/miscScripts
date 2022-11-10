#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 08:20:25 2022

@author: tandeitnik
"""


"""
This script implements the Runge-Kutta 4th order method for a 3D system
first-order system where

dv_x/dt = u(x,y,z)
dv_y/dt = g(x,y,z)
dv_z/dt = h(x,y,z)

v_x = dx/dt
v_y = dy/dt
v_z = dz/dt

To implement for 1D or 2D systems is suffices to set the missing functions
to zero
"""

import numpy as np
import matplotlib.pyplot as plt

#Define the functions u, g and h. As an example, below are defined the Lorenz equations
#Note that s, r, and b here are just parameters of the Lorenz equation, you may change
#to parameters suited to your system
def u(x,y,z,s,r,b):
    
    return s*(y-x)

def g(x,y,z,s,r,b):
    
    return r*x - y - x*z

def h(x,y,z,s,r,b):
    
    return x*y - b*z


#The next function evaluates u, g, and h at a given point and returns the values as a vector.
def f(x,y,z,s,r,b):
    
    return np.array([u(x,y,z,s,r,b) , g(x,y,z,s,r,b) , h(x,y,z,s,r,b) ])

#The next function applies an integration step perfoming Runge-Kutta 4th order
def rungeKuttaStep(x,y,z,dt,s,r,b):
    
    k1 = f(x,y,z,s,r,b)*dt
    k2 = f(x+k1[0]*0.5,y+k1[1]*0.5,z+k1[2]*0.5,s,r,b)*dt
    k3 = f(x+k2[0]*0.5,y+k2[1]*0.5,z+k2[2]*0.5,s,r,b)*dt
    k4 = f(x+k3[0],y+k3[1],z+k3[2],s,r,b)*dt
    
    newPositions = np.array([x,y,z]) + 1/6*(k1+2*k2+2*k3+k4)
    
    return newPositions

#The next funcion applies the Runge-Kutta method the desired time interval
#[x0,y0,z0] are the initial positions
def rungeKutta(x0,y0,z0,dt,tMax,s,r,b):
    
    positions = np.zeros([3,int(tMax/dt)])
    positions[0,0] = x0
    positions[1,0] = y0
    positions[2,0] = z0
    
    for i in range(1,int(tMax/dt)):
        
        newPositions = rungeKuttaStep(positions[0,i-1],positions[1,i-1],positions[2,i-1],dt,s,r,b)
        positions[0,i] = newPositions[0]
        positions[1,i] = newPositions[1]
        positions[2,i] = newPositions[2]
        
    return positions


#Finally we apply the Runge-Kutta method
#Fist define the initial position
x0 = 0
y0 = 1
z0 = 0

#Define the time-step of the numerical integration and the max. time of integration
dt = 0.01
tMax = 100

#The parameters
s = 10
b = 8/3
r = 28

#simulate the system!
positions = rungeKutta(x0,y0,z0,dt,tMax,s,r,b)

#just for fun, let's plot the trajectory
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(positions[0,:], positions[1,:], positions[2,:], s=0.1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
