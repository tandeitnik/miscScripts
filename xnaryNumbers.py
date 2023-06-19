# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:21:24 2023

@author: tandeitnik

This piece of code creates x-nary (like binary) numbers with N entries
"""
import numpy as np

cap = 3
N = 4 
x = np.zeros(N)

done = False

while not done:
    
    print(x)
    
    x[-1] += 1
    
    for j in range(len(x)):
        
        if x[-1 - j] >= cap and j != len(x)-1:
            
            x[-1 - j -1] += cap-x[-1 - j]+1
            x[-1 - j] = 0
        
        elif  x[-1 - j] >= cap and j == len(x)-1:
            
            done = True
            break
