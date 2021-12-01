## Advent of Code --- Day 18: Operation Order ---
from Line import Rovnice


textFile = open("data.txt", "r")

lines = []

for textImport in textFile:
    line = Rovnice(textImport)
    line.spocitejRadek()
    lines.append(line)
textFile.close()


suma_part1 = 0
suma_part2 = 0
for line in lines:
    suma_part1 += line.result

print("Suma: {0}".format(suma_part1))
