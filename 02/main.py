#Advent of Code 2020 - Day 1

## nacti data ze souboru
f = open("scratch.txt", "r")
data = []
for x in f:
    data.append((x))
f.close()

pocetPlatnychHesel = 0

## prevedeni radku z txt na instance tridy Heslo
for i in data: ## nacte i.-ty radek ze vstupu
    radek = str(i)
    vystup = []
    readOut = ""

    #nacita postupne znaky z radku, kdyz narazi na pomlcku/mezeru, prida cislo jako paramatr do seznamu vystup
    for x in radek:
        readOut += x
        if x == "-":
           readOut = readOut[:-1]
           vystup.append(int(readOut))
           readOut = ""
        if x == " ":
            vystup.append(int(readOut))
            readOut = ""
            break

    #najde na radku dvojtecku a jako overovaci znak ulozi pozici o 1 vlevo
    dvojtecka = radek.find(":")
    znak = radek[dvojtecka-1]

    #vymazani vstupnich promennych
    valid1 = False
    valid2 = False

    #jestlize znak na pozici dvojtecka + vstup + 1 = znak
    if znak == radek[dvojtecka+vystup[0]+1]:
        valid1 = True
    if znak == radek[dvojtecka+vystup[1]+1]:
        valid2 = True
    # ^ je XOR -> musi platit prave jedna z moznosti, pokud neplati zadna nebo obe, vraci false
    if valid1 ^ valid2:
        pocetPlatnychHesel += 1


print("Pocet platnych hesel: {0}".format(pocetPlatnychHesel))