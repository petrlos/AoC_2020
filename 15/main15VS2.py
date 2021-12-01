from datetime import datetime
print("Elf Memory Game")

start = datetime.now()
#predposledni vyskyt: hodnota:pozice
predposledniDict = {}

searchIndex = 30000000
cisla = [9,12,1,4,17,0,18]
poradi = list(range(1,len(cisla)+1))

#posledni vyskyt: hodnota:pozice
posledniDict = {cisla[i]: poradi[i] for i in range(len(cisla))}

posledniHodnota = cisla[-1]

print("Hledam {0}. cislo z pocatecni rady: {1}".format(searchIndex, cisla))

for counter in range(len(cisla)+1,searchIndex + 1):
    if counter % 3000000 == 0:
        print("{0}% hotovo".format(counter/3000000*10))

    if posledniHodnota not in predposledniDict.keys():
        posledniHodnota = 0
        if posledniHodnota not in posledniDict.keys():
            posledniDict.setdefault(posledniHodnota)
            posledniDict[posledniHodnota] = counter
        else:
            predposledniDict.setdefault(posledniHodnota)
            predposledniDict[posledniHodnota] = posledniDict[posledniHodnota]
            posledniDict[posledniHodnota] = counter
    else:
        vzdalenost = posledniDict[posledniHodnota] - predposledniDict[posledniHodnota]
        if vzdalenost not in posledniDict.keys():
            posledniDict.setdefault(vzdalenost)
            posledniDict[vzdalenost] = counter
        else:
            predposledniDict.setdefault(vzdalenost)
            predposledniDict[vzdalenost] = posledniDict[vzdalenost]
            posledniDict[vzdalenost] = counter
        posledniHodnota = vzdalenost

#Vypis vysledku
for hodnota, posledniVyskytIndex in posledniDict.items():
    if posledniVyskytIndex == searchIndex:
        print("Pozice {0} je: {1}".format(posledniVyskytIndex, hodnota))
print("Total runtime: {0}".format(datetime.now()-start))