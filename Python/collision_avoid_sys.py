import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class Collision_Avoid_Sys:
    def __set_mem_function(self) -> None:
        self.distance['veryclose'] = fuzz.trimf(self.distance.universe,[0,0,20])
        self.distance['close']     = fuzz.trimf(self.distance.universe,[10,25,40])
        self.distance['near']      = fuzz.trimf(self.distance.universe,[30,45,60])
        self.distance['far']       = fuzz.trimf(self.distance.universe,[50,65,80])
        self.distance['veryfar']   = fuzz.trimf(self.distance.universe,[65,100,100])

        self.speed['veryslow']   = fuzz.trimf(self.speed.universe,[0,0,40])
        self.speed['slow']       = fuzz.trimf(self.speed.universe,[20,35,50])
        self.speed['medium']     = fuzz.trimf(self.speed.universe,[40,50,60])
        self.speed['fast']    = fuzz.trimf(self.speed.universe,[50,70,90])
        self.speed['veryfast']    = fuzz.trimf(self.speed.universe,[70,110,110])

        self.brak_pressure['verylight'] = fuzz.trimf(self.brak_pressure.universe,[0,2,4])
        self.brak_pressure['light'] = fuzz.trimf(self.brak_pressure.universe,[2,4,6])
        self.brak_pressure['medium'] = fuzz.trimf(self.brak_pressure.universe,[4,6,8])
        self.brak_pressure['heavy'] = fuzz.trimf(self.brak_pressure.universe,[6,8,10])
        self.brak_pressure['veryheavy'] = fuzz.trimf(self.brak_pressure.universe,[8,10,10])
    
    def __set_rules(self) -> None:
        self.rules.append(ctrl.Rule(self.distance['veryclose'] & self.speed['veryslow'], self.brak_pressure['medium']))
        self.rules.append(ctrl.Rule(self.distance['veryclose'] & self.speed['slow'], self.brak_pressure['veryheavy']))
        self.rules.append(ctrl.Rule(self.distance['veryclose'] & self.speed['medium'], self.brak_pressure['veryheavy']))
        self.rules.append(ctrl.Rule(self.distance['veryclose'] & self.speed['fast'], self.brak_pressure['veryheavy']))
        self.rules.append(ctrl.Rule(self.distance['veryclose'] & self.speed['veryfast'], self.brak_pressure['veryheavy']))

        self.rules.append(ctrl.Rule(self.distance['close'] & self.speed['veryslow'], self.brak_pressure['verylight']))
        self.rules.append(ctrl.Rule(self.distance['close'] & self.speed['slow'], self.brak_pressure['light']))
        self.rules.append(ctrl.Rule(self.distance['close'] & self.speed['medium'], self.brak_pressure['veryheavy']))
        self.rules.append(ctrl.Rule(self.distance['close'] & self.speed['fast'], self.brak_pressure['veryheavy']))
        self.rules.append(ctrl.Rule(self.distance['close'] & self.speed['veryfast'], self.brak_pressure['veryheavy']))

        self.rules.append(ctrl.Rule(self.distance['near'] & self.speed['veryslow'], self.brak_pressure['verylight']))
        self.rules.append(ctrl.Rule(self.distance['near'] & self.speed['slow'], self.brak_pressure['verylight']))
        self.rules.append(ctrl.Rule(self.distance['near'] & self.speed['medium'], self.brak_pressure['light']))
        self.rules.append(ctrl.Rule(self.distance['near'] & self.speed['fast'], self.brak_pressure['veryheavy']))
        self.rules.append(ctrl.Rule(self.distance['near'] & self.speed['veryfast'], self.brak_pressure['veryheavy']))

        self.rules.append(ctrl.Rule(self.distance['far'] & self.speed['veryslow'], self.brak_pressure['verylight']))
        self.rules.append(ctrl.Rule(self.distance['far'] & self.speed['slow'], self.brak_pressure['verylight']))
        self.rules.append(ctrl.Rule(self.distance['far'] & self.speed['medium'], self.brak_pressure['verylight']))
        self.rules.append(ctrl.Rule(self.distance['far'] & self.speed['fast'], self.brak_pressure['light']))
        self.rules.append(ctrl.Rule(self.distance['far'] & self.speed['veryfast'], self.brak_pressure['veryheavy']))

        self.rules.append(ctrl.Rule(self.distance['veryfar'] & self.speed['veryslow'], self.brak_pressure['verylight']))
        self.rules.append(ctrl.Rule(self.distance['veryfar'] & self.speed['slow'], self.brak_pressure['verylight']))
        self.rules.append(ctrl.Rule(self.distance['veryfar'] & self.speed['medium'], self.brak_pressure['verylight']))
        self.rules.append(ctrl.Rule(self.distance['veryfar'] & self.speed['fast'], self.brak_pressure['verylight']))
        self.rules.append(ctrl.Rule(self.distance['veryfar'] & self.speed['veryfast'], self.brak_pressure['heavy']))

        self.breaking_sim = ctrl.ControlSystemSimulation(ctrl.ControlSystem(self.rules))

    def show_sim(self):
        self.distance.view(sim=self.breaking_sim)
        self.speed.view(sim=self.breaking_sim)
        self.brak_pressure.view(sim=self.breaking_sim)

    # calculate brake pressure
    def brak(self, speed: int, distance: int):
        self.breaking_sim.input['distance'] = distance
        self.breaking_sim.input['speed'] = speed
        self.breaking_sim.compute()
        return self.breaking_sim.output['brak']

    def __init__(self) -> None:
        self.distance = ctrl.Antecedent(np.arange(0,100,1),'distance')
        self.speed = ctrl.Antecedent(np.arange(0,110,1),'speed')
        self.brak_pressure = ctrl.Consequent(np.arange(0,11,1),'brak')
        self.rules = []
        self.breaking_sim = None
        
        self.__set_mem_function()
        self.__set_rules()
