class Field:

    def __init__(self, line):
        self.line = line
        k = 0
        jmenoParametru, lr1, lr2, ur1, ur2 = "", "", "", "", ""
        lower, upper = [], []
        while line[k] != ":":
            jmenoParametru += line[k]
            k += 1
        k += 2 # vynechani dvojtecky a mezerey
        while line[k] != "-":
            lr1 += line[k]
            k += 1
        k += 1 #  vynechani mezery
        while line[k] != " ":
            lr2 += line[k]
            k += 1
        k += 4
        while line[k] != "-":
            ur1 += line[k]
            k += 1
        k += 1
        while line[k] != "\n":
            ur2 += line[k]
            k += 1
        self.jmeno = jmenoParametru

        lower.append(int(lr1))
        lower.append(int(ur1))
        self.lower = lower
        upper.append(int(lr2))
        upper.append(int(ur2))
        self.upper = upper

    def __str__(self):
        return self.line

    def checkParametr(self, hodnota):
        error = False
        for i in range(0,2):
            if hodnota in range(self.lower[i],self.upper[i]+1):
                    error = True
        return error

