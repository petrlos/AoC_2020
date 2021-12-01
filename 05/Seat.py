class Seat:

    def __init__(self, code):
        self.code = code[:-1]
        self.row = 0
        self.column = 0
        self.id = 0

    def __str__(self):
        return "Sedadlo s kodem {0} ma ID {1}".format(self.code, self.id)

    def getId(self):
        lower = 0
        upper = 127
        for i in range(0,7,1):
            mid = lower + int((upper - lower) / 2) + 1
            if self.code[i] == "B":
                lower = mid
            else:
                upper = mid - 1
        self.row = lower

        lower = 0
        upper = 7
        for i in range(7,10,1):
            mid = lower + int((upper - lower) / 2) + 1
            if self.code[i] == "R":
                lower = mid
            else:
                upper = mid - 1
        self.column = lower

        self.id = self.row * 8 + self.column