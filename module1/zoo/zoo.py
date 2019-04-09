import modScreen as screen
import presentation 
from data import *

def calculateTicket(age):
    ticket = {"price":0,"type":""}
    if age <= 2:
        ticket["type"] = "baby"
        ticket["price"] = 0
    elif age <= 12:
        ticket["type"] = "kid"
        ticket["price"] = 14
    elif age <= 65:
        ticket["type"] = "adult"
        ticket["price"] = 23
    else:
        ticket["type"] = "retired"
        ticket["price"] = 18
    return ticket
    
def inputTicket():
    age = presentation.askAge("Introduce the group member age: ")
    intTotalPrice = 0
    intTotalTicket = 0
    ticket = dict()
    
    while age != 0:
        ticket = calculateTicket(age)
        intTotalPrice += ticket["price"]
        intTotalTicket += 1
        
        totalTicket[ticket["type"]]["quantity"] += 1
        totalTicket[ticket["type"]]["price"] += ticket["price"] 
        presentation.posLine(ticket["type"],\
                totalTicket[ticket["type"]]["price"],\
                totalTicket[ticket["type"]]["quantity"])
        presentation.posLine("total", intTotalPrice, intTotalTicket)
        age = presentation.askAge("Introduce the group member age: ")

    return totalTicket

def writeReg(register):
    fInput = open("transactions.txt", "a+")
    fInput.write(register)
    fInput.close()

def prepReg(inputDict):
    register = ""
    for keyType, keyTotal in inputDict.items():
        register += "{},".format(keyTotal["quantity"])
    else:
        register = register.strip(',')
        register += "\n"
    return register
    
def main():
    presentation.outputScreen()
    tickets = inputTicket()
    writeReg(prepReg(tickets))
    screen.locateCursor(30,1)
    screen.pause()


main()
