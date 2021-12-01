# Advent of Code - Day 24: Lobby Layout - Hexgrid
from datetime import datetime
start = datetime.now()

def checkDuplicity(tile):
    #projde cely seznam tiles a hleda, jestli existuje dilek se stejnou adresou - pokud ano, vrati
    #jeho poradi v poli
    vysledek = -1
    for i in range(0,len(tiles)):
        if tile.x == tiles[i].x and tile.y == tiles[i].y:
            vysledek = i
    return vysledek

from tile import Tile
tiles = []

file = open("data.txt","r")
for line in file:
    newTile = Tile(line)
    kontrola = checkDuplicity(newTile)
    #pokud dilek neexistuje (-1), pripoji ho do seznamu, jinak obrati dile na indexu "kontrola"
    if kontrola == -1:
        tiles.append(newTile)
    else:
        tiles.pop(kontrola)


pocitadlo = 0
for tile in tiles:
    if tile.status == "black":
        pocitadlo += 1

print("Celkovy pocet cernych dilku: {0}".format(pocitadlo))
print("Runtime:", datetime.now()-start)