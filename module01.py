def changeComma(string):
    
    result = string.replace(",",".")
    return result

def isDecimal(strInput):

    strInput = changeComma(strInput)

    try:
        float(strInput)
        return True
    except:
        return False

def inputFloat(message):
    strInput = input (message)
    while not isDecimal(strInput):
         strInput = input ("ERROR!- It is not a decimal.\n Insert a decimal number: ")
    return strInput