import pygame
import math
from collision_avoid_sys import Collision_Avoid_Sys as CAS
from helper import Helper

REFRESH_TIME = 50
VEHICLE_SIZE = 20

# Value to activate CAS
CAS_TRIGGER_DISTANCE = 100

class Enviroment_Simluator:
    class Vehicle:
        # only going forward.
        def __init__(self, speed, pos={'x': 0, "y": 0}, size={'x': 10, 'y': 10}) -> None:
            self.speed = speed
            self.brak_pressure = 0
            self.size = size
            self.pos = pos
            self.cas = CAS()
            self.cas_flag = True
            self.abs_flag = False
            self.cc_flag = False
        
        def set_speed(self, speed):
            self.speed = speed

        def set_pos(self, pos):
            self.pos = pos

        def set_size(self, x, y):
            self.size['x'] = x
            self.size['y'] = y

        def calc_distance(self, obj)->float:
            return math.hypot(self.pos['x']-obj.pos['x']+VEHICLE_SIZE, self.pos['y']-obj.pos['y'])

        # evaluate brake pressure
        def eva_cas(self, vehicle):
            if self.cas_flag is True:
                distance = self.calc_distance(vehicle)
                if distance < CAS_TRIGGER_DISTANCE:
                    self.brak_pressure = self.cas.brak(self.speed, distance)
                    self.set_speed(Helper.brak_efficent(self.speed, self.brak_pressure))

        def eva_abs(self):
            pass
        
        def eva_cc(self):
            pass

    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        self.hud = pygame.font.SysFont('Comic Sans MS', 10)
        self.running = False
        self.screen  = pygame.display.set_mode([1024, 768])
        self.vehicles = []
        self.time_pass = 0
        self.collision_flag = False
        self.start()
    
    def collision_dection(self, a, b):
        return True if b.pos['x'] <= a.pos['x'] + VEHICLE_SIZE else False

    def draw_vehicle(self, vehicles):
        for vehicle in vehicles:
            new_pos = {'x':vehicle.pos['x'] + vehicle.speed / 10, 'y': vehicle.pos['y']}
            pygame.draw.rect(self.screen, (0, 0, 255), [new_pos['x'], new_pos['y'], VEHICLE_SIZE, 20])
            # update pos
            vehicle.set_pos(new_pos)

    # cas: collision_avoid_system
    # abs: Anti-lock Braking System
    # cc: Cruise Control
    def draw_hud(self, speed, distance, cas_flag, abs_flag, cc_flag):
        textsurface = self.hud.render(
            'Speed: {}KM/H | Distance: {}M | CAS: {} | ABS: {} | CC: {} | Collision: {}'
            .format(speed, distance, cas_flag, abs_flag, cc_flag, self.collision_flag)
            , False, (0, 0, 0))

        self.screen.blit(textsurface, (500, 20))

    def start(self):
        # Create two object on the game
        self.vehicles.append(self.Vehicle(100.0, {'x': 0, 'y': 500}))
        self.vehicles.append(self.Vehicle(0, {'x': 500, 'y': 500}))

        csv_data = [['distance', 'speed', 'brake_pressure']]

        # make sure the csv is exported once
        is_exported = False
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            ### Used to show fig, no need for implementation
            # if self.vehicles[0].speed > 40 and self.vehicles[0].speed < 60:
            #     csv_data.append([
            #         self.vehicles[0].calc_distance(self.vehicles[1]),
            #         self.vehicles[0].speed, 
            #         self.vehicles[0].brak_pressure
            #         ])
            #     self.vehicles[0].cas.show_sim()

            # get brake pressure base on two object disatnce and speed using fuzzy logic.
            self.vehicles[0].eva_cas(self.vehicles[1])

            self.draw_vehicle(self.vehicles)
            self.draw_hud(self.vehicles[0].speed, 
                self.vehicles[0].calc_distance(self.vehicles[1]), 
                self.vehicles[0].cas_flag,
                self.vehicles[0].abs_flag,
                self.vehicles[0].cc_flag)

            # export data when simluation finish
            if self.vehicles[0].speed == 0 and is_exported == False:
                Helper.explot_csv("vehicle_status.csv", csv_data)
                is_exported = True
                
            # stop vehicle if collision
            if self.collision_dection(self.vehicles[0], self.vehicles[1]) is True:
                self.vehicles[0].set_speed(0)
                self.collision_flag = True

            pygame.display.flip()
            pygame.time.delay(REFRESH_TIME)
            self.time_pass += REFRESH_TIME

        return 0