#Advent of Code Day 21: Alergens + Ingredients

from pprint import pprint

with open("data.txt", "r") as file:
    lines = file.read().replace(" (contains ",":").replace(")","").splitlines()

ingredients = []
allergensDict = {}
for line in lines:
    data = line.split(":")
    allergens = data[-1].split(", ")
    newIngredients = data[0].split(" ")
    ingredients += newIngredients
    for allergen in allergens:
        if allergen in allergensDict.keys():
            possibleAllergens = set(allergensDict[allergen]).intersection(set(newIngredients))
            allergensDict[allergen] = possibleAllergens
        else:
            allergensDict.setdefault(allergen, newIngredients)

mayBeAllergen = []
for value in allergensDict.values():
    mayBeAllergen += value

result = [item for item in ingredients if item not in mayBeAllergen]

print("Task 1:", len(result))

print("Task 2: vpzxk,bkgmcsx,qfzv,tjtgbf,rjdqt,hbnf,jspkl,hdcj")
print("Task 2 vyresen na papire postupnou redukci moznych alergenu")
print(" ")

done = False
while not done:
    done = True
    for values in allergensDict.values():
        if len(values) > 1:
            done = False
        else:
            for key in allergensDict.keys():
                if len(allergensDict[key]) > 1:
                    allergensDict[key] = allergensDict[key] - values

pprint(allergensDict)