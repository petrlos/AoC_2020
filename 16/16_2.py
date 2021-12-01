#Advent of Code 2020 Day 16
import re, datetime

def isValid(ticket):
    valid = True
    for value in ticket:
        if value not in possibleValues:
            valid = False
            task1.append(value)
    return valid

regNum = re.compile(r"\d+")
regWord = re.compile(r"\w+:")

with open("data.txt", "r") as file:
    lines = file.read().splitlines()

#save values from input
parameters = {}
nearbyTicketBool = False
nearbyTickets = []
for index,line in enumerate(lines):
    if "or" in line:
        param = regWord.search(line).group()
        numbers = [int(x) for x in regNum.findall(line)]
        values = list(range(numbers[0], numbers[1]+1)) + list(range(numbers[2], numbers[3]+1))
        parameters.setdefault(param, values)
    if len(line.split(",")) > 1 and "your" in lines[index-1]:
        ownTicket = [int(x) for x in line.split(",")]
    if "nearby" in line:
        nearbyTicketBool = True
    if nearbyTicketBool and line[0].isnumeric():
        nearbyTickets.append([int(x) for x in line.split(",")])

#Task1
possibleValues = []
for values in parameters.values():
    possibleValues += values
validTickets = []
task1 = [] ##hodnoty do tohoto seznamu se ukladaji ve funkci isValid, pokud ticket neni platny
for ticket in nearbyTickets:
    if isValid(ticket):
        validTickets.append(ticket)
print("Task 1:",sum(task1))

#Task2
keysRemaining = {} #overuje, ktere param jsou jeste volne (true) resp. obsazene (false)
for key in parameters.keys(): #na zacatku jsou volne vsechny
    keysRemaining.setdefault(key, True)
#je potreba prochazet hodnoty po sloupcich, proto je vyhodnejsi matici otocit o 90st a prochazet
#otocenou matici po radcich
ticketsRotated = list(zip(*validTickets[::-1]))

#vysledky ve formatu parametr: index odpovidajici indexu v ownticket resp. tickets
results = {}

while True:
    #vezmi i. radek (resp. sloupec v neotocene matici)
    for index, values in enumerate(ticketsRotated):
        possibleKeys = {}
        #pomocny dict - pokud uz najde nejaky parametr, nova otocka While True
        #bude overovat jenom volne parametry
        for key in keysRemaining.keys():
            if keysRemaining[key]:
                possibleKeys.setdefault(key, True)
        #projde jednotlive hodnoty
        for value in values:
            #a projde jednotlive parametry
            for key in possibleKeys.keys():
                #pokud parametr ma jeste hodnotu True, ale hodnotu nabit nemuze, nastavi hodnotu false
                if possibleKeys[key] == True:
                    if value not in parameters[key]:
                        possibleKeys[key] = False
        #pokud nasel takovou kombinaci, ze prave jeden parametr z possibleKeys == True: vyradi tento
        #parametr z keysRemaining + zapise do results parametr + jeho index (viz Line59 a enumerate)
        if len(list(filter(lambda x: x, possibleKeys.values()))) == 1:
            for key in possibleKeys:
                if possibleKeys[key] == True:
                    keysRemaining[key] = False
                    results.setdefault(key, index)
    #opakuj while dokud nema 20 vysledku
    if len(results.keys()) == 20:
        break

task2 = 1
#projde vysledky v results, pokud key obsahuje "depart", vynasobi vysledek odpovidajici hodnotou
#dle indexu v ownTicket
for result in results.keys():
    if "depart" in result:
        task2 *= ownTicket[results[result]]

print("Task 2:",task2)