# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 12:04:21 2021

@author: viniv
"""

import numpy as np
import matplotlib.pyplot as plt


p0 = 3
L = 1

x = np.linspace(0,L,1000)

q_x = (-p0*(x-0.3)**-1)*(x>0.3)
V_x = (-p0*(x-0.3)**0)*(x>0.3) + 13
M_x = (-p0*(x-0.3)**1)*(x>0.3) + 13*x -10.9

plt.close('all')
plt.subplot(211)
plt.plot(x,V_x,'g')
plt.grid('on')
plt.subplot(212)
plt.plot(x,M_x,'r')
plt.grid('on')
