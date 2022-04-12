# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 20:51:42 2020

@author: Antonio Viniicius Garcia Campos

CÓDIGOS PARA SIMULAÇÃO NUMÉRICA DE SISTEMAS DINÂMICOS

===============================================================================
SISTEMA COM 1 GDL - ANALITICO

- input:
    
    
- output:
    
===============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0,6,5000)

m = 10   # kg
k = 1000 # N/m
c = 10  # N.s/m
F0 = 400 # N
X0 = 1   # m
dX0 = 1  # m/s


wf = 20

wn = np.sqrt(k/m)

c_cr = 2*m*wn

zt = c/c_cr

wd = np.sqrt(1 - zt**2)*wn

# movimento livre - não amortecido
xt1 = X0*np.cos(wn*t) + (dX0/wn)*np.sin(wn*t)


# movimento livre - amortecido
xt2 = np.exp(-zt*wn*t)*(X0*np.cos(wd*t) + ((dX0 + zt*wn*X0)/wd)*np.sin(wd*t))


# movimento forçado - não amortecido
xt3 = (X0 - F0/(k-m*wf**2))*np.cos(wn*t) + (dX0/wn)*np.sin(wn*t) + (F0/(k-m*wf**2))*np.cos(wf*t)

rg_w = np.linspace(0,1.5*wf,500)/wn

x_st = abs(1/(1-rg_w**2))

p_serv = abs(1/(1-(wf/wn)**2))


# graficos

plt.close('all')
plt.figure(1)
plt.plot(t,xt1)
plt.xlabel('tempo [s]')
plt.ylabel('deslocamento [m]')
plt.title('movimento livre - não amortecido')
plt.grid('on')

plt.figure(2)
plt.plot(t,xt2)
plt.xlabel('tempo [s]')
plt.ylabel('deslocamento [m]')
plt.title('movimento livre - amortecido')
plt.grid('on')

# plt.figure(3)
# plt.plot(t,xt3)
# plt.xlabel('tempo [s]')
# plt.ylabel('deslocamento [m]')
# plt.title('movimento forçado - não amortecido')
# plt.grid('on')


# plt.figure(4)
# plt.semilogy(rg_w, x_st,wf/wn,p_serv,'-or')
# plt.legend(['espectro','ponto de operação'])
# # plt.plot(rg_w, x_st,wf/wn,p_serv,'-or')
# plt.xlabel('espectro de frequencia')
# plt.ylabel('deslocamento [m]')
# plt.title('espectro de frequencia')
# plt.grid('on')

fig, (ax1,ax2) = plt.subplots(2,gridspec_kw={'hspace':0.3})
fig.suptitle('Vibração Forçada')
ax1.plot(t, xt3)
ax1.set_xlabel('tempo [s]')
ax1.set_ylabel('deslocamento [m]')
ax2.semilogy(rg_w, x_st,wf/wn,p_serv,'-or')
ax2.legend(['espectro','ponto de operação'])
ax2.set_xlabel('espectro de frequencia')
ax2.set_ylabel('')
