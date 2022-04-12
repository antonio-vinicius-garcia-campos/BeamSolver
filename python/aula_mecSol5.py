# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:22:06 2021

@author: viniv
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


b = 50              # mm
h = 100             # mm
L = 1000            # mm
I = (1/12)*b*h**3   # mm^4
E = 200000          # MPa
F = -1000           # N
npts = 2000

x = np.linspace(0,L,npts)
y = np.linspace(-h/2,h/2,npts)


V = (-F*(x-L/2)**0)*(x>=L/2) + F/2
M = (-F*(x-L/2)**1)*(x>=L/2) + (F/2)*x

Theta = (1/(E*I))*((-F/2*(x-L/2)**2)*(x>=L/2) + (F/4)*x**2 - (F*L**2)/16)
v_y = (1/(E*I))*((-F/6*(x-L/2)**3)*(x>=L/2) + (F/12)*x**3 - (F*x*L**2)/16)


plt.close('all')
plt.figure()
plt.subplot(411)
plt.plot(x,V,'r')
plt.subplot(412)
plt.plot(x,M,'g')
plt.subplot(413)
plt.plot(x,Theta,'b')
plt.subplot(414)
plt.plot(x,v_y,'m')

#%% TENSAO
X,Y = np.meshgrid(x,y)
S = M*Y/I

plt.figure()
plt.contourf(X,Y,S,levels=30,cmap=cm.jet)
cbar = plt.colorbar()
cbar.set_label('Tensão Normal SXX')
