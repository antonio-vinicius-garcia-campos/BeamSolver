# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:18:45 2020

@author: viniv
"""
# MÉTODO DE EULER SOLUÇÃO NUMÉRICA PARA EDO/PVI DE UM PÊNDULO
import numpy as ny
import matplotlib.pyplot as plt

# Parametros do modelo
g=9.81               # gravidade
le=10              # comprimento do fio
w=ny.sqrt(g/le)   # frequencia natural do pendulo
u0 = 0.5          # C.I. deslocamento
du0 = 0.0          # C.I. velocidade

# método Euler
# parametros auxiliares
t=0                  # tempo  inicial
time_max=12
h=0.1               # passo do método
ite_max=int(time_max/h)
ut=ny.zeros([2,ite_max])
xt=ny.zeros([1,ite_max])
yt=ny.zeros([1,ite_max])
the_t=ny.zeros([1,ite_max])
er=ny.zeros([1,ite_max])
u = ny.array([[u0],[du0]])
A=ny.array([[0,1],[-w**2,0]])
for i in range(0,ite_max):
    t=t+h
    # solução numérica
    u=u+h*(ny.dot(A,u))
    ut[:,i]=u.T
    xt[:,i]=le*ny.sin(u[0])  # coord. cartesianas
    yt[:,i]=-le*ny.cos(u[0]) # coord. cartesianas

    # solução analítica
    the_t[:,i] =u0*ny.cos(w*t)+(du0/w)*ny.sin(w*t)

    # erro relativo
    er[:,i]=abs((the_t[:,i]-ut[0,i])/ut[0,i])*100 #erro em %


# analise do erro
erro_max=ny.max(er)
print('Erro relativo máximo [%]')
print(erro_max)


# pos processamento
time = ny.arange(0,time_max,h)
plt.close('all')
plt.figure()
plt.clf
plt.plot(time,ut[0,:],'r',time,the_t.T,'b')
plt.title('Solução')
plt.xlabel('tempo')
plt.ylabel('Angulo')
plt.grid(True)
plt.show

plt.figure()
plt.clf
plt.plot(time,xt[0,:],'r',time,yt[0,:],'b')
plt.title('Solução')
plt.xlabel('tempo')
plt.ylabel('Angulo')
plt.grid(True)
plt.show

plt.figure()
plt.clf
plt.plot(xt,yt,'ob')
plt.axis('equal')
plt.title('Movimento do pendulo')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.grid(True)
plt.show


