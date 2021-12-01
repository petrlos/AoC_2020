import string

class Group:

    def __init__(self, persons):
        #self.lst - seznam znaku abecedy od a do z
        self.lst = list(string.ascii_lowercase)
        self.persons = persons
        self.howMany = 0

        #postupne prochazi osoby v jednotlive skupine a pokud u osoby nenajde znak, nahradi ho #
        for osoby in self.persons:
            for znak in self.lst:
                if znak not in osoby:
                    toBeDeleted = self.lst.index(znak)
                    self.lst[toBeDeleted] = "#"

        #celkovy pocet znaku, ktere obsahuji vsechny osoby je pocet ne-krizku
        self.howMany = 26 - self.lst.count("#")

    def __str__(self):
        return str(self.persons)

'''    def getAnswers(self):
        seznam = self.lst
        for osoby in self.persons:
            for i in range(0,len(seznam),1):
                if seznam[i] is not in osoby:
                    seznam.pop(i)
        return len(seznam)
'''
