from collections import defaultdict

class Adapters:

    def __init__(self, adapters):
        self.adapters = adapters

    def part1(self):
        joltage = 0
        differenceOne = 0
        differenceThree = 0

        for adapter in self.adapters:
            if adapter - joltage == 1:
                differenceOne += 1
                joltage += 1
            if adapter - joltage == 3:
                differenceThree += 1
                joltage += 3
        return differenceOne * differenceThree

    def part2(self):
        paths = defaultdict(int)
        paths[0] = 1
        for item in self.adapters:
            paths[item] = paths[item - 1] + paths[item - 2] + paths[item - 3]

        return paths[self.adapters[-1]]