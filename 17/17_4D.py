#Advent of Code: Day 17: 4D GameOfLife
from copy import deepcopy

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def getNeighbours(coords):
    neighbours = 0
    for deltaX in range(-1,2,1):
        for deltaY in range(-1, 2, 1):
            for deltaZ in range(-1, 2, 1):
                for deltaW in range(-1, 2, 1):
                    if not (deltaX == deltaY == deltaZ == deltaW == 0):
                        neighbour = tupleSum((deltaX, deltaY, deltaZ, deltaW), coords)
                        if neighbour in grid:
                            neighbours += 1
    return neighbours

#MAIN

with open("data.txt") as file:
    data = file.read().splitlines()

grid = set()
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "#":
            grid.add((x,y,0,0))

xMax = x
yMax = y

newGrid = set()

for step in range(0,6):
    for x in range(0-step-1, xMax+step+2, 1):
        for y in range(0-step-1, yMax+step+2, 1):
            for z in range(0-step-1, 0+step+2, 1):
                for w in range(0-step-1, 0+step+2, 1):
                    neighbourCount = getNeighbours((x,y,z,w))
                    if (x,y,z,w) in grid:
                        if neighbourCount in [2,3]:
                            newGrid.add((x,y,z,w))
                    else:
                        if neighbourCount == 3:
                            newGrid.add((x,y,z,w))
    grid = deepcopy(newGrid)
    newGrid = set()

print("Task 2:", len(grid))