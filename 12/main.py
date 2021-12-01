# Advent of Code - Day 12
from ship import Ship
from ship_2 import Ship2

textFile = open("data.txt", "r")

instructions = []

lod = Ship()
lepsiLod = Ship2()

for textImport in textFile:
    line = textImport[:-1]
    instructions.append(line)
textFile.close()

print(lepsiLod)
#Day12 Part1
#for instrukce in instructions:
#    lod.provedInstrukci(instrukce)
#print("Day12 Part 1: {0}".format(lod.kolikUjela()))

for instrukce in instructions:
    lepsiLod.provedInstrukci(instrukce)
print(lepsiLod)
print("Lod ujela: {}".format(lepsiLod.kolikUjela()))

