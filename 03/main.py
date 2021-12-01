#Advent of Code - Day3 - hledani cesty mezi stromy
from Radek import Radek

#nastaveni smeru, vpravo a dolu, odpovidajici indexy ve dvou seznamech
right = [1,3,5,7,1]
down = [1,1,1,1,2]
pocet = []

## nacti data ze souboru a vytvor seznam instanci tridy Radek s parametrem line, delka radku a poradi radku
textFile = open("scratch.txt", "r")
data = []
poradiRadku = -1
for textImport in textFile:
    poradiRadku += 1
    line = Radek(str(textImport),poradiRadku)
    data.append(line)
textFile.close()

#hlavni cyklus od 0 -> 4, kazda iterace predava jiny parametr smeru v promenne down + right
for i in range(0,5,1):

    #vymazani vstupnich promennych
    location = 1-right[i]
    treeCount = 0

    #projde vsechny radky v seznamu data
    for line in data:
        #pokud narazi na spravny radek = poradi radku je
        #delitelne krokem dolu, overi jesti se na pozici nachazi strom
        if line.poradi % down[i] == 0:
            location += right[i]
            if location > line.length:
                location = location - line.length
            if line.isTree(location-1):
                treeCount += 1
    #pocet stromu v jednotlivych iteracich se uklada do seznamu
    pocet.append(treeCount)

#vynasobeni vysledneho seznamu a vypsani vysledku
result = 1
for i in pocet:
    result = result * i

print(result)