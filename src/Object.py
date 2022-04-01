import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
from skfuzzy import trapmf, trimf
from skfuzzy.control import Antecedent, Rule


class Object:
    def __init__(self):
        self.distance = Object.__distance()
        self.speed = Object.__speed()
        self.acceleration = Object.__acceleration()

    @staticmethod
    def __distance() -> Antecedent:
        """
        The detected objects distance
        """
        universe = np.arange(0, 100, 1)

        # Should really only be emergency braking or not
        distance = Antecedent(universe, "object distance")

        distance["danger"] = trapmf(universe, [0, 0, 30, 50])
        distance["near"] = trapmf(universe, [40, 60, 100, 200])
        distance["far"] = trapmf(universe, [160, 250, 500, 500])

        return distance

    @staticmethod
    def __speed() -> Antecedent:
        """
        The detected objects relative speed
        """
        universe = np.arange(0, 100, 0.1)

        # Should really only be emergency braking or not
        speed = Antecedent(universe, "object speed")

        speed["none"] = trimf(universe, [0, 0, 10])
        speed["slow"] = trimf(universe, [0, 10, 20])
        speed["medium"] = trimf(universe, [50, 75, 100])
        speed["danger"] = trimf(universe, [50, 100, 100])

        return speed

    @staticmethod
    def __acceleration() -> Antecedent:
        """
        The detected objects relative acceleration
        """
        universe = np.arange(0, 50, 0.1)

        acceleration = Antecedent(universe, "object acceleration")

        acceleration["none"] = trimf(universe, [0, 0, 0.7])
        acceleration["low"] = trimf(universe, [0, 0, 1])
        acceleration["warning"] = trimf(universe, [0, 0, 1])
        acceleration["danger"] = trimf(universe, [0, 0, 1])

        return acceleration

    def view_all(self):
        self.distance.view()
        self.speed.view()
        self.acceleration.view()
