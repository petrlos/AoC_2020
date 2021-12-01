class Linky:

    def __init__(self, seznam):
        self.autobusy = seznam.split(",")
        self.deltaT = []
        pocitadlo = 0
        for i in self.autobusy:
            if i != "x":
                self.deltaT.append(pocitadlo)
            pocitadlo += 1
        while "x" in self.autobusy:
            self.autobusy.remove("x")

    def __str__(self):
        vypis = ""
        for i in self.autobusy:
            vypis += i + ", "
        return vypis

    def nextDeparture(self, timeStamp):
        odjezdy, pouzeLinky = [],[]
        for autobus in self.autobusy:
            if autobus != "x":
                linka = int(autobus)
                pouzeLinky.append(linka)
                # spocitam predchozi odjezd
                pristiOdjezd = int(timeStamp / linka)
                # spocitam nasledujici odjezd
                pristiOdjezd = (pristiOdjezd + 1) * linka
                # za jak dlouho opravdu jede
                pristiOdjezd = pristiOdjezd - timeStamp
                odjezdy.append(pristiOdjezd)
        nextDepartureIn = min(odjezdy)
        nextLine = pouzeLinky[odjezdy.index(nextDepartureIn)]
        result = int(nextLine) * nextDepartureIn
        return result

    def postupnyOdjezd(self):
        start = 0
        krok = int(self.autobusy[0])
        for i in range(0,len(self.autobusy)-1):
            delta = int(self.deltaT[i+1])
            nasledujici = int(self.autobusy[i+1])
            while True:
                start = start + krok
                if ((start + delta) % nasledujici) == 0:
                    krok = krok * nasledujici
                    break
        return start

