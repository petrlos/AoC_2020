#Advent of Code 2é20: Day 7

def parse_data(lines):
    bags = {}
    for line in lines:
        key, content = line.split(" contain ")
        key = " ".join(key.split(" ")[0:2]) #ignore word bag/bags
        if "other" in content:
            bags[key] = [] #if no bags, add empty list to prevent key error
        else:
            single_bags = content.split(", ")
            values = []
            for single_bag in single_bags:
                words = single_bag.split(" ")
                #format: tuple(count, colour) without word bag/bags
                values.append((int(words[0]), " ".join(words[1:3])))
            bags[key] = values
    return bags

def count_bags(bags, type):
    total_bags = 0
    for quantity, inner_bag in bags[type]:
        total_bags += quantity + quantity * count_bags(bags, inner_bag)
    return total_bags

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

bags = parse_data(lines)

print("Task 2:", count_bags(bags, "shiny gold"))