# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 16:27:22 2023

@author: tandeitnik
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

file = open(r'fileName.csv')
skipRows = 2 #after header

csvreader = csv.reader(file)

header = []
header = next(csvreader)

for i in range(skipRows):
    
    next(csvreader)

rows = []

for row in csvreader:
    
    rows.append(row)
    
file.close()

data = np.array(rows).astype(float)
