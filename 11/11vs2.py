#AoC Day 11 - Game of Life
def extendGrid(grid):
    # rozsirit mrizku o 1 bunku kazdym smerem - muzu pak projit vsechny sousedy
    # podle listu delta, nemusim se starat o delku retezce
    emptyRow = "x"*len(grid[0])
    newGrid = []
    newGrid.append("x" + emptyRow + "x")
    for line in grid:
        newGrid.append("x" + line + "x")
    newGrid.append("x" + emptyRow + "x")
    return newGrid

def task1(grid):
    #pocita jenom prime sousedy
    rows, cols = len(grid), len(grid[0])
    delta = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    grid = extendGrid(grid)
    newGrid = []
    for row in range(1,rows+1):
        newRow = ""
        for col in range(1, cols+1):
            neighbours = ""
            for deltax, deltay in delta:
                rowx = row + deltax
                coly = col + deltay
                neighbours += grid[rowx][coly]
            neighboursOccupied = neighbours.count("#")
            if grid[row][col] == "L" and neighboursOccupied == 0:
                newRow += "#"
            elif grid[row][col] == "#" and neighboursOccupied >= 4:
                newRow += "L"
            else:
                newRow += grid[row][col]
        newGrid.append(newRow)
    return newGrid

def task2(grid):
    #pocita vsechny viditelne sousedy
    rows, cols = len(grid), len(grid[0])
    delta = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    grid = extendGrid(grid)
    newGrid = []
    for row in range(1,rows+1):
        newRow = ""
        for col in range(1, cols+1):
            neighbours = ""
            for deltax, deltay in delta:
                rowx = row
                coly = col
                while True:
                    rowx = rowx + deltax
                    coly = coly + deltay
                    if grid[rowx][coly] != ".":
                        neighbours += grid[rowx][coly]
                        break
            neighboursOccupied = neighbours.count("#")
            if grid[row][col] == "L" and neighboursOccupied == 0:
                newRow += "#"
            elif grid[row][col] == "#" and neighboursOccupied >= 5:
                newRow += "L"
            else:
                newRow += grid[row][col]
        newGrid.append(newRow)
    return newGrid

#MAIN
from datetime import datetime
start = datetime.now()
print("AoC - Day 11")

with open ("data.txt" , 'r') as f:
    startGrid = [line.rstrip() for line in f.readlines()]

counter = 0
grid = startGrid * 1
while True:
    newGrid = task1(grid)
    if newGrid == grid:
        break
    else:
        grid = newGrid * 1
counter = 0
for line in grid:
    counter += line.count("#")
print("Task1:",counter)

counter = 0
grid = startGrid * 1
while True:
    newGrid = task2(grid)
    if newGrid == grid:
        break
    else:
        grid = newGrid * 1
counter = 0
for line in grid:
    counter += line.count("#")
print("Task2:",counter)

print("Runtime: ",datetime.now() - start)

