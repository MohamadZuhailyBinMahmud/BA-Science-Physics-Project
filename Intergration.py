# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:41:08 2021

@author: acer
"""

import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 2

def f(x):
    return x*np.log(x)

def midpt(a,b):
    val = (b-a)*f((a+b)/2)
    return val

def trapez(a,b):
    val = (b-a)/2*(f(a)+f(b))
    return val

def simpson(a,b):
    val = (b-a)/6*(f(a)+(4*f((a+b)/2))+f(b))
    return val

exact = 0.63662943610
print(midpt(a,b),trapez(a,b),simpson(a,b),exact,sep='\n')

x = np.linspace(1,2)
plt.plot(x,f(x),label="$f(x)=x ln x$")
plt.fill_between(x,0,f(x),alpha=0.1)
plt.legend()
plt.show()
