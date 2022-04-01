import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

import car
import object
import rules.e_braking

object_distance = object.distance()

object_distance.view()


# # object_distance = object.distance()
# # object_speed = object.speed()
#
# object_time_to_collision = object.time_to_collision()
# emergency_braking = car.e_braking()
#
# system = ctrl.ControlSystem(rules=rules.e_braking.generate_rules(object_time_to_collision, emergency_braking))
# sim = ctrl.ControlSystemSimulation(system, flush_after_run=50 * 50 + 1)
#
# object_speed.view()
# object_distance.view()
# # object_time_to_collision.view()
# # emergency_braking.view()
#
# upsampled = np.linspace(0, 49, 49)
# x = upsampled
# y = np.zeros_like(x)
#
# # Loop through the system 21*21 times to collect the control surface
# for i in range(49):
#     sim.input['time_to_collision'] = x[i]
#     sim.compute()
#     y[i] = sim.output['emergency_braking']
#
# # Plot the result in pretty 3D with alpha blending
# import matplotlib.pyplot as plt
#
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(111)
# ax.plot(x, y)
#
# plt.show()
