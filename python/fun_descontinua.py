# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:20:23 2021

@author: viniv
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,6,0.0001)
y1 = ((x-3)**0)*(x>3)
y2 = ((x)**6)*(x>0)



# n=50
# y1b = 1/(1+np.exp(-n*x))
# y3 = ((n**2)*np.exp(-n*x)*(1-np.exp(-n*x)))/(1+np.exp(-n*x)**3)
# y4 = (n*np.exp(-n*x))/(1+np.exp(-n*x)**2)


# plt.close('all')

# # plt.figure()
# # plt.plot(x,y1)
# # plt.show()

# plt.figure()
# plt.plot(x,y1b)
# plt.show()

# plt.figure()
# plt.plot(x,y3)
# plt.show()

plt.figure()
plt.plot(x,y1)
plt.show()