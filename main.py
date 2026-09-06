import random
import math
import json
from color import RED, GREEN

with open("settings.json","r") as file:
    settings = json.load(file)

EYE_SPACING = settings["eye_spacing"]
AGL_DIF_STRT = int(settings["angle_difference_start"])
AGL_DIF_END = int(settings["angle_difference_end"])
COORD_STRT = int(settings["coordinate_start"])
COORD_END = int(settings["coordinate_end"])

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
    difference = random.randint(AGL_DIF_STRT, AGL_DIF_END) / 100
    angle_1 = random.randint(-18000, 18000) / 100
    angle_2 = round(angle_1 + difference, 2)
    distance = round(EYE_SPACING / math.cos(math.radians(90-difference)))
    z_coord = random.randint(COORD_STRT, COORD_END)
    x_coord = random.randint(COORD_STRT, COORD_END)
    angle_norm = angle_2 % 90
    z_perc = math.cos(math.radians(angle_norm))
    x_perc = math.sin(math.radians(angle_norm))
    local_z_sum = distance * z_perc
    local_x_sum = distance * x_perc

    print("Difference:")
    task(value1=angle_2, value2=angle_1, result=difference, operator="-")

    print("Distance:")
    task(value1=difference, result=distance, mode=2)

    print("Apply clock method on angle 2:")
    task(value1=angle_2, result=angle_norm, mode=2)

    print("Z percentage:")
    task(value1=angle_norm, result=round(z_perc, 3), mode=2)

    print("X percentage:")
    task(value1=angle_norm, result=round(x_perc, 3), mode=2)

    print("Z sum:")
    task(value1=distance, value2="Z percentage", result=local_z_sum, operator="*")

    print("X sum:")
    task(value1=distance, value2="X percentage", result=local_x_sum, operator="*")