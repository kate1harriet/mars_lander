#using the Verlet method to simulate a mass on a spring
import numpy as np
import matplotlib.pyplot as plt

dt =0.001

time = np.arange(100, step = 0.001)
disp = [0.000,.001]
vel = [1]
#confused with setting initial values for this method. 
#two initial values are required for displacement, is this the issue?


def velocity(x1, x2, dt):
    return (x2-x1)/dt


def displacement(x1, x2, dt, k):
    return 2*x2 - x1 + k*x2*dt**2



def calc(dt, k):
    for n in range(len(time)-2):
        newDisp = displacement(disp[n],disp[n+1],dt,k)
        newVel = velocity(disp[n+1], newDisp, dt)
        disp.append(newDisp)
        vel.append(newVel)
    vel.append(0)    
    return disp, vel

disp, vel = calc(0.001, 1)
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
