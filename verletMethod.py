#using the Verlet method to simulate a mass on a spring
import numpy as np
import matplotlib.pyplot as plt


"""
dt =0.001
tmax = 100
km = 1

time = np.arange(tmax, step = dt)
disp = [0.000,.001]
vel = [1]
#confused with setting initial values for this method. 
#two initial values are required for displacement, is this the issue?


def velocity(x1, x2, dt):
    return (x2-x1)/dt


def displacement(x1, x2, dt, km):
    return 2*x2 - x1 + km*x2*dt**2

#using the paramater km to be the specific spring constant
#as neither value is ever required in isolation

def calc(dt, km):
    for n in range(len(time)-2):
        newDisp = displacement(disp[n],disp[n+1],dt,km)
        newVel = velocity(disp[n+1], newDisp, dt)
        disp.append(newDisp)
        vel.append(newVel)
    vel.append(0)    
    return disp, vel

disp, vel = calc(dt, km)
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

"""

def verlet(km,x,v,t_max,dt):
    
    #create list of times for plotting
    t_array = np.arange(0, t_max, dt)

    #initialise lists, note that we need two x values for verlet, so 
    #I found the second value using euler
    x_list = [x, x + dt * v]
    v_list = [v]
    
    
    #verlet intergtaion
    #note how the range is shifted by 1 to the right, since we already have our second value
    for t in range(1, len(t_array) - 1):
        
        x = 2*x_list[t] - x_list[t-1] - ((dt ** 2) * km*x_list[t])
        v = 1/(2*dt) * (x - x_list[t-1]) 
        
        x_list.append(x)
        v_list.append(v)
    
    #we also need the last value for v, which we find using the less accurate v(t+dt) formula
    v_list.append(1/dt * (x - x_list[t]))
    
    """
    #change to arrays
    x_array = np.array(x_list)
    v_array = np.array(v_list)
    """

    #plot
    plt.figure(1)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(t_array, x_list, label='x (m)')
    plt.plot(t_array, v_list, label='v (m/s)')
    plt.legend()
    plt.show()


verlet(1, 0, 1, 1000, 1.25) #km, x, v, t_max, dt
#1.95
#struggling with part 1 q3

# Struggling to understand the stability element at this level.
# dt is so large that most have a very large time step
# so results are far from sinusoidal
# but equally max amplitudes do not dramatically increase or decrease
# so is can stability be cyclical in amplitude range, or not??


