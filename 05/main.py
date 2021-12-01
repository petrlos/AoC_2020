#Advent of Code - Day 5 - Binary Bonding

from Seat import Seat

textFile = open("data.txt", "r")

maxID = 0

data = []

for textImport in textFile:
    seat = Seat(str(textImport))
    #metoda ktera prekoduje vstup do ciselne hodnoty
    seat.getId()
    # part1 - najdi nejvyssi seatID
    if seat.id > maxID:
        maxID = seat.id
    data.append(seat.id)
textFile.close()

data.sort()
lst = []

for i in range(1,len(data)-1,1):
    if (data[i-1]+data[i+1]) != (2*data[i]):
        lst.append(data[i])

freeSeat = int((lst[0]+lst[1])/2)

print("Volne sedadlo: {0}".format(freeSeat))


print("Nejvyssi ID sedadla: {0}".format(maxID))