class Ticket:

    def __init__(self, line):
        self.line = line
        hodnoty, hodnota, k = [], "", 0
        for k in range(0,len(line)):
            if line[k] == "," or line[k] == "\n":
                hodnoty.append(int(hodnota))
                hodnota = ""
            elif line[k] != ",":
                hodnota += line[k]
        self.hodnoty = hodnoty
        self.correct = True

    def __str__(self):
        return self.line