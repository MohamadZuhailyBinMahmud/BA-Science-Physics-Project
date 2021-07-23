# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:30:34 2021

@author: acer
"""

import numpy as np
import matplotlib.pyplot as plt


a = 1
b = 2
n = 6

def f(x):
    return  x*np.log(x)

def midpoint(a,b,n):

    tot = 0
    h = (b-a)/n
    for i in range(n):
        tot = tot + f(a+(i-1/2)*h)
    fin = h*tot
    return fin
        

print(midpoint(a,b,n),sep='\n')