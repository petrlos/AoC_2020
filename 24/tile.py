class Tile:

    def __init__(self, line):
        self.line = line
        self.x = 0
        self.y = 0
        self.status = "black"

        self.__getCoordinates()

    def __str__(self):
        return "Dilek na souradnicich {0}, {1} ma status: {2}".format(self.x, self.y, self.status)

    def flip(self):
        if self.status == "white":
            self.status = "black"
        else:
            self.status = "white"

    def __getCoordinates(self):
        x, y, i = 0, 0, 0
        #postupne prochazi po znaku na radku a dekoduje smer a upravuje souradnice od vychoziho bodu
        #vysledek nastavi jako self.x resp self.y
        while self.line[i] != "\n":
            if self.line[i] == "e" or self.line[i] == "w":
                smer = self.line[i]
            else:
                #pokud je smer slozeny ze dvou znaku (neni to east nebo west), vezme dva znaky + poskoci o dva znaky
                smer = self.line[i] + self.line[i+1]
                i += 1
            if smer == "e":
                x = x + 1
            elif smer == "w":
                x = x - 1
            elif smer == "nw":
                x = x - 1
                y = y + 1
            elif smer == "ne":
                y = y + 1
            elif smer == "sw":
                y = y - 1
            elif smer == "se":
                x = x + 1
                y = y - 1
            i += 1
        self.x = x
        self.y = y