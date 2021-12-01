#Advent of Code 2020 - Day 9 Verze 2
from itertools import combinations

with open("data.txt") as file:
    numbers = [int(x) for x in file.read().splitlines()]
#Task1
for index in range(25, len(numbers)):
    if numbers[index] not in [sum(item) for item in combinations(numbers[index-25:index], 2)]:
        task1 = numbers[index]
print("Task1:",task1)
#Task2
for index in range(0, len(numbers)):
    for intervalIndex in range(0, index+1):
        controlSumNumbers = numbers[intervalIndex:index]
        if sum(controlSumNumbers) == task1 and len(controlSumNumbers) > 1:
            task2 = min(controlSumNumbers) + max(controlSumNumbers)
print("Task2:",task2)