import numpy as np
import matplotlib.pyplot as plt

n = 99
m = 1000
T = 2.0
t = np.linspace(-T/2,T/2,m)


# ft = [A*np.ones(1,length(t)/2),-A*ones(1,length(t)/2)];


SF = 0.0
for ii in range(1,n+2,2):
    SF += (4/np.pi)*(1/ii)*(np.sin(ii*(2*np.pi*t)/T))
    

plt.close('all')
plt.figure()
plt.plot(t,SF,'--r')
plt.show()
plt.grid(True)