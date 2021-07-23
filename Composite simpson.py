# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:51:49 2021

@author: acer
"""

import numpy as np
import matplotlib.pyplot as plt


a = 1
b = 2
n = 6


def f(x):
    return  x*np.log(x)

def simpson(a,b,n):
    i=1
    tot = 0
    h = (b-a)/2
    x = np.linspace(a,b,n+1)
    while i<=(n/2):
        tot = tot + h/3*(f(x[(2*i-2)])+4*f(x[(2*i-1)])+f(x[(2*i)]))
        i+=1 
    return tot
        

print(simpson(a,b,n),sep='\n')

