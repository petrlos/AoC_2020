## Advent of Code Day 16 - Train Ticket
from parametr import Field
from ticket import Ticket
textFile = open("test.txt", "r")

parametry, tickets = [], []
cisloRadku = 0

for textImport in textFile:
    cisloRadku += 1
    line = textImport
    # prvni tri radky jsou parametry
    if cisloRadku <= 3:
        newParametr = Field(line)
        parametry.append(newParametr)
    # 6. radek je vlastni ticket
    if cisloRadku == 6:
        ownTicket = Ticket(line)
    # 9. az 12. radek jsou "nearby tickets"
    if cisloRadku >= 9 and cisloRadku <= 11:
        ticket = Ticket(line)
        tickets.append(ticket)

error = 0

#Part1: postupne prochazi vsechny tickety a zkousi u jednotlivych hodnot, jestli je v nejakem z parametru
#pokud ne, vyradi cely ticket
for ticket in tickets:
    for hodnota in ticket.hodnoty:
        correctValue = False #predpokladam, ze spravny parametr neexistuje
        for parametr in parametry:
            # zkontroluj jestli je hodnota v parametru
            if parametr.checkParametr(hodnota):
                correctValue = True #pokud ho najde
        if not correctValue: #pokud ho nenasel
            error += hodnota
            ticket.correct = False
print(error)
