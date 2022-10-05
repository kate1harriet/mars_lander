import numpy as np
import matplotlib.pyplot as plt

# completing seperate code for the freefall case and the orbital cases
# as different coordinate systems will be used.
# We focus first on freefall, where we consider movement only along one line

def euler(r,v,M,G,tmax,dt):
#note that the results obtained are independent of the test mass

    t_array = np.arange(0, tmax, dt) #creates array of times up to t_max with step dt
    
    # initialise empty lists to record trajectories, where r is the radal vector
    r_list = []
    v_list = []
    
    # Euler integration
    for t in t_array:
        # append current state to trajectories
        r_list.append(r)
        v_list.append(v)
    
    
        a_direction = -1 * (r / np.linalg.norm(r))
        a_magnitude = (G * M) / ((np.linalg.norm(r))**2)
        
        # calculate new position and velocity
        a = a_magnitude * a_direction
        r = r + dt * v
        v = v + dt * a
        
        #comparator ensures that neither x,y or z r coordinate have hit earth.
        if r[0]<0 or r[1]<0 or r[2]<0:
            print(r)
            break
    
    while len(r_list) < len(t_array):
        r_list.append(np.array([0,0,0]))
        v_list.append(np.array([0,0,0]))
    
    r_list2 = []
    v_list2 = []
    
    for vector in r_list:
        r_list2.append(np.linalg.norm(vector))
        
    for vector in v_list:
        v_list2.append(np.linalg.norm(vector))
        
    altitude = np.array(r_list2)
    velocity = np.array(v_list2)
    
    plt.figure(1)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(t_array, altitude, label='altitude (m)')
    plt.plot(t_array, velocity, label='v (m/s)')
    plt.legend()
    plt.show()

def verlet(r,v,M,G,t_max,dt):
    
    #create list of times for plotting
    t_array = np.arange(0, t_max, dt)

    #initialise lists, note that we need two x values for verlet, so 
    #I found the second value using euler
    r_list = [r, r + dt * v]
    v_list = [v]
    
    
    #verlet intergtaion
    #note how the range is shifted by 1 to the right, since we already have our second value
    for t in range(1, len(t_array) - 1):
        
        F_direction = -1 * (r_list[t] / np.linalg.norm(r_list[t]))
        a_magnitude = (G * M) / ((np.linalg.norm(r_list[t]))**2)
        
        r = 2*r_list[t] - r_list[t-1] + ((dt ** 2) * (a_magnitude*F_direction))
        v = 1/(2*dt) * (r - r_list[t-1]) 
        
        r_list.append(r)
        v_list.append(v)
        
        #this is ONLY for straight descent
        #when the object hits earth it stops
        if r[0]<0 or r[1]<0 or r[2]<0:
            print(r)
            break
    
    #we also need the last value for v, which we find using the less accurate v(t+dt) formula
    v_list.append(1/dt * (r - r_list[t]))
    
    while len(r_list) < len(t_array):
        r_list.append(np.array([0,0,0]))
        v_list.append(np.array([0,0,0]))
    
    r_list2 = []
    v_list2 = []
    
    for vector in r_list:
        r_list2.append(np.linalg.norm(vector))
        
    for vector in v_list:
        v_list2.append(np.linalg.norm(vector))
    
    
    altitude = np.array(r_list2)
    velocity = np.array(v_list2)
    
    plt.figure(1)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(t_array, altitude, label='altitude (m)')
    plt.plot(t_array, velocity, label='v (m/s)')
    plt.legend()
    plt.show()

    
r0 = np.array([0,1000000,0])
v0 = np.array([0,0,0])
M = 6.42e23

G = 6.67384e-11

euler(r0, v0, M, G, 1000, 0.1)
verlet(r0, v0, M, G, 1000, 0.1)