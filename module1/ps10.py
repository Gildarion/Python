from validation import *

def inputSide(message):
    strSide = input (message)
    while not isDecimal(strSide):
         strSide= input ("ERROR!- Base is not a decimal.\n Insert a decimal number: ")
    return strSide

strBase = inputSide("Please insert the base of the triangle: ")
strHeight = inputSide("Please insert the height of the triangle: ")

fltBase = float(changeComma(strBase))
fltHeight = float(changeComma(strHeight))

area = (fltBase * fltHeight) / 2


print("The area of the triangle is ", round(area,2))
