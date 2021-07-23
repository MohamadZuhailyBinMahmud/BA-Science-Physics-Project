# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:22:09 2021

@author: acer
"""

import numpy as np
import matplotlib.pyplot as plt

a = 0.1
b = 1.5
tol = 10**(-4)


c = 0
re = 0
deviation = 10
i = 0


def f(E):
    M=1
    e = 0.5
    return M - (0.5)*np.sin(E)

print('f(a) =',f(a))
print('f(b) =',f(b))


if f(a)*f(b)>0:
    print('No root')
elif f(a)==0:
    print('Root is',a)
elif f(b)==0:
    print('Root is',b)
elif f(a)*f(b)<0:
    print('i','a','f(a)','b','f(b)','deviation','c','f(c)',sep='\t')
    while deviation>=tol:
        deviation = abs(b-a)
        c = a+(0.5*(b-a))
        
        print(i,round(a,4),round(f(a),4),round(b,4),round(f(b),4),round(deviation,4),round(c,4),round(f(c),4),sep='\t')
        if f(c)>0:
            if f(b)>0:
                b=c
            elif f(a)>0:
                a=c
        elif f(c)<0:
            if f(b)<0:
                b=c
            elif f(a)<0:
                a=c
        i+=1
        print(c)
        
x = np.linspace(0.1,1.5,100)
y = f(x)
plt.plot(x,y)
    
    