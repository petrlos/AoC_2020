#AoC Day 24 - Verze 2
from datetime import datetime
import re, operator, copy
start = datetime.now()

def task1():
    tiles = {}
    for line in instructions:
        tile = [directions[key] for key in regexPatern.findall(line)]
        coordX, coordY = 0, 0
        for x, y in tile:
            coordX += x
            coordY += y
        if (coordX, coordY) in tiles.keys():
            tiles[coordX,coordY] = False
        else:
            tiles.setdefault((coordX, coordY), True)
    return tiles

def countBlackTiles(grid):
    return len(list(filter(lambda x: x, grid.values())))

def task2(startGrid):
    allPossibleTiles = startGrid
    #ziska ze vstupnich dat dictionary ve formatu (x,y):True/False - souradnice dilku:True=black/False=white
    newGrid = copy.deepcopy(allPossibleTiles)
    for days in range(1,101):
        #zkopiruje aktualni stav do newGrid a prida vsechny okolni bunky, ktere se mohou v tomto tahu rozsvitit
        for key in allPossibleTiles.keys():
            for value in directions.values():
                newCoords = tuple(map(operator.add, key, value))
                newGrid.setdefault(newCoords, False)
        #kopie z newGrid do allPossibleTiles
        allPossibleTiles = copy.deepcopy(newGrid)
        for key in allPossibleTiles.keys():
            counter = 0
            for value in directions.values():
                newCoords = tuple(map(operator.add, key, value))
                if newCoords in allPossibleTiles.keys():
                    if allPossibleTiles[newCoords] == True:
                        counter += 1
            if allPossibleTiles[key] == True:
                if counter == 0 or counter > 2:
                    newGrid[key] = False
            else:
                if counter == 2:
                    newGrid[key] = True
        allPossibleTiles = copy.deepcopy(newGrid)
        if days % 10 == 0:
            print("{0}% done in {1}".format(days, datetime.now()-start))
    return countBlackTiles(allPossibleTiles)

#MAIN
#black = True, white = False
print("AoC Day 24")

regexPatern = re.compile(r"(nw|ne|se|sw|w|e)")
directions = {"nw":(-1,1), "ne":(0,1), "w":(-1,0), "e":(1,0), "sw":(0,-1), "se":(1,-1)}

with open("data.txt","r") as f:
    instructions = [line.rstrip() for line in f.readlines()]

startGrid = task1()

print("Task 1: ", countBlackTiles(startGrid))
print("Task 2: ", task2(startGrid))
print("Total Runtime:", datetime.now()-start)