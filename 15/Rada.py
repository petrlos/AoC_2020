class Rada:

    def __init__(self, rada, count):
        self.rada = rada
        self.zacatek = self.rada * 1
        self.count = count

        self.__getResult(count)

    def __str__(self):
        return "Pozice {0} v rade {1} je: {2}".format(self.count, self.zacatek, self.rada[-1])

    def __najdiPosledniDvePozice(self, cislo):
        temporary = self.rada * 1
        pozice1 = len(self.rada) - temporary[::-1].index(cislo) - 1
        temporary.pop(pozice1)
        pozice2 = len(temporary) - temporary[::-1].index(cislo) - 1
        return pozice1 - pozice2

    def __getResult(self, count):
        i = len(self.rada) - 1
        while len(self.rada) < count:
            if self.rada.count(self.rada[i]) <= 1:
                newNumber = 0
            else:
                newNumber = self.__najdiPosledniDvePozice(self.rada[i])
            self.rada.append(newNumber)
            i += 1
