#Advent of Code - Day 23 - Crab Cups

#TODO: naive and brute force, works fine for task1, definitely not for task2

from collections import deque

input = "156794823"

data = deque(input)

rounds = 100
currentCup = 0

for pocitadlo in range(0, rounds, 1):
    currentCupValue = data[currentCup]

    while data.index(currentCupValue) != 0:
        backUp = data[0]
        data.popleft()
        data.append(backUp)
    currentCup = data.index(currentCupValue)
    pickUp = ""
    #destinationCup je hodnota hrnicku na aktualni pozici -1
    #NENI TO INDEX, ale hodnota na hrnku
    destinationCup = int(data[currentCup]) - 1
    if destinationCup == 0:
        destinationCup = 9
    #vybere 3 nasledujici hrnicky od pozice current cup
    for i in range(currentCup+1, currentCup+4, 1):
        pickUp += data[i]
    #prevedeni na deque
    pickUp = deque(pickUp)
    #vymazani prvku v pickUp z data
    for toBeDeleted in pickUp:
        data.remove(toBeDeleted)
    #uprava destination: pokud je destination jeden z hrnicku, ktere jsou v pickup, odecte jedna,
    #dokud nenajde takovy, ktery tam neni
    #v okamziku preteceni do nuly zacne znova od nejvyssiho
    while str(destinationCup) in pickUp:
        destinationCup -= 1
        if destinationCup <= 0:
            destinationCup = 9
    #najde index destinationCup po vymazani pickUp
    destinationIndex = data.index(str(destinationCup))
    #vlozi pickUp na index destinationIndex
    for i in range(0, 3):
        data.insert(destinationIndex + 1 + i, pickUp[i])
    #najdi spravnou pozici nasledujiciho hrnku:
    currentCup = data.index(str(currentCupValue)) + 1
    if currentCup > 9:
        currentCup = 0

while data.index("1") != 0:
    backUp = data[0]
    data.popleft()
    data.append(backUp)

data.popleft()
result = ""
for cisla in data:
    result += cisla

print("Task 1:",result)