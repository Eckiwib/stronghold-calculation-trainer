import random
import math
import time
import json

with open("settings.json","r") as file:
    settings = json.load(file)

inp = 4

while True:
    difference_range = random.choice([True, False])
    if difference_range:
        difference = random.randint(38, 115) / 100
    else:
        difference = random.randint(114, 300) / 100
    
    angle_1 = random.randint(-18000, 18000) / 100
    angle_2 = angle_1 - difference
    while inp != difference:
        print(f"Angle 1 = {angle_1} Angle 2 = {angle_2}")
        inp = float(input())
