## GAME OF LIFE - Advent of Code Day 11
from gamefield import HerniPole
from datetime import datetime
start = datetime.now()

textFile = open("data.txt", "r")

gameField = []

for textImport in textFile:
    line = textImport[:-1]
    radek = []
    for znak in line:
        radek.append(str(znak))
    gameField.append(radek)
    dataField = HerniPole(gameField, len(radek), len(gameField))
textFile.close()

print("Pocet radku: {0}".format(dataField.pocetRadku))
print("Pocet sloupcu: {0}".format(dataField.pocetSloupcu))

pocitadlo = 0

while not dataField.stabilni:
    pocitadlo += 1
    dataField.preindexujPole()

print("Pocet zidli po stabilizaci pole: {0}".format(dataField.pocetZidli))
print("Pocet kroku potrebnych ke stabilizaci: {0}".format(pocitadlo))


print("Runtime:",datetime.now()-start)