# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:03:01 2021

@author: acer
"""

import numpy as np
import math as mp

def f(x):
    return

def g(x):
    return

def h(x):
    return

def bisection(a,b,interval_of_error):
    c = 0
    deviation = abs(b-a)
    i = 0
    
    if f(a)*f(b)>0:
        print('Invalid initial guess')
    elif f(a)==0:
        print('Root is',a)
    elif f(b)==0:
        print('Root is',b)
    elif f(a)*f(b)<0:
        while deviation>interval_of_error:
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
    
def newtraph(a,interval_of_error):
    x = 0
    deviation = 10  
    i = 0
    
    while deviation > interval_of_error:
        x = a-(f(a)/g(a))
        deviation = abs(x-a)
        print(i,round(a,4),round(x,4),round(deviation,4),sep='\t')
        i+=1
        a = x
    
    print(round(x,6))
    
def secant(x1,x2,interval_of_error): 
    deviation = abs(x2-x1)  
    i = 0
    
    print(i, round(x1,4), round(x2,4), round(deviation,4))
    
    while deviation > interval_of_error:
        i+=1
        x = x2 - (f(x2)*(x2-x1))/(f(x2)-f(x1))
        x1=x2
        x2=x
        deviation = abs(x2-x1)
        print(i, round(x1,4), round(x2,4), round(deviation,4),sep='\t')
        
    print(x2)
    
