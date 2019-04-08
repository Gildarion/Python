import ps1Screen as screen

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

    screen.locateCursor(1,1)

    while intError != 0:
        strAge = input(message)
        intError = validateIntPos(strAge) 
        if intError == -1:
            print("ERROR - Age must be positive interger")
        elif intError == -2:
            print("ERROR - Age must be a interger")
        else:
            intError = 0

    age = int(strAge)  
    return age

intTotal = 0
line = 4

screen.clearScreen()

age = askAge("Introduce the group member age: ")

while age != 0:
    intTicket = calculateTicket(age)
    intTotal += intTicket
    screen.locateCursor(line, 1)
    print("Ticket {}".format(intTicket))
    age = askAge("Introduce the group member age: ")
    line += 1

screen.locateCursor(line, 1)
print("Total: {}".format(intTotal))
