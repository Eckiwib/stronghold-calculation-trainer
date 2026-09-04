import random
import math
import time
import json
from color import RED, GREEN

with open("settings.json","r") as file:
    settings = json.load(file)

# Distance between thrown eyes
EYE_SPACING = settings["eye_spacing"]

# Calculate distance from difference
def kathete(difference):
    return round(EYE_SPACING / math.cos(math.radians(90-difference)))

# Algorithm to show the task and check the answer
# mode 1: Calculation style
# mode 2: Question style
def task(value1, result, value2=None, operator=None, mode=1):
    if mode == 1:
        inp = float(input(f"{value1} {operator} {value2} = "))
    if mode == 2:
        inp = float(input(f"{value1} : "))
    while inp != result:
        print(f"{RED}WRONG!")
        if mode == 1:
            inp = float(input(f"{value1} {operator} {value2} = "))
        if mode == 2:
            inp = float(input(f"{value1} : "))
    print(f"{GREEN}CORRECT!")

# mainloop
while True:
    difference = random.randint(38, 300) / 100
    angle_1 = random.randint(-18000, 18000) / 100
    angle_2 = round(angle_1 + difference, 2)
    distance = kathete(difference=difference)
    

    print("Difference:")
    task(value1=angle_2, value2=angle_1, result=difference, operator="-")

    print("Distance:")
    task(value1=difference, result=distance, mode=2)