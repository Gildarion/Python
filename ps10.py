from validation import *

strBase = input ("Please insert the base of the triangle: ")
while not isDecimal(strBase):
    base = input ("ERROR!- Base is not a decimal.\n Insert a decimal number: ")

strHeight = input("Please insert the height of the triangle: ")
while not isDecimal(strHeight):
    strHeight = input("ERROR!- Height is not a decimal.\n Insert a decimal number:")

fltBase = float(changeComma(strBase))
fltHeight = float(changeComma(strHeight))

area = (fltBase * fltHeight) / 2


print("The area of the triangle is ", "{0:0.2f}".format(area))
