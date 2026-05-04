import random
import math
import time
import json

with open("settings.json","r") as file:
    settings = json.load(file)

def distance(difference):
    return round(20 / math.cos(math.radians(90-difference)))

inp = 4

while True:
    operator = random.choice([True, False])
    difference = random.randint(38, 300) / 100
    angle_1 = random.randint(-18000, 18000) / 100
    if operator:
        angle_2 = round(angle_1 + difference, 2)
    else:
        angle_2 = round(angle_1 - difference, 2)

    while inp != difference:
        print()
        print(angle_1)
        print(angle_2)
        inp = float(input("Difference = "))

    print("Correct")
    inp = -1
    while inp != distance(difference=difference):
        inp = float(input("Distance = "))
    
    print("Correct")