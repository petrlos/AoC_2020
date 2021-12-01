#Advent of Code 2020 - Day 4
from passport import PassId

textFile = open("scratch.txt", "r")

str = ""
pocet = 0

for textImport in textFile:
    textToInput = textImport[:-1]
    str += " " + textToInput
    if textToInput == "":
        newPassID = PassId(str)
        newPassID.validate()
        if newPassID.isValid:
            pocet += 1
        str = ""
textFile.close()

print("\nCelkovy pocet validnich pasu: {0}".format(pocet))
