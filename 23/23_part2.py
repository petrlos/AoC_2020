#Advent of Code 2020: Day 23

input = "156794823"

ct = dict() #crabTable

for index in range(len(input)):
    ct[int(input[index])] = int(input[(index + 1) % len(input)])

currentCup = int(input[0])
for moves in range(100):
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
for _ in range(8):
    next = ct[next]
    print(next, end = "")
print(" ")