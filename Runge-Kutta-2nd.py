# -*- coding: utf-8 -*-
"""
Created on Thu May 27 21:47:30 2021

@author: acer
"""

import numpy as np
from matplotlib.pyplot import plot as plt

def f(x,y):
    return -y*np.log(y)

y0 = 0.5
x0 = 0
n = 4
x_max = 1
h = x_max/n
x_range = []
y_range = []

for i in range(n):
    x_range.append(x0)
    y_range.append(y0)
    K1 = f(x0,y0)
    K2 = f(x0+h,y0+h*K1)
    y = y0 + (h/2)*(K1+K2)
    y0 = y
    x0 = x0 + h
    
print(x_range,y_range,sep='\n')
plt(x_range,y_range)