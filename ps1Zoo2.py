import ps1Screen as screen

dicTicket = {
        "baby":{
            "price":0,
            "quantity":0
            },
        "kid":{
            "price":0,
            "quantity":0
            },
        "adult":{
            "price":0,
            "quantity":0
            },
        "retired":{
            "price":0,
            "quantity":0
            }
        }
posTicket = {
        "baby":5,
        "kid":6,
        "adult":7,
        "retired":8
        }

def calculateTicket(age):
    if age <= 2:
        price =  0
    elif age <= 12:
        price = 14
    elif age <= 65:
        price = 23
    else:
        price = 18
    return price

def validateIntPos(cadena):
    try:
       n = int(cadena)
       if n >= 0:
           result = 0
       else:
           result = -1
    except:
        result = -2
    return result

def askAge(message):
    intError = -1
    while intError != 0:
        strAge = screen.inputMsg(message, 1, 1)
        intError = validateIntPos(strAge) 
        if intError == -1:
           screen.printError("Age must be positive interger")
        elif intError == -2:
           screen.printError("Age must be a interger")
        else:
            intError = 0
    age = int(strAge) 
    screen.clearLine(25)
    return age

def outputScreen():
    screen.clearScreen()
    screen.reset()
    screen.printMsg("Baby    tickets....: 00 - ", 5, 5)
    screen.printMsg("Kid     tickets....: 00 - ", 6, 5)
    screen.printMsg("Adult   tickets....: 00 - ", 7, 5)
    screen.printMsg("Retired tickets....: 00 - ", 8, 5)
    screen.formatMsg(1, 40, 37)
    screen.printMsg("Total......: ", 10, 13)
    screen.reset()
    
def typeTicket(price):
    if price == 0:
        return "baby"
    elif price == 14:
        return "kid"
    elif price == 23:
        return "adult"
    else:
        return "retired"

def posLine(column, totalTicket = 0, quantity = 0):
    screen.printMsg("{0:02d}".format(quantity), column, 26)
    screen.printMsg("{0:.2f} €".format(totalTicket), column, 31)
    screen.clearLine(1)

def main():
    age = askAge("Introduce the group member age: ")
    intTotalPrice = 0
    intTotalTicket = 0
    while age != 0:
        intTicket = calculateTicket(age)
        intTotalPrice += intTicket
        intTotalTicket += 1
        member = typeTicket(intTicket)
        dicTicket[member]["quantity"] += 1
        dicTicket[member]["price"] += intTicket 
        posLine(posTicket[member],\
                dicTicket[member]["price"],\
                dicTicket[member]["quantity"])
        posLine(10, intTotalPrice, intTotalTicket)
        age = askAge("Introduce the group member age: ")

outputScreen()
main()
screen.locateCursor(30,1)
screen.pause()
