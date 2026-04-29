import random
import math
import time
import json

with open("settings.json","r") as file:
    settings = json.load(file)

while True:
    difference_range = random.