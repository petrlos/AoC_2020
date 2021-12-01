## Advent of Code - Day19
import re
textFile = open("text2.txt", "r")

pravidla = ""
messages = []

#pokud radek obsahuje hvezdicku, jedna se o pravidlo, ulozi ho do retezce pravidel a ukonci strednikem
#pokud je to pouze text, jedna se o zpravu, ulozi ji do pole zprav
for textImport in textFile:
    textImport = textImport[:-1] #je potreba odstranit konec radku \n na konci kazdeho radku
    if ":" in textImport:
        pravidla += textImport + ";"
    if textImport.isalpha():
        messages.append(textImport)
textFile.close()

#vymaze z retezce pravidel posledni strednik, aby se vygeneroval slovnik
pravidla = pravidla[:-1]

#vytvori slovnik - dvojice klic + heslo je oddelena v puvodnim retezce dvojteckou, jednotlive dvojice
#v puvodnim retezci oddeleny strednikem
pravidlaDict = dict((x.strip(), y.strip())
            for x, y in (element.split(':')
            for element in pravidla.split(';')))

pokracovat = True

#mezera na zacatku a na konci cisla zamezi nahrazeni napr. pravidla 11 pravidlem 1 apod.
retezec = " 0 "

while pokracovat:

    for i in range(0,len(pravidlaDict)+100):
        #je potreba hledat pouze cisla, ktere maji z obou stran mezeru
        hledej = " " + str(i) + " "
        if str(i) in pravidlaDict:
            #nahrazeny retezec ze slovniku musi mit z obou stran mezeru
            retezec = retezec.replace(hledej, " ( "+pravidlaDict[str(i)]+" ) ")

    pokracovat = False
    #kontrola, jestli retezec obsahuje nejaka cisla - projde po znaku cely retezec, pokud najde cislo
    #spusti smycku znova
    for znak in retezec:
        if str(znak).isdigit():
            pokracovat = True

#vycisteni retezce - vymaze prebytecne mezery + vymaze uvozovky
retezec = retezec.replace(" ","")
retezec = retezec.replace("\"", "")

#porovnani retezce zpravy s vygenerovanym vzorem
pocet = 0
for message in messages:
    if re.fullmatch(retezec, message):
        pocet += 1
print(pocet)