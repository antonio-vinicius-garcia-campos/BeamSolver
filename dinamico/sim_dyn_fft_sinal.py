# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 17:56:37 2021

@author: viniv
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

n = 1000 #data.shape[0] #numero de pontos

f = 30 #Hz
w = 2*np.pi*f

t = np.linspace(0,3,n)

sinal = np.sin(w*t)+np.sin(4*w*t)

sinal_fft = np.fft.fft(sinal)
freq = np.fft.fftfreq(len(sinal),t[1]-t[0])

freq_side = freq>0
freq = freq[freq_side]
sinal_fft = sinal_fft[freq_side]


plt.close('all')
plt.figure()
plt.subplot(211)
plt.plot(t,sinal)
plt.grid('on')
plt.subplot(212)
plt.semilogy(freq,abs(sinal_fft))

