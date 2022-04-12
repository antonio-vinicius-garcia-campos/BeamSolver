# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 12:04:21 2021

@author: viniv
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,1500,5000)

q_x = -10*((x**0)-((x-500)**0)*(x>=500)) - (3000*(x-750)**(-1))*(x>=750)
V_x = -10*((x**1)-((x-500)**1)*(x>=500)) - (3000*(x-750)**(0))*(x>=750) + 8000
M_x = -5*((x**2)-((x-500)**2)*(x>=500)) - (3000*(x-750)**(1))*(x>=750) + 8000*x - 3500

plt.close('all')
plt.subplot(211)
plt.plot(x,V_x,'g')
plt.grid('on')
plt.subplot(212)
plt.plot(x,M_x,'r')
plt.grid('on')
