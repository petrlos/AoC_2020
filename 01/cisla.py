class Cisla:

    def __init__(self, cisla):
        self.cisla = cisla

    def najdiDvojice(self):
        for i in self.cisla:
            for j in self.cisla:
                    suma = i + j
                    if (suma == 2020):
                        return i * j

    def najdiTrojice(self):
        for i in self.cisla:
            for j in self.cisla:
                for k in self.cisla:
                    suma = i + j + k
                    if (suma == 2020):
                        return i * j * k
