class Radek:

    def __init__(self, line, poradi):
        line = line[:-1]  #je potreba useknout posledni znak - "\n"
        self.line = line
        self.length = len(line) #ulozi se delka radku
        self.poradi = poradi

    def __str__(self):
        return "{2}. Radek: {0}, delka: {1}".format(self.line, self.length, self.poradi)

    #pokud je na lokaci strom, vrati true, jinak false
    def isTree(self, location):
        if self.line[location] == "#":
            return True
        else:
            return False