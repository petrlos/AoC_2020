#Advent of Code 2020: Day 23
from datetime import datetime
startTime = datetime.now()

def letsPlayAGameTask1(rounds):
    currentCup = int(input[0])
    for moves in range(rounds):
        triplet = [ct[currentCup], ct[ct[currentCup]], ct[ct[ct[currentCup]]]]
        destCup = currentCup - 1
        if destCup == 0:
            destCup += 9
        while destCup in triplet:
            destCup -= 1
            if destCup == 0:
                destCup += 9
        ct[triplet[-1]], ct[destCup], ct[currentCup] = ct[destCup], triplet[0], ct[triplet[-1]]
        currentCup = ct[currentCup]
    next = 1
    result = ""
    for _ in range(8):
        next = ct[next]
        result += str(next)
    return result

def letsPlayAGameTask2(rounds):
    currentCup = int(input[0])
    for moves in range(rounds):
        triplet = [ct[currentCup], ct[ct[currentCup]], ct[ct[ct[currentCup]]]]
        destCup = currentCup - 1
        if destCup == 0:
            destCup = 1000000
        while destCup in triplet:
            destCup -= 1
            if destCup == 0:
                destCup = 1000000
        ct[triplet[-1]], ct[destCup], ct[currentCup] = ct[destCup], triplet[0], ct[triplet[-1]]
        currentCup = ct[currentCup]
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
print("Task 1:",letsPlayAGameTask1(100))

ct = dict() #crabTable
#startsequence
for index in range(len(input)):
    ct[int(input[index])] = int(input[(index + 1) % len(input)])
for i in range(10,1000001):
    ct[i] = i+1
ct[int(input[-1])] = 10 #last number in input points to 10
ct[1000000] = int(input[0]) #cup 1.000.000 points to first cup
print("Task 2:", letsPlayAGameTask2(10000000))

print("Runtime:", datetime.now() - startTime)