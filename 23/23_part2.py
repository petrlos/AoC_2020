#Advent of Code 2020: Day 23
from datetime import datetime
startTime = datetime.now()

def letsPlayAGame(rounds, max, task1 = True):
    currentCup = int(input[0])
    for moves in range(rounds):
        triplet = [ct[currentCup], ct[ct[currentCup]], ct[ct[ct[currentCup]]]]
        destCup = currentCup - 1
        if destCup == 0:
            destCup += max
        while destCup in triplet:
            destCup -= 1
            if destCup == 0:
                destCup += max
        ct[triplet[-1]], ct[destCup], ct[currentCup] = ct[destCup], triplet[0], ct[triplet[-1]]
        currentCup = ct[currentCup]
    next = 1
    result = ""
    if task1:
        for _ in range(8):
            next = ct[next]
            result += str(next)
        return result
    else:
        next = 1
        result = 1
        for _ in range(2):
            next = ct[next]
            result *= next
        return result

#MAIN
input = "156794823"

ct = dict() #crabTable
#startsequence
for index in range(len(input)):
    ct[int(input[index])] = int(input[(index + 1) % len(input)])
print("Task 1:",letsPlayAGame(100, 9))

ct = dict() #crabTable
#startsequence
for index in range(len(input)):
    ct[int(input[index])] = int(input[(index + 1) % len(input)])
for i in range(10,1000001):
    ct[i] = i+1
ct[int(input[-1])] = 10 #last number in input points to 10
ct[1000000] = int(input[0]) #cup 1.000.000 points to first cup
print("Task 2:", letsPlayAGame(10000000, 1000000, False))

print("Runtime:", datetime.now() - startTime)