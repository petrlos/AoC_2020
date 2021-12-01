## Advent of Code: Day 15 - Memory Game
from datetime import datetime
start = datetime.now()

from Rada import Rada

sample1 = Rada([1,2,3], 2020)
print(sample1)

sample2 = Rada([2,1,3], 2020)
print(sample2)

part1 = Rada([9,12,1,4,17,0,18], 2020)
print(part1)

print(" ")
print("Runtime: {0}".format(datetime.now() - start))