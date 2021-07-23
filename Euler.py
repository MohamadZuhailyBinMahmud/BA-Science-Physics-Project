# -*- coding: utf-8 -*-
"""
Created on Thu May 27 21:20:28 2021

@author: acer
"""

import numpy as np
from matplotlib.pyplot import plot as plt

def f(x,y):
    return -y*np.log(y)

y0 = 0.5
x0 = 0
n = np.array([2,4,8])
x_max = 1
h = x_max/n
nlen = len(n)

"""
def Euler(y0,x0,n,h):
    x_range = []
    y_range = []

    for i in range(n):
        x_range.append(x0)
        y_range.append(y0)
        y = y0 + h*f(x0,y0)
        y0 = y
        x0 = x0 + h
    return x_range,y_range

     
xarray,yarray = Euler(y0,x0,n,h)
    
print(xarray,yarray,sep='\n')
plt(xarray,yarray)
    """
    
print


    
    