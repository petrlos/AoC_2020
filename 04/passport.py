class PassId:

    def __init__(self, popis):
        self.isValid = True
        lst = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
        self.popis = popis
        self.hodnota = []

        #do seznamu "hodnota" se v v poradi v seznamu "lst" ulozi odpovidajici
        #hodnoty parametru
        for parametr in lst:
            output = ""
            zacatek = self.popis.find(parametr) + 4
            while self.popis[zacatek] != " ":
                output += self.popis[zacatek]
                zacatek += 1
            self.hodnota.append(output)

    def validate(self):
        #0 overeni parametru byr - 1920-2002
        if not self.checkYear(self.hodnota[0], 1920, 2002):
            self.isValid = False
        #1 overeni parametru iyr - 2010-2020
        if not self.checkYear(self.hodnota[1], 2010, 2020):
            self.isValid = False
        #2 overeni parametru eyr - 2020-2030
        if not self.checkYear(self.hodnota[2], 2020, 2030):
            self.isValid = False
        #3 vereni parametru hgt: 150-193cm, 59-76in
        if not self.checkHGT(self.hodnota[3]):
            self.isValid = False
        #4 overeni parametru hcl: # followed by exactly six characters 0-9 or a-f
        if not self.checkHCL(self.hodnota[4]):
            self.isValid = False
        #5 overeni parametru ecl: musi obsahovat: amb, blu, brn, gry, grn, hzl, oth
        if not self.checkECL(self.hodnota[5]):
            self.isValid = False
        #6 overeni parametru pid: a nine-digit number, including leading zeroes.
        if not self.checkPID(self.hodnota[6]):
            self.isValid = False

    def checkYear(self, parametr, lower, upper):
        if len(parametr) == 4 and parametr.isdigit():
            if int(parametr) >= lower and int(parametr) <= upper:
                return True
        else:
            return False

    def checkHGT(self, parametr):
        fail = False
        if "in" in parametr:
            vyska = parametr[:-2]
            if vyska.isdigit():
                if int(vyska) >= 59 and int(vyska) <= 76:
                    fail = True
        if "cm" in parametr:
            vyska = parametr[:-2]
            if vyska.isdigit():
                if int(vyska) >= 150 and int(vyska) <= 193:
                    fail = True
        return fail

    def checkHCL(self, parametr):
        fail = False
        if parametr[0] == "#":
            fail = True
            parametr = parametr[1:]
        lst = ("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f")
        for check in parametr:
            if check not in lst:
                fail = False
        if len(parametr) != 6:
            fail = False
        return fail

    def checkECL(self, parametr):
        fail = False
        lst = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        for check in lst:
            if check == parametr:
                fail = True
        return fail

    def checkPID(self, parametr):
        fail = True
        if (len(parametr) != 9) or (not parametr.isdigit()):
            fail = False
        return fail

    def __str__(self):
        validni = "neni validni"
        if self.isValid:
            validni = "je validni"
        return "Pas s daty{0} {1}".format(self.popis, validni)