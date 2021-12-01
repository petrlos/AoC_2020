#Advent of Code 2020 - Day 6

from Group import Group

textFile = open("data.txt", "r")

suma = 0
str = ""
data = []
persons = []

for textImport in textFile:
    textToInput = textImport[:-1]
    if textToInput != "":
        persons.append(textToInput)
    if textToInput == "":
        newGroup = Group(persons)
        data.append(newGroup)
        suma += newGroup.howMany
        persons = []
textFile.close()

print(suma)