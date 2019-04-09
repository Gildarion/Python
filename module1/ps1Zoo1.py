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
    while intError != 0:
        screen.locateCursor(1,1)
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

def outputScreen():
    screen.locateCursor(4,1)
    #len of this 17
    print("Baby tickets...: ")
    print("Kid tickets:...: ")
    print("Adult tickets:.: ")
    print("Retired tickets: ")

def posLine(price):
    if price == 0:
        return 4
    elif price == 14:
        return 5
    elif price == 23:
        return 6
    else:
        return 7

screen.clearScreen()
outputScreen()

age = askAge("Introduce the group member age: ")
intTotal = 0
line = 4

while age != 0:
    intTicket = calculateTicket(age)
    line = posLine(intTicket)
    intTotal += intTicket

    screen.locateCursor(line, 18)
    print("{}".format(intTicket))
    age = askAge("Introduce the group member age: ")

screen.locateCursor(9, 1)
print("Total: {}".format(intTotal))
