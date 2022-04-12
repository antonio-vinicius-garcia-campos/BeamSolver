# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:12:33 2021

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

U0 = 0
dU0 = 0
ddU0 = np.array([0,0])

T_max = 12*0.28  # tempo max em segundos
dT  = T_max/12   # incremento de tempo


# A = 6.35*50.80
# I = 1.6817E6 #(1/12)*50.80*6.35**3
# L = 6000
# E = 200000
# rho = 7.86E-6
# m = rho*A*L


# Matriz de rigidez
# k=2
K = np.array([[6,-2],[-2,4]])
# K = np.array([[3*k,-2*k,0],[-2*k,4*k,-2*k],[0,-2*k,3*k]])
  # qtd de GDL do modelo
# K = ((E*I)/(L**3))*np.array([[630.85,-603.42,246.85],[-603.42,877.71,-603.42],[246.85,-603.42,630.85]])

# K = ((E*I)/(7*L**3))*np.array([[768,-240],[-240,96]])

sgdl = len(K)

# Matriz de massa - lumped
# m=10
# M = np.array([[m,0,0],[0,3*m,0],[0,0,m]])
M = np.array([[2,0],[0,1]])

# M = (m/2)*np.array([[1,0],[0,1]])


# Matriz de amortecimento
# c=0.08
C = np.zeros([sgdl,sgdl])
# C = np.array([[2*c,-c,0],[-c,2*c,-c],[0,-c,2*c]])

# Amplitude de forca
F0 = np.array([0,10])

#%% PARAMETROS DA SIMULACAO
t = np.arange(0,T_max,dT)
ite_max = t.shape[0]

# forcas dinamicas
F = np.zeros([sgdl,ite_max])
F[0,:] = F0[0]
F[1,:] = F0[1]

# n=50
# (n*np.exp(-n*x))/(1+np.exp(-n*x)**2)
# F[1,:] = F0*((t-T_max/2)**0)*(t>T_max/2)

# F[1,0] = F0*np.cos(1*t)
# F[0,0] = 1

# matrizes auxiliares
U = np.zeros((sgdl,ite_max))
dU = np.zeros((sgdl,ite_max))
ddU = np.zeros((sgdl,ite_max))

U[:,0] = U0
dU[:,0] = dU0
ddU[:,0] = ddU0

# Disp = np.zeros([sgdl,ite_max])
# Velc = np.zeros([sgdl,ite_max])
# Acel = np.zeros([sgdl,ite_max])
# Fb = np.zeros([sgdl,ite_max])


#%% INTEGRACAO METODO DAS DISFERENCAS CENTRAIS
a0 = 1/(dT**2)
a1 = 1/(2*dT)
a2 = 2*a0
a3 = 1/a2

U_dt = U[:,0] - dT*dU[:,0] + a3*ddU[:,0]

Mb = a0*M + a1*C
invMb = np.linalg.inv(Mb)

KM = -(K-a2*M)
MC = -(a0*M-a1*C)
for i in range(0,ite_max-1):
    Fb = np.reshape(F[:,i],(sgdl,1))  + np.dot(KM,np.reshape(U[:,i],(sgdl,1))) + np.dot(MC,np.reshape(U_dt,(sgdl,1)))
    S = np.dot(invMb,Fb)
    U[:,i+1] = S[:,0]
        
    ddU[:,i] = a0*(U_dt - 2*U[:,i] + U[:,i+1])
    dU[:,i] = a1*(U[:,i+1] - U_dt)

    U_dt = U[:,i]

#%%
plt.close('all')
plt.figure()
plt.plot(t,U[0,:],'-r',t,U[1,:],'-.g')
plt.legend(['U1','U2'])
plt.xlabel('tempo [s]')
plt.ylabel('deslocamento [m]')
plt.grid('on')

plt.figure()
plt.plot(t,dU[0,:],'-r',t,dU[1,:],'-.g')
plt.legend(['dU1','dU2','dU3'])
plt.xlabel('tempo [s]')
plt.ylabel('velocidade [m/s]')
plt.title('movimento livre - não amortecido')
plt.grid('on')

plt.figure()
plt.plot(t,ddU[0,:],'-r',t,ddU[1,:],'-.g')
plt.legend(['ddU1','ddU2','ddU3'])
plt.xlabel('tempo [s]')
plt.ylabel('aceleracao [m/s2]')
plt.title('movimento livre - não amortecido')
plt.grid('on')

plt.figure()
plt.plot(t,F[1,:])
plt.xlabel('tempo [s]')
plt.ylabel('Forca Dinamica [N]')
plt.grid('on')