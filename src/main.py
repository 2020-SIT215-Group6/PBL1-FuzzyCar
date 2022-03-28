import numpy
import fuzzylogic.functions
from matplotlib import pyplot
from fuzzylogic import *
from fuzzylogic.truth import *
from fuzzylogic.rules import *
from fuzzylogic.hedges import *
from fuzzylogic.classes import *
from fuzzylogic.functions import *
from fuzzylogic.combinators import *

from car_velocity import car_velocity
from object_distance import object_distance
from object_velocity import object_velocity

from matplotlib import pyplot


pyplot.rc("figure", figsize=(10, 10))

S = car_velocity()
D = object_distance()
V = object_velocity()

S.maintain.plot()
S.soft.plot()
S.medium.plot()
S.emergency.plot()
pyplot.show()
