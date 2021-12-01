## Advent of Code - Day 10 - Adapter Array
from adapters import Adapters

textFile = open("data.txt", "r")
data = []
for textImport in textFile:
    line = int(textImport)
    data.append(line)
textFile.close()

device = max(data) + 3
data.append(device)

data.sort()

getResult = Adapters(data)

print("Part1: {0}".format(getResult.part1()))
print("Part2: {0}".format(getResult.part2()))