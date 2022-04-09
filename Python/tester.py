from collision_avoid_sys import Collision_Avoid_Sys as CAS
from helper import Helper

"""Tester extract data to csv so that we can adjust or rules.
"""
def speed_on_queensland_datasheet(mul=1):
    # base on https://www.qld.gov.au/transport/safety/road-safety/driving-safely/stopping-distances/graph
    cas = CAS()
    test_speed = [40, 50, 60, 70, 80, 90, 100, 110]
    test_distance = [9, 14, 20, 27, 36, 45, 56, 67]

    csv_data = []
    for m in range(1, mul + 1):
        csv_data.append(['distance', 'speed', 'brake_pressure'])
        for i in range(len(test_speed)):
            speed = test_speed[i]
            distance = test_distance[i] * m
            brake_pressure = cas.brak(speed, distance)
            csv_data.append([distance, speed, brake_pressure])
    Helper.explot_csv("Queensland_Datasheet_Compare.csv", csv_data)

def targeted_speed_with_each_distance(speed, testing_range=100):
    cas = CAS()
    csv_data = [['distance', 'speed', 'brake_pressure']]
    for distance in range(testing_range):
        brake_pressure = cas.brak(speed, distance)
        csv_data.append([distance, speed, brake_pressure])
    Helper.explot_csv("Fixed_Speed_With_Diff_Distance.csv", csv_data)

def all_speed_distance(speed=110, distance = 100):
    cas = CAS()
    csv_data = [['distance', 'speed', 'brake_pressure']]
    for speed in range(speed):
        for distance in range(distance):
            brake_pressure = cas.brak(speed, distance)
            csv_data.append([distance, speed, brake_pressure])
    Helper.explot_csv("Speed110_Distance100.csv", csv_data)