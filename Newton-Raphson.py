# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:51:30 2021

@author: acer
"""

import numpy as np

a = 2
deviation = 10  
tol = 10e-6

x = 0
i = 0
e1 = 0
e2 = 0
e1_list =[]
e2_list =[]
const_list=[]
i_list=[]
a_list=[]
x_list=[]
deviation_list=[]


def f(x):
    return (x**3)-(2*x)-5

def g(x):
    return (3*(x**2)-2)


while deviation > tol:
    i_list.append(i)
    a_list.append(a)
    x = a-(f(a)/g(a))
    x_list.append(x)
    deviation = abs(x-a)
    deviation_list.append(deviation)
    i+=1
    b = a
    a = x


for i in i_list:
    e1 = abs(x - a_list[i])
    e2 = abs(x - x_list[i])
    const = e2/(e1**2)
    e1_list.append(e1)
    e2_list.append(e2)
    const_list.append(const)
    

print('i','x_i','x_(i+1)','deviation','E_1','E_2','const',sep='\t')

for i in i_list:
    print(i_list[i],round(a_list[i],6),round(x_list[i],6)
          ,round(deviation_list[i],6),round(e1_list[i],6),round(e2_list[i],6)
          ,round(const_list[i],6),sep='\t')
    
print('α =', round(x,6))

