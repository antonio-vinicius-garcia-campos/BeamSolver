# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:22:06 2021

@author: viniv
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


L = 5

x = np.linspace(0,L,1000)


# q_x =  ((-50/2)*((x**1) - ((x-2)**1)*(x>=2))) + (50*(x-2)**0)*(x>=2) + (40*(x-2)**-1)*(x>=2)
V_x = ((-25/2)*((x**2) - ((x-2)**2)*(x>=2))) + (50*(x-2)**1)*(x>=2) + (40*(x-2)**0)*(x>=2)
M_x = ((-25/6)*((x**3) - ((x-2)**3)*(x>=2))) + ((50/2)*(x-2)**2)*(x>=2) + (40*(x-2)**1)*(x>=2)


plt.close('all')

# plt.subplot(211)
# plt.plot(x,q_x,'r')
# plt.grid('on')
plt.subplot(211)
plt.plot(x,V_x,'b')
plt.grid('on')
plt.subplot(212)
plt.plot(x,M_x,'g')
plt.grid('on')