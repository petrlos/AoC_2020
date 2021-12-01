# Advent Of Code - Day 22 - Crab Combat

def vypocitejViteze(hrac, vitez, kola):
    suma = 0
    nasobic = len(hrac)
    for cisla in hrac:
        suma += cisla * nasobic
        nasobic -= 1
    message = "Vyhral {0} po {1} kolech s celkovym skore je: {2}". format(vitez, kola, suma)
    return message

textFile = open("data.txt", "r")

hrac1, hrac2 = [],[]
player = ""

for textImport in textFile:
    line = textImport[:-1]
    if "player" in line.lower():
        player = line
    if player == "Player 1:" and line.isdigit():
        hrac1.append(int(line))
    elif player == "Player 2:" and line.isdigit():
        hrac2.append(int(line))
textFile.close()

pocetKol = 0

print(max(hrac1))
print(max(hrac2))

while True:
    pocetKol += 1
    if hrac1[0] > hrac2[0]:
        #pokud ma hrac1 vyssi kartu, presune se nejdrive jeho karta na konec, pak hrace2
        hrac1.append(hrac1[0])
        hrac1.append(hrac2[0])
    else:
        #pokud ma hrac2 vyssi kartu, presune se nejdfive jeho karta na konec, pak hrace1
        hrac2.append(hrac2[0])
        hrac2.append(hrac1[0])
    #obe presunute karty je potreba vymazat
    hrac1.pop(0)
    hrac2.pop(0)
    if len(hrac1) == 0 or len(hrac2) == 0:
        break

if len(hrac1) > len(hrac2):
    vitez = vypocitejViteze(hrac1, "Hráč 1", pocetKol)
else:
    vitez = vypocitejViteze(hrac2, "Hráč 2", pocetKol)

print(vitez)