class Ship:

    def __init__(self):
        self.direction = "E"
        self.x = 0
        self.y = 0

    def kolikUjela(self):
        vzdalenost = abs(self.x) + abs(self.y)
        return "Lod ujela celkem: {0}".format(vzdalenost)

    def __str__(self):
        return "Aktualni lokace: {0}:{1}".format(self.x, self.y)

    def provedInstrukci(self, instrukce):
        if ("L" in instrukce) or ("R" in instrukce):
            self.rotate(instrukce)
        else:
            self.plnouParouVpred(instrukce)

    def plnouParouVpred(self, kam):
        if "F" in kam:
            smerJizdy = self.direction
        else:
            smerJizdy = kam[0]
        oKolik = int(kam[1:])
        if smerJizdy == "N":
            self.x = self.x + oKolik
        if smerJizdy == "S":
            self.x = self.x - oKolik
        if smerJizdy == "E":
            self.y = self.y + oKolik
        if smerJizdy == "W":
            self.y = self.y - oKolik

    def rotate(self, kam):
        #pokud je smer otaceni doprava, nastavi se "kompas" vpravo, jinak vlevo
        #string se vynasobi petrkrat, abych nemusel resit "preteceni" indexu
        if kam[0] == "R":
            poradi = 5*"NESW"
        else:
            poradi = 5*"NWSE"
        krok = int(kam[1:])/90
        newDirectionIndex = int(int(poradi.find(self.direction)) + krok)
        self.direction = poradi[newDirectionIndex]


