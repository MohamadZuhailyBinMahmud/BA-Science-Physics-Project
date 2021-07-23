# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:37:53 2021

@author: acer
"""

import numpy as np

x1 = float(input('Insert first guess'))
x2 = float(input('Insert second guess'))

deviation = abs(x2-x1)  
interval_of_error = 1e-2
i = 0

def f(x):
    return 3*(x**3)-x-1

print(i, round(x1,4), round(x2,4), round(deviation,4))

while deviation > interval_of_error:
    i+=1
    x = x2 - (f(x2)*(x2-x1))/(f(x2)-f(x1))
    x1=x2
    x2=x
    deviation = abs(x2-x1)
    print(i, round(x1,4), round(x2,4), round(deviation,4),sep='\t')
    
print(x2)