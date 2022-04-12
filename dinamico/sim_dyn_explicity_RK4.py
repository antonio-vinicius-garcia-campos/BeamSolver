# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:06:47 2020

@author: Antonio Viniicius Garcia Campos

CÓDIGOS PARA SIMULAÇÃO NUMÉRICA DE SISTEMAS DINÂMICOS

===============================================================================
SOLUÇÃO NUMÉRICA EXPLICITA - SOLVER RUNGE-KUTTA RK4

- input:
    
    
- output:
    
===============================================================================
"""
#%% PACOTES 
import sys
import numpy as np
from scipy import linalg as la
import matplotlib.pyplot as plt

#%% PARAMETROS DO SISTEMA - CARACTERISTICAS DO MODELOS
sgdl = 3  # qtd de GDL do modelo


# A = 6.35*50.80
I = 1.6817E6 #(1/12)*50.80*6.35**3
L = 6000
E = 200000
# rho = 7.86E-6
# m = rho*A*L


# Matriz de massa - lumped
# M = np.ones([sgdl,sgdl])
# m=10
# M = np.array([[m,0,0],[0,3*m,0],[0,0,m]])
m=178.98
M = np.array([[m/4,0,0],[0,m/4,0],[0,0,m/4]])

# M = (m/2)*np.array([[1,0],[0,1]])

# Matriz de rigidez
# K = np.ones([sgdl,sgdl])
# k=1000
# K = np.array([[3*k,-2*k,0],[-2*k,4*k,-2*k],[0,-2*k,3*k]])
K = ((E*I)/(L**3))*np.array([[630.85,-603.42,246.85],[-603.42,877.71,-603.42],[246.85,-603.42,630.85]])

# K = ((E*I)/(7*L**3))*np.array([[768,-240],[-240,96]])

# Matriz de amortecimento
# c=0.08
C = np.zeros([sgdl,sgdl])
# C = np.array([[2*c,-c,0],[-c,2*c,-c],[0,-c,2*c]])

# Amplitude de forca
F0 = 1

#%% PARAMETROS DA SIMULACAO
T_max = 600 # tempo max em segundos
dT = 0.2  # incremento de tempo

t = np.arange(0,T_max+dT,dT)
ite_max = t.shape[0]

# forcas dinamicas
F = np.zeros([sgdl,ite_max])
# f = np.zeros([ite_max,1])
# f[0] = 1

# n=50
# (n*np.exp(-n*x))/(1+np.exp(-n*x)**2)
F[1,:] = F0*((t-T_max/2)**0)*(t>T_max/2)

# F[1,0] = F0*np.cos(1*t)
# F[0,0] = 1

# matrizes auxiliares
zeros_vect = np.zeros([sgdl,1])
zeros_matr = np.zeros([sgdl,sgdl])
inden_matr = np.eye(sgdl)
inv_M = np.linalg.inv(M)


#%% ANALISE MODAL
w,v_mode = la.eig(K,M)
w_freq_rad = np.sqrt(abs(w))
f_freq_hz = w_freq_rad/(2*np.pi)
T_per = 1/f_freq_hz
# v_mode = np.concatenate((np.zeros([1,sgdl]),v),axis=0)


print('freq. natural [rad/s]: ',w_freq_rad)
print('freq. natural [Hz]: ',f_freq_hz)
print('periodo mov. livre [s]: ',T_per)

dW = 0.001

W_max = (np.pi/2)*max(w_freq_rad)

w_range =  np.arange(0,W_max+dW,dW)

w_range_max = w_range.shape[0]

frf_out = np.zeros([sgdl,w_range_max])
Fw = np.ones([sgdl,1])

U_modal = np.zeros([sgdl,w_range_max])
for ww in range(w_range_max):
    Wn = w_range[ww]
    Dw = K-(Wn**2)*M
    U_modal[:,ww] = np.reshape(np.linalg.solve(Dw,Fw),(1,sgdl))



#%% INTEGRACAO RK4

A1 = np.concatenate((zeros_matr,np.dot(-inv_M,K)),axis=0)
A2 = np.concatenate((inden_matr,np.dot(-inv_M,C)),axis=0)
A = np.concatenate((A1,A2),axis=1)

U = np.zeros([2*sgdl,1])

Disp = np.zeros([sgdl,ite_max])
Velc = np.zeros([sgdl,ite_max])
Acel = np.zeros([sgdl,ite_max])


for i in range(ite_max):  
    b = np.concatenate((zeros_vect,np.dot(inv_M,np.reshape(F[:,i],(sgdl,1)))),axis=0)  
    
    l1 = np.dot(A,U)+b
    ux1 = U+(dT*0.5)*l1
    l2 =  np.dot(A,ux1)+b
    ux2 = U+(dT*0.5)*l2
    l3 =  np.dot(A,ux2)+b
    ux3 = U+(dT*l3)
    l4 = np.dot(A,ux3)+b
    U = U + (dT/6)*(l1 + 2*l2 + 2*l3 + l4)
    
    Disp[:,i] = U[:sgdl,0]
    Velc[:,i] = U[sgdl:2*sgdl,0]



#%% GRAFICOS
# # mode shape
plt.close('all')
plt.figure()
plt.subplot(311)
plt.plot(v_mode[:,0],label='w_1= '+str(f_freq_hz[0])+' Hz')
plt.legend(loc='upper right')
# plt.ylabel('1 Mode Shape')
plt.grid('true')

plt.subplot(312)
plt.plot(v_mode[:,1],label='w_2= '+str(f_freq_hz[1])+' Hz')
plt.legend(loc='upper right')
# plt.ylabel('2 Mode Shape')
plt.grid('true')

plt.subplot(313)
plt.plot(v_mode[:,2],label='w_3= '+str(f_freq_hz[2])+' Hz')
plt.legend(loc='upper right')
# plt.ylabel('3 Mode Shape')
plt.grid('true')



# # movimento no tempo - RK4
plt.figure()
# plt.plot(t,Disp[0,:],'-r',t,Disp[1,:],'-.b')
plt.plot(t,1000*Disp[0,:],'-r',t,1000*Disp[1,:],'-.g',t,1000*Disp[2,:],'--b')
plt.legend(['U1','U2','U3'])
plt.xlabel('tempo [s]')
plt.ylabel('deslocamento [m]')
plt.grid('on')

# # plt.figure()
# # plt.plot(t,Velc[0,:],'-r',t,Velc[1,:],'-.g',t,Velc[2,:],'--b')
# # plt.legend(['dU1','dU2','dU3'])
# # plt.xlabel('tempo [s]')
# # plt.ylabel('velocidade [m/s]')
# # plt.title('movimento livre - não amortecido')
# # plt.grid('on')

plt.figure()
plt.plot(t,F[1,:])
# plt.legend(['dU1','dU2','dU3'])
plt.xlabel('tempo [s]')
plt.ylabel('Forca Dinamica [N]')
plt.grid('on')


# # FRF Modelo
plt.figure()
plt.semilogy(w_range/(2*np.pi),abs(U_modal[1,:]))
# plt.legend(['dU1','dU2','dU3'])
plt.xlabel('espectro de frequencia [Hz]')
plt.ylabel('FRF')
plt.grid('on')


#%% FFT NUMPY


