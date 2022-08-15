#marslander excercise 1 - euler method demonstration

import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
km = 1

time = np.arange(10, step = dt)
disp = [0]
vel = [1]



def velocity(v, x, dt, k):
    return v - k*dt*x
#paramater k actually refers to k/m ratio of the mass spring system

def displacement(v, x, dt):
    return x + v*dt


def calc(dt, k):
    for n in range(len(time)-1):
        newVel = velocity(vel[n], disp[n], dt, k)
        newDisp = displacement(vel[n], disp[n], dt)
        #performing v+d calculations with most recent values
        #adding these to the end of existing lists
        vel.append(newVel)
        disp.append(newDisp)
    return disp, vel


disp, vel = calc(dt, 1)
print(disp[:10], vel[:10])

plt.plot(time, disp, label = 'displacement')
plt.plot(time, vel, label = 'velocity')
plt.xlabel('$t$')
plt.ylabel('$x/v$')
plt.legend()
plt.figure()
plt.show()

#attempting to show displacement with time of a mass spring system
#note the timestep must be suitably small to avoid numerical errors





