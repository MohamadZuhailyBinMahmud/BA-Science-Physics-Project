# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 21:17:45 2021

@author: acer
"""

import math as mt

x0 = 1
x1 = 0
i = 1
delta = 10
prevdelta = 11
nx = 0
k=0
j=0


def f(x):
    return mt.exp(-x**2)
    
    
def g(x):
    a = -2*mt.exp(-x**2)*x
    b = -2*(-2*mt.exp(-x**2)*(x**2)+mt.exp(-x**2))
    return round(x-(a/b),6)

k = f(x0)


while delta > 0.1:
    x1 = g(x0)
    delta = round(abs(x1-x0),6)
        
    
    print(i , x0 , x1, delta,sep='\t')
    
    
    if delta > prevdelta:
        print('diverging')
        break
    
    i += 1
    x0 = x1
    prevdelta = delta
    
j = f(x1)
    

if k<j:
    print(round(k,2),'<',round(j,2))
    print('maximum point')
elif k>j:
    print(round(k,2),'>',round(j,2))
    print('minimum point')
    
    
    
    