# Advent of Code - Day7
from pprint import pprint as pp

#TODO: not working recursion

def findShinyBag(shiny, bag):
    for child in bags[bag]:
        if child == shiny:
            return True
        else:
            findShinyBag(shiny, child)
    return False

#MAIN
with open("test.txt") as file:
    data = file.read().splitlines()

result = []

bags = {}
for line in data:
    textLine = line.replace(" contain", ":").replace("bags", "bag").replace(".","")
    textLine = textLine.split(": ")
    if not textLine[0] in bags.keys():
        bags.setdefault(textLine[0], textLine[1].split(", "))

shiny = "shiny gold bag"

pp(bags)

#task1
counter = 0
for bag in bags.keys():
    if findShinyBag(shiny, bag):
        counter += 1

print(counter)
