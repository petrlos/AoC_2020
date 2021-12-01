class Rovnice:

    def __init__(self, line):
        self.popis = str(line)
        self.vysledek = 0
        self.vysledek2 = 0
    def __str__(self):
        return self.popis

    def spocitejRadek(self):
        i, levaZavorka = 0, 0
        while True:
            #najde tu nejvice vnitrni zavorku
            if self.popis[i] == "(":
                levaZavorka = i
            elif self.popis[i] == ")":
                pravaZavorka = i
                self.__spocitejPodretezec(levaZavorka, pravaZavorka)
                i = -1
            elif "(" not in self.popis:
                self.__spocitejPodretezec(0,len(self.popis)-1)
                i = -1
            if self.popis.count(" ") <= 1:
                break
            i += 1
        self.vysledek = int(self.popis)

    def __spocitejPodretezec(self, od, do):
        zpracuj = ""
        # najde podretezec, jehoz vysledek je potreba spocitat
        for i in range(od, do+1):
            zpracuj += self.popis[i]
        #zaloha - tato promenna bude nahrazena v celkovem retezci vysledkem, nemeni se
        zaloha = zpracuj
        # osekej z retezce zavorky
        zpracuj = zpracuj.replace("(", "")
        zpracuj = zpracuj.replace(")", "")
        # rozdel retezec podle mezer na pole a vypocitej jeho vysledek
        vysledek = self.__spocitejVysledekPart2(zpracuj.split(" "))
        self.popis = self.popis.replace(zaloha, str(vysledek))

    def __spocitejVysledekPart1(self,txt):
        #part 1: bez priority nasobeni/scitani - cisla se scitaji a nasobi tak jak jsou napsany za sebou
        #vezme i. cislo + i+1 operator + i+2. cislo a provede operaci, v dalsi iteraci skoci o dva,
        # tzn. na dalsi operator a cislo
        vysledek = int(txt[0])
        for i in range(0, len(txt)-2,2):
            druheCislo = int(txt[i+2])
            if txt[i+1] == "*":
                vysledek = vysledek * druheCislo
            if txt[i+1] == "+" in txt:
                vysledek = vysledek + druheCislo
        return vysledek

    def __spocitejVysledekPart2(self,txt):
        #SCITANI ma prioritu pred NASOBENIM, tzn. je potreba nejdrive provezt vsechna scitani a potom vsechna nasobeni
        i = 1
        while i < len(txt):
            #pokud je na pozici operatoru "+", secte predchozi a nasledjici cislo, operator a jedno cislo vymaze
            #a vysledek vlozi na misto v seznamu misto 2. cisla
            if txt[i] == "+":
                meziVysledek = int(txt[i-1]) + int(txt[i+1])
                txt.pop(i-1)
                txt.pop(i-1)
                txt[i-1] = meziVysledek
                #aby prosel vsechny operatory, je potreba se pri uspesnem souctu vratit o 2 cleny zpet
                #protoze seznam se o dva cleny zkratil, ale i zustalo stejne
                i = i - 2
            i = i + 2
        vysledek = int(txt[0])
        #postupne se pronasobi vsechna cisla od prvniho do posledniho
        for i in range(1,len(txt),2):
            vysledek = vysledek * int(txt[i+1])
        #vysledek se propise do retezce a dale se postupuje stejne jako v 1. casti
        return(vysledek)
