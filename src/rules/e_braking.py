import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
from typing import List

Rules = List[ctrl.Rule]

def generate_rules(object_distance: ctrl.Antecedent, object_speed: ctrl.Antecedent, object_acceleration: ctrl.Antecedent, e_braking: ctrl.Consequent) -> Rules:
    rules: Rules = []

    rules.append(ctrl.Rule(
        antecedent=object_distance["a"]
    ))

    return rules
