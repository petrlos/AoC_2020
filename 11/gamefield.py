class HerniPole:

    def __init__(self, pole, sizeX, sizeY):
        self.pole = pole
        self.pocetSloupcu = sizeX
        self.pocetRadku = sizeY
        self.pocetZidli = 0
        self.stabilni = False

    def __str__(self):
        vypis = ""
        for radek in self.pole:
            for bunka in radek:
                vypis += bunka + " "
            vypis += "\n"
        return vypis

    def preindexujPole(self):
        #vytvor 2D pole se stejnymi parametry, jako puvodni pole
        newField = []
        for radek in self.pole:
            line = []
            for cell in radek:
                line.append(cell)
            newField.append(line)

        #projde vsechny prvky postupne a v pripade splneni podminky ho preklopi
        #pokud "L" nema souseda s "#", obsadi se
        #pokud "#" ma 4 a vice sousedu, uvolni se
        for radek in range(0,self.pocetRadku):
            for sloupec in range(0,self.pocetSloupcu):
                if newField[radek][sloupec] != ".":
                    sousedi = self.__countNeighbours(sloupec,radek)
                    if newField[radek][sloupec] == "L" and sousedi == 0:
                        newField[radek][sloupec] = "#"
                    elif newField[radek][sloupec] == "#" and sousedi > 4:
                        newField[radek][sloupec] = "L"

        #pokud preindexovane pole je shodne s puvodnim, pole je stabilni - spocitej zidle
        #jinak se self.pole premaze novy polem
        if newField == self.pole:
            self.__spocitejObsazeneZidle()
            self.stabilni = True
        else:
            self.pole = []
            for radek in newField:
                line = []
                for cell in radek:
                    line.append(cell)
                self.pole.append(line)

    # q = x, w = y
    def __countNeighbours(self,stred_x, stred_y):

        #metode se predaji souradnice stedu a ty se rozsiri o 1 vsemi smery
        #pokud by vysly mimo herni pole, nebudou se rozsirovat dannym smerem
        if stred_x == 0:
            leva = stred_x
        else:
            leva = stred_x - 1

        if stred_x == self.pocetSloupcu - 1:
            prava = stred_x
        else:
            prava = stred_x + 1

        if stred_y == 0:
            horni = stred_y
        else:
            horni = stred_y - 1

        if stred_y == self.pocetRadku - 1:
            dolni = stred_y
        else:
            dolni = stred_y + 1

        #spocita vsechny krizky
        counter = 0
        for i in range(horni, dolni + 1, 1):
            for j in range(leva, prava + 1, 1):
                if self.pole[i][j] == "#":
                    counter += 1
        return counter

    def __spocitejObsazeneZidle(self):
        pocet = 0
        for radek in self.pole:
            for cell in radek:
                if cell == "#":
                    pocet += 1
        self.pocetZidli = pocet