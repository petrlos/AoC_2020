#Advent of Code 2020 - Day 1

from cisla import Cisla
from datetime import datetime
start = datetime.now()


file = open("scratch.txt", "r")
data = []
for line in file:
    data.append(int(line))
file.close()

cisla = Cisla(data)
part1 = cisla.najdiDvojice()
part2 = cisla.najdiTrojice()

print("Part1: {0}".format(part1))
print("Part1: {0}".format(part2))

print("Runtime:",datetime.now()-start)