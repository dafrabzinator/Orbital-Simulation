import numpy as np

# Initial conditions
altitude = 200 # km
velocity = 7.8 # km/s

# Gravitational parameter of Earth (mu = G * M)
mu = 3.986e5 # km^3/s^2

# Calculate orbital radius
r = altitude + 6371 # km (6371 km is Earth's radius)

# Calculate orbital period
T = 2 * np.pi * np.sqrt(r**3 / mu) # seconds

# Time step for simulation
dt = T / 1000 # seconds

# Initial position and velocity vectors
pos = np.array([r, 0, 0]) # km
vel = np.array([0, velocity, 0]) # km/s

# Array to store position and velocity at each time step
positions = [pos]
velocities = [vel]

# Simulation loop
for i in range(1000):
    # Calculate acceleration vector
    acc = -mu * pos / np.linalg.norm(pos)**3

    # Update position and velocity
    pos = pos + vel*dt + 0.5*acc*dt**2
    vel = vel + acc*dt

    # Store position and velocity
    positions.append(pos)
    velocities.append(vel)

# Plot the results
import matplotlib.pyplot as plt

# Convert positions to arrays
positions = np.array(positions)

# Plot x and y positions
plt.plot(positions[:,0], positions[:,1])
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.show()
