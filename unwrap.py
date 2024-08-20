# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:00:07 2024

@author: Daniel Tandeitnik

this script make numbers fall into the modular range of [-y,y]. Ive made it to
unwrapped numbers in radians into the range [-pi,pi].
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10*np.pi,10*np.pi,10000)
y = np.pi

unwrapped = -1*np.sign(x)*y*((np.abs(x) // y) % 2) + np.fmod(x,y)
plt.plot(x/np.pi,unwrapped/np.pi)
