#Advent of Code 2020 Day 20
from functools import reduce

def getEdges(tile, init=False):
    #vrati list vsech moznych okraju 1 dilku, rotated i flipped
    notFlippedEdges = []
    notFlippedEdges.append(tile[0]) # horni radek
    notFlippedEdges.append("".join(list(reversed(tile[-1])))) #spodni radek zprava doleva
    notFlippedEdges.append("".join([line[-1] for line in tile])) # pravy sloupec zeshora dolu
    notFlippedEdges.append("".join(list(reversed([line[0] for line in tile])))) #levy sloupec od zdola nahoru
    flippedEdges = []
    if init:
        for edge in notFlippedEdges:
            flippedEdge = "".join(list(reversed(edge)))
            flippedEdges.append(flippedEdge)
    edges = flippedEdges + notFlippedEdges
    return edges

#MAIN

with open("data.txt") as file:
    data = file.read().split("Tile ")
data.pop(0)

#vytvori dict ve formatu "cisloDilku: [list radku dilku]"
tiles = {}
for tile in data:
    lineSplit = tile.split(":")
    lineSplit[1] = lineSplit[1][1:-2]
    tiles.setdefault(int(lineSplit[0]), lineSplit[1].split("\n"))

#vygeneruje list vsech moznych okraju
allEdges = []
for tile in tiles.values():
    possibleEdges = getEdges(tile, True)
    for edge in possibleEdges:
        allEdges.append(edge)

#spocita, kolik ze 4 okraju se vyskytuje v seznamu prave 1x = jedna se o okraj
counter = {}
for tileKey in tiles.keys():
    tileEdges = getEdges(tiles[tileKey])
    counter.setdefault(tileKey, 0)
    for tileEdge in tileEdges:
        if allEdges.count(tileEdge) == 1:
            counter[tileKey] += 1

#najde dilky, jejichz pocet okraju vyskytujicich se prave 1x je roven prave dvema - jedna se o roh
result = []
for tileKey in counter:
    if counter[tileKey] == 2:
        result.append(tileKey)

print("Corner tiles:", result)

print("Task 1:", reduce((lambda  x, y: x * y), result))