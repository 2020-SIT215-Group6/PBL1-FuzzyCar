import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl


def distance() -> ctrl.Antecedent:
    universe = np.arange(0, 100, 1)

    # Should really only be emergency braking or not
    distance = ctrl.Antecedent(universe, "object_distance")

    distance["danger"] = fuzz.trapmf(universe, [0, 0, 30, 50])
    distance["near"] = fuzz.trapmf(universe, [40, 60, 100, 200])
    distance["far"] = fuzz.trapmf(universe, [160, 250, 500, 500])

    return distance
