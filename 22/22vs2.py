#AoC Day 22 - Verze 2
import re
from datetime import datetime
start = datetime.now()

def task1(p1deck, p2deck):
    while True:
        if p1deck[0] > p2deck[0]:
            p1deck.append(p1deck[0]); p1deck.append(p2deck[0])
            p1deck = p1deck[1:]; p2deck = p2deck[1:]
        else:
            p2deck.append(p2deck[0]); p2deck.append(p1deck[0])
            p1deck = p1deck[1:]; p2deck = p2deck[1:]
        if len(p1deck) == 0 or len(p2deck) == 0:
            break

    #vypocet skore
    if len(p1deck) == 0:
        p1deck = p2deck
    return sum([a*b for a,b in zip(p1deck, range(len(p1deck), 0, -1))])

# MAIN:
with open("data.txt", "r") as file:
    inputData = ";".join([line.rstrip() for line in file.readlines()]).replace("Player ","P")

regexPlayer1 = re.compile(r"P1:(;\d*)*")
mo = regexPlayer1.search(inputData).group().split(";")[1:-2]
p1deck = [int(x) for x in mo]

regexPlayer2 = re.compile(r"P2:(;\d*)+")
mo = regexPlayer2.search(inputData).group().split(";")[1:]
p2deck = [int(x) for x in mo]


print("Result task1: {0}".format(task1(p1deck, p2deck)))
print("Total runtime: {0}".format(datetime.now()-start))