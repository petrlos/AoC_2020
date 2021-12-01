class Instrukce:

    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.visited = False

    def __str__(self):
        return "{0}: {1}".format(self.type, self.value)

    #pokud uz instrukci navstivil, navstavi na ni priznak visited - True
    def execute(self):
        self.visited = True

    #prejmenuje urcitou instrukci nop->jmp resp. obracene
    def rename(self):
        if self.type == "nop":
            self.type = "jmp"
        elif self.type == "jmp":
            self.type = "nop"

    def reset(self):
        self.visited = False