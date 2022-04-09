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

        # The universe will be 0 to 100 metres
        universe = np.arange(0, 100, 1)

        distance = Antecedent(universe, "object distance")

        # around 30 metres is the danger zone
        distance["danger"] = trapmf(universe, [0, 0, 20, 30])
        distance["near"] = trapmf(universe, [20, 30, 45, 60])
        distance["far"] = trapmf(universe, [45, 55, 100, 100])

        return distance

    @staticmethod
    def __speed() -> Antecedent:
        """
        The detected objects relative speed
        """

        # The universe is 0 - 100 km/h
        universe = np.arange(0, 100, 0.1)

        # Should really only be emergency braking or not
        speed = Antecedent(universe, "object speed")

        speed["none"] = trimf(universe, [0, 0, 5])
        speed["slow"] = trimf(universe, [2, 5, 15])
        speed["medium"] = trimf(universe, [5, 40, 70])
        speed["danger"] = trimf(universe, [50, 100, 100])

        return speed

    @staticmethod
    def __acceleration() -> Antecedent:
        """
        The detected objects relative acceleration
        """
        universe = np.arange(0, 20, 0.1)

        acceleration = Antecedent(universe, "object acceleration")

        acceleration["none"] = trimf(universe, [0, 0, 2])
        acceleration["low"] = trimf(universe, [1, 5, 10])
        acceleration["warning"] = trimf(universe, [5, 10, 15])
        acceleration["danger"] = trapmf(universe, [10, 15, 20, 20])

        return acceleration

    def view_all(self):
        self.distance.view()
        self.speed.view()
        self.acceleration.view()
