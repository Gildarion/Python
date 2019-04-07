#validate inputs
# proof
# 1 baby 0 
# 3 kids 14 42
# 2 adult 23 46
# 1 retired 18

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

def askAge(message):
    intError = -1

    while intError != 0:
        try:
            strAge = input(message)
            intAge = int(strAge)
            if intAge < 0:
                print("ERROR - Age must be positive interger")
            else:
                intError = 0
        except:
            print("ERROR - One error occurred when program was running")
    return intAge

intTotal = 0

age = askAge("Introduce the group member age: ")
# age > 0 only int
while age != 0:
    intTicket = calculateTicket(age)
    intTotal += intTicket
    age = askAge("Introduce the group member age: ")

print("Total: {}".format(intTotal))


#ask edad
#price / age


