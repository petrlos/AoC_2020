#Advent of Code - Day 13
from linky import Linky
from datetime import datetime

start=datetime.now()

#timeStamp = 939
#autobusyStr = "67,7,59,61"

timeStamp = 1008713
autobusyStr = "13,x,x,41,x,x,x,x,x,x,x,x,x,467,x,x,x,x,x,x,x,x,x,x,x,19," \
              "x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,353,x,x,x,x,x,37,x," \
              "x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23"


jizdnirad = Linky(autobusyStr)
print(jizdnirad)
print(jizdnirad.nextDeparture(timeStamp))

print(jizdnirad.postupnyOdjezd())

print(datetime.now()-start)
