from typing import Tuple

import numpy as np
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import Car


car_controller = Car.CarController()


# # object_distance = object.distance()
# # object_speed = object.speed()
#
# object_time_to_collision = object.time_to_collision()
# emergency_braking = car.e_braking()
#
def num_calc(calc: Tuple[int, float]):
    return calc[0] / calc[1]

distance_units = (100, 1)
speed_units = (100, 0.1)
acceleration_units = (20, 0.1)

ctrl_system = car_controller.e_braking_controller
sim = ctrl.ControlSystemSimulation(ctrl_system, flush_after_run=distance_units[0] * speed_units[0] * acceleration_units[0] + 1)

distance_samples = np.linspace(0, distance_units[0], 30)
speed_samples = np.linspace(0, speed_units[0], 30)
acceleration_samples = np.linspace(0, acceleration_units[0], 30)

x, y, z = np.meshgrid(distance_samples, speed_samples, acceleration_samples, indexing="ij")
a = np.zeros_like(x)

# Loop through the system 21*21 times to collect the control surface
for dist in range(10):
    for speed in range(10):
        for accel in range(10):
            sim.input["object distance"] = x[dist, speed, accel]
            sim.input["object speed"] = y[dist, speed, accel]
            sim.input["object acceleration"] = z[dist, speed, accel]
            sim.compute()
            a[dist, speed, accel] = sim.output["car emergency braking"]

# Plot the result in pretty 3D with alpha blending
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_trisurf(x, y, a, c=z, rstride=1, cstride=1, cmap='viridis',
                       linewidth=0.4, antialiased=True)
# surf = ax.plot_trisurf(x, y, z, c=a, rstride=1, cstride=1, cmap='viridis',
#                        linewidth=0.4, antialiased=True)
# img = ax.scatter(x, y, a, c=z, cmap=plt.hot())
# cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
# cset = ax.contourf(x, y, z, zdir='x', offset=3, cmap='viridis', alpha=0.5)
# cset = ax.contourf(x, y, z, zdir='y', offset=3, cmap='viridis', alpha=0.5)

# fig.view_init(30, 200)
plt.show()
