#Advent of Code - Day 25

doorPublic, cardPublic = 12232269, 19452773 #ostra data

#doorPublic, cardPublic = 5764801, 17807724

loopDoor = 0
p = 20201227
vysledek = 1
mezivysledek = 1


while vysledek != doorPublic:
    loopDoor += 1
    vysledek = vysledek * 7 % p


secretKey = pow(cardPublic, loopDoor, p)

print(secretKey)

