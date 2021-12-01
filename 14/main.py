#Advent of Code - Day 14
from datetime import datetime
from pamet import Pamet

start = datetime.now()

textFile = open("data.txt", "r")

zapisyVPameti = []

for textImport in textFile:
    line = textImport
    if "mask" in line:
        #pokud radek obsahuje "mask", ulozi ji do retezce
        maska = ""
        i = line.find("=") + 2
        while line[i] != "\n":
            maska += line[i]
            i += 1
    if "mem" in line:
        #pokud radek obsahuje "mem", najde na radku adresu pameti a hodnotu a ulozi je do parametru
        adresa = ""
        i = line.find("[") + 1 #pocatecni znak adresy
        while line[i] != "]":
            adresa += line[i]
            i += 1
        adresa = int(adresa)

        hodnota = ""
        i = line.find("=") + 2 #pocatecni znak hodnoty k ulozeni
        while line[i] != "\n":
            hodnota += line[i]
            i += 1
        hodnota = int(hodnota)

        #vytvoreni instance tridy Pamet
        novyZapis = Pamet(adresa, hodnota)
        #prevedeni hodnoty
        novyZapis.prevedHodnotuPresMasku(maska)

        #projde vsechny zaznamy - pokud uz existuje zaznam, ktery ma stejnou adresu jako novy zaznam
        #dojde k jeho vymazani ze seznamu instanci
        for zapisy in zapisyVPameti:
            if zapisy.adresa == novyZapis.adresa:
                zapisyVPameti.remove(zapisy)

        #novy zaznam se pripoji do seznamu
        zapisyVPameti.append(novyZapis)

textFile.close()

suma = 0
for hodnoty in zapisyVPameti:
    suma += hodnoty.hodnota

print("Vysledek AoC Day14 Part1:", suma)
print("Runtime:",datetime.now() - start)