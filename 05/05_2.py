#Advent of Code 2020: Day 5 created in 12/2021

with open("data.txt") as file:
    seats = file.read().splitlines()

seatIDs = []
for seat in seats:
    row = int(seat[0:7].replace("F","0").replace("B","1"), 2)
    column = int(seat[7:].replace("L","0").replace("R","1"), 2)
    seatIDs.append(row * 8 + column)

print("Task 1:",max(seatIDs))

#Task 2
for seat in range(max(seatIDs)+1):
    if seat not in seatIDs:
        if (seat-1 in seatIDs) and (seat+1 in seatIDs):
            print("Task 2:",seat)