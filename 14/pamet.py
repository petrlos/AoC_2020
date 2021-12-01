class Pamet:

    def __init__(self, adresa, hodnota):
        self.adresa = adresa
        self.hodnota = hodnota

    def __str__(self):
        return "{0}: {1}".format(self.adresa, self.hodnota)

    # prevod dec --> bin: vrati retezec: "{0:b}".format(x)
    # prevod bin --> dec: z retezce: int(y, 2) vraci cislo
    def prevedHodnotuPresMasku(self, maska):
        binarni = "{0:b}".format(self.hodnota)
        binarni = (36-len(binarni))*"0" + binarni
        novaHodnota = ""
        for i in range(0,36):
            if maska[i] == "X":
                novaHodnota += binarni[i]
            elif maska[i] == "0":
                novaHodnota += "0"
            elif maska[i] == "1":
                novaHodnota += "1"
        self.hodnota = int(novaHodnota, 2)


