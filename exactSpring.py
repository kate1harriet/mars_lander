#Need to delete once can confirm that the other code is working as expected

"""
import numpy as np
import matplotlib.pyplot as plt
import math

dt = 0.001
km = 1
x0 = 0
v0 = 1
k=1
m=1

time = np.arange(10, step = dt)

def maxDisp(x0,v0,k,m):
    #takes input velocity and displacement of spring, returns maximum displacement
    energy = 0.5*k*x0**2 + 0.5*m*v0**2
    maxVal = math.sqrt(2*energy/k)
    return maxVal


amplitude = maxDisp(x0,v0,k,m)
omega = math.sqrt(k/m)


plt.plot(amplitude*math.cos(omega*time), time)
plt.xlabel('$t$')
plt.ylabel('$x/v$')
plt.legend()
plt.figure()
plt.show()
"""
