import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl


def e_braking() -> ctrl.Consequent:
    universe = np.arange(0, 1, 0.1)

    # Should really only be emergency braking or not
    braking = ctrl.Consequent(universe, "emergency_braking")

    braking["normal"] = fuzz.trimf(braking.universe, [0, 0, 0.7])
    braking["emergency"] = fuzz.trimf(braking.universe, [0.5, 1, 1])

    return braking
