# Advent of Code - Day7
from collections import deque

def task1(shiny):
    for parent in bags.keys():
        queue.append([parent])
    results = set()
    while queue:
        for _ in range(len(queue)):
            checkedBag = queue[0]
            for kid in bags[checkedBag[-1]]:
                if kid[2:] == shiny:
                    results.add(checkedBag[0])
                else:
                    newPath = checkedBag + [kid[2:]]
                    if kid != "no other bag":
                        queue.append(newPath)
            queue.popleft()
    return len(results)

#MAIN
with open("data.txt") as file:
    lines = [line[:-1] for line in file.read().replace("bags", "bag").splitlines()]

bags = {}
queue = deque()
for line in lines:
    bag = line.split(" contain ")
    parent, kids = bag
    kids = kids.split(", ")
    bags[parent] = kids

shiny = "shiny gold bag"

print("Task 1:", task1(shiny))