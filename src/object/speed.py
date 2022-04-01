import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl


def speed() -> ctrl.Antecedent:
    universe = np.arange(0, 100, 0.1)

    # Should really only be emergency braking or not
    speed = ctrl.Antecedent(universe, "object relative speed")

    speed["none"] = fuzz.trimf(universe, [0, 0, 10])
    speed["slow"] = fuzz.trimf(universe, [0, 10, 20])
    speed["medium"] = fuzz.trimf(universe, [50, 75, 100])
    speed["danger"] = fuzz.trimf(universe, [50, 100, 100])

    return speed
