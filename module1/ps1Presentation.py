import ps1Screen as screen

posTicket = {
        "baby":5,
        "kid":6,
        "adult":7,
        "retired":8,
		"total":10
        }

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

def posLine(typeMember, totalTicket = 0, quantity = 0):
    screen.printMsg("{0:02d}".format(quantity), posTicket[typeMember], 26)
    screen.printMsg("{0:.2f} €".format(totalTicket), posTicket[typeMember], 31)
    screen.clearLine(1)
	
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
	