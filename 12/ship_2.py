class Ship2:

    def __init__(self):
        self.location = [0,0] #pocatecni startovni pozice lodi
        self.waypoint = [10,1] #pocatecni startovni pozice waypointu
        self.vektor = [0,0]
        self.zprava = ""

    def __str__(self):
        vypis = "Umisteni lodi: {0}".format(self.location) + "\n"
        vypis += "Umisteni waypointu: {0}".format(self.waypoint)
        return vypis

    def kolikUjela(self):
        vzdalenost = abs(self.location[0]) + abs(self.location[1])
        return "Lod ujela celkem: {0}".format(vzdalenost)

    def provedInstrukci(self, instrukce):
        if "F" in instrukce:
            self.__posunLod(instrukce)
        elif "R" in instrukce or "L" in instrukce:
            self.__otocWaypoint(instrukce)
        elif True:
            self.__presunWaypoint(instrukce)
        self.nastavZpravu(self.__str__())

    #odecte od sebe odpovidajici souradnice waypointu a lode a spocita tim vektor trasy
    def spocitejVektor(self):
        for i in range(0,2):
            self.vektor[i] = self.waypoint[i] - self.location[i]

    def __posunLod(self, kam):
        #kolik jednotek je potreba posunout
        pocetPosunu = int(kam[1:])
        #jakym smerem
        self.spocitejVektor()
        #posun:
        for i in range(0,2):
            self.waypoint[i] += pocetPosunu * self.vektor[i]
            self.location[i] += pocetPosunu * self.vektor[i]

    def __otocWaypoint(self, kam):
        #je potreba urcit smer otaceni, kolik kroku a vektor
        self.spocitejVektor()
        smer = kam[0]
        oKolik = int(kam[1:])
        kolikrat = int(oKolik / 90)

        #pokud je smer otaceni doleva, je to stejne jako 4-x krat otoceni doprava
        if smer == "L":
            kolikrat = 4 - kolikrat

        #rotace vektoru: x = y, y = -x
        for i in range(0,kolikrat):
            temp = -1 * self.vektor[0]
            self.vektor[0] = self.vektor[1]
            self.vektor[1] = temp

        #korekce waypointu o vektor:
        for i in range(0,2):
            self.waypoint[i] = self.location[i] + self.vektor[i]

    def nastavZpravu(self, zprava):
        self.zprava = zprava

    def vratZpravu(self):
        return self.zprava

    def __presunWaypoint(self, kam):
        smerPosunu = kam[0]
        oKolik = int(kam[1:])
        if smerPosunu == "N":
            self.waypoint[1] += oKolik
        if smerPosunu == "S":
            self.waypoint[1] -= oKolik
        if smerPosunu == "E":
            self.waypoint[0] += oKolik
        if smerPosunu == "W":
            self.waypoint[0] -= oKolik
