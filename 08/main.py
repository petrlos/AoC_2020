from instrukce import Instrukce
#nop: nedela nic, prejde na dalsi instrukci
#acc: zvysuje hodnotu v akumulatoru, prejde na dalsi instrukci
#jmp: skoci na instrukci v offsetu viz parametr

textFile = open("data.txt", "r")

change = -1
i = 0

#seznam instanci Instrukce
data = []

for textImport in textFile:
    textToInput = textImport[:-1]
    type = textToInput[0:3]
    value = int(textToInput[4:len(textToInput)])
    input = Instrukce(type, value)
    data.append(input)
textFile.close()

#nakonec seznamu pridam instrukci "end"
data.append(Instrukce("end", 0))

while data[i].type != "end":
    change += 1
    acc = 0
    i = 0
    if data[change].type != "acc":
        #postupne zkousi zmenit instrukci na urcite pozici a projet
        data[change].rename()
        for instrukce in data:
            instrukce.reset()

        while data[i].visited == False:
            data[i].execute()
            if data[i].type == "nop":
                i = i + 1
            elif data[i].type == "acc":
                acc = acc + data[i].value
                i = i + 1
            elif data[i].type == "jmp":
                i = i + data[i].value
            elif data[i].type == "end":
                print("Konecna hodnota akumulatoru po dojeti do konce: {0}".format(acc))
        data[change].rename()