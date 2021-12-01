#Advent of Code 2020 - Day 14, Verze 2
import re, datetime

start = datetime.datetime.now()

def decodeNewValueTask1(mask, mo):
    adress, value = mo[0], mo[1]
    valueBin = bin(value)[2:]
    valueBin = (len(mask) - len(valueBin)) * "0" + valueBin
    result = ""
    for x, y in zip(mask, valueBin):
        if x == "X":
            result += y
        else:
            result += x
    return [adress, int(result,2)]

def task1(lines):
    memory = {}
    for line in lines:
        if "mask" in line:
            mask = line[7:]
        if "mem" in line:
            mo = [int(x) for x in reNum.findall(line)]
            result = decodeNewValueTask1(mask, mo)
            if result[0] not in memory.keys():
                memory.setdefault(result[0], result[1])
            else:
                memory[result[0]] = result[1]
    return sum(memory.values())

def genSubMask(mask, adress):
    subMask = ""
    binAdress = bin(adress)[2:]
    binAdress = (len(mask)-len(binAdress)) * "0" + binAdress
    for x, y in zip(mask, binAdress):
        if x == "0":
            subMask += y
        else:
            subMask += x
    return subMask

def genNewAdresses(subMask):
    newAdresses = []
    subMask = list(subMask)
    counter = subMask.count("X")
    possibleMasks = 2** (counter)
    for i in range(0,possibleMasks):
        key = list((counter - len(bin(i)[2:]))* "0" + bin(i)[2:])
        keyIndex = 0
        newAdress = ""
        for char in subMask:
            if char == "X":
                newAdress += key[keyIndex]
                keyIndex += 1
            else:
                newAdress += char
        newAdresses.append(int(newAdress, 2))
    return newAdresses

def task2(lines):
    mask = ""
    memory = {}
    for line in lines:
        if "mask" in line:
            mask = line[7:]
        if "mem" in line:
            mo = [int(x) for x in reNum.findall(line)]
            subMask = genSubMask(mask, mo[0])
            newAdresses = genNewAdresses(subMask)
            for adress in newAdresses:
                if adress not in memory.keys():
                    memory.setdefault(adress, mo[1])
                else:
                    memory[adress] = mo[1]
    return sum(memory.values())

#MAIN
with open("data.txt", "r") as file:
    lines = file.read().splitlines()

reNum = re.compile(r"\d+")

print("Task1:", task1(lines))
print("Task2:", task2(lines))
print("Runtime:", datetime.datetime.now() - start)