from typing import List
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
from skfuzzy import trapmf, trimf
from skfuzzy.control import Consequent, Rule

from Object import Object


Rules = List[Rule]


class CarController:
    def __init__(self):
        self.Object = Object()
        self.e_braking = CarController.__e_braking()
        self.e_braking_rules = self.__e_braking_rules()
        self.e_braking_controller = self.__e_brake_control_system()

    @staticmethod
    def __e_braking() -> Consequent:
        universe = np.arange(0, 1, 0.1)

        # Should really only be emergency braking or not
        braking = Consequent(universe, "car emergency braking")

        braking["normal"] = trimf(braking.universe, [0, 0, 0.7])
        braking["emergency"] = trimf(braking.universe, [0.5, 1, 1])

        return braking

    def __e_braking_rules(self) -> Rules:
        return [
            Rule(
                antecedent=(
                    self.Object.speed["none"] &
                    self.Object.acceleration["none"]
                ),
                consequent=self.e_braking["normal"]
            ),
            Rule(
                antecedent=(
                    self.Object.speed["slow"] &
                    self.Object.acceleration["none"]
                ),
                consequent=self.e_braking["normal"]
            ),
            Rule(
                antecedent=(
                    self.Object.speed["slow"] &
                    self.Object.acceleration["low"]
                ),
                consequent=self.e_braking["normal"]
            ),
            Rule(
                antecedent=(
                    self.Object.distance["danger"] |
                    self.Object.speed["danger"] |
                    self.Object.acceleration["danger"]
                ),
                consequent=self.e_braking["normal"]
            ),
            Rule(
                antecedent=(
                    self.Object.distance["near"] |
                    self.Object.distance["far"] |
                    self.Object.speed["none"] |
                    self.Object.speed["slow"] |
                    self.Object.speed["medium"] |
                    self.Object.acceleration["none"] |
                    self.Object.acceleration["low"] |
                    self.Object.acceleration["warning"]
                ),
                consequent=self.e_braking["normal"]
            )
        ]

    def __e_brake_control_system(self):
        return ctrl.ControlSystem(self.e_braking_rules)
