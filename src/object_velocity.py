import fuzzylogic.functions
from fuzzylogic.classes import *
from fuzzylogic.functions import *


def object_velocity() -> Domain:
    # Create the domain
    domain = Domain("Speed", 0, 10, res=0.1)

    # Create the membership functions
    S.maintain = fuzzylogic.functions.S(1.5, 3)
    S.soft = fuzzylogic.functions.triangular(2.5, 4)
    S.medium = fuzzylogic.functions.triangular(3.5, 8)
    S.emergency = fuzzylogic.functions.R(6, 6.5)

    return domain
