# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:37:21 2021

@author: acer
"""

import numpy as np
from scipy import linalg as lin


A = np.array([[14, 14, -9, 3,-5], [14, 52, -15, 2,-32], [-9, -15, 36, -5,16], [3, 2, -5, 47,49],[-5,-32,16,49,79]])
b = b = np.array([-15,-100,106,329,463])
L = lin.cholesky(A, lower = True)
L1 = lin.cho_factor(A,lower=True)
x = lin.cho_solve(L1,b)



print(x)
