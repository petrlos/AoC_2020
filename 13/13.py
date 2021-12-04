#Advent of Code 2020: Day 13 - created in 12/2021
import re
regNum = re.compile(r"\d+")

with open("data.txt") as file:
    lines = file.read().splitlines()

timestamp = int(lines[0])
busesTask1 = [int(x) for x in regNum.findall(lines[1])]

nextDeparture = {}
for bus in busesTask1:
    nextDeparture.setdefault(bus, bus - timestamp % bus)

for bus, departure in nextDeparture.items():
    if departure == min(nextDeparture.values()):
        print("Task 1:",bus * departure)

