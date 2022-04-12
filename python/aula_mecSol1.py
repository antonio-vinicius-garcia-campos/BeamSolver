# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:48:28 2021

@author: viniv
"""

import numpy as np
import matplotlib.pyplot as plt



p0 = 10
L = 1500

x = np.linspace(0,L,1000)


q_x = (-p0*(x)**0)*(x>0)

V_x = (-p0*(x)**1)*(x>0) + p0*L/2
M_x = ((-p0/2)*(x)**2)*(x>0) + p0*L*x/2


plt.close('all')

plt.subplot(311)
plt.plot(x,q_x,'r')
plt.grid('on')
plt.subplot(312)
plt.plot(x,V_x,'b')
plt.grid('on')
plt.subplot(313)
plt.plot(x,M_x,'g')
plt.grid('on')
