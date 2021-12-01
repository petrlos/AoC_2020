#funkce, ktera vrati seznam sum dvojic mezi indexy: index a index-sifra
def findSumOfPairs(begin, end):
    toBePaired = []
    pairs = []
    #ze seznamu data si vyberu cisla v intervalu begin/end, ktre budu parovat
    for i in range(end, begin, 1):
        toBePaired.append(data[i])
    #dva vnorene cykly - secte i. clen s j. a pokud i neni rovno j a hodnota neni v seznamu, ulozi ji
    for i in range(0,sifra,1):
        for j in range(0,sifra,1):
            newNumber = toBePaired[i] + toBePaired[j]
            if (i != j) and (newNumber not in pairs):
                pairs.append(newNumber)
    return pairs

# zacatek MAIN
sifra = 25

if sifra == 5:
    FileToOpen = "test2.txt"
else:
    FileToOpen = "data.txt"

textFile = open(FileToOpen, "r")

data = []

for textImport in textFile:
    textToInput = textImport
    data.append(int(textToInput))
textFile.close()

index = sifra - 1 # sifra zavadeci sekvence, -1 protoze seznam zacina 0. prvkem

while True:
    index += 1
    sumaDvojic = findSumOfPairs(index, index-sifra)
    if data[index] not in sumaDvojic:
        break

failedNumber = data[index]

print("prvni cislo, ktere neodpovida sifre je {0} a je na pozici {1} ".format(failedNumber,index))

lowerIndex = 0
higherIndex = 0

#proved soucet od i. clena po konec
for i in range(0,len(data),1):
    for j in range(i,len(data)-i,1):
        suma = sum(data[i:j+1])
        if suma == failedNumber:
            lowerIndex = i
            higherIndex = j
            break
        if suma > failedNumber:
            break


newList = []
print("Index zacatku a konce souvisleho intervalu:",lowerIndex, higherIndex)
for i in range(lowerIndex,higherIndex+1,1):
    newList.append(data[i])
print("Hodnoty v intervalu: ",newList)
print("minimum: {0}, maximum: {1}".format(min(newList),max(newList)))
print("suma:",max(newList)+min(newList))

