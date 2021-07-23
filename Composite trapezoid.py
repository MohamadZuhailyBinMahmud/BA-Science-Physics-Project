# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:42:00 2021

@author: acer
"""

import numpy as np
import matplotlib.pyplot as plt


a = 1
b = 2
n = 6


def f(x):
    return  x*np.log(x)

def trapezoid(a,b,n):
    tot = 0
    h = (b-a)/n
    x = np.linspace(a,b,n+1)
    for i in range(1,n):
        tot = tot + f(x[i])
    fin = h/2*(f(x[0])+2*tot+f(x[n]))
    return fin
        

print(trapezoid(a,b,n),sep='\n')