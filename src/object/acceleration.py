import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl


def acceleration() -> ctrl.Antecedent:
    universe = np.arange(0, 50, 0.1)

    # Should really only be emergency braking or not
    acceleration = ctrl.Antecedent(universe, "object_acceleration")

    acceleration["none"] = fuzz.trimf(universe, [0, 0, 0.7])
    acceleration["low"] = fuzz.trimf(universe, [0, 0, 1])
    acceleration["warning"] = fuzz.trimf(universe, [0, 0, 1])
    acceleration["danger"] = fuzz.trimf(universe, [0, 0, 1])

    return acceleration
