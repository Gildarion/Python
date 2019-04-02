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
