from module01 import *

listUnit = []
listPrice = []
index = 1
floatTotalCount = 0
floatTotalUnit = 0

strUnit = inputFloat("Product nº." + str(index) + " - Unit: ")
strPrice = inputFloat("Product nº." + str(index) + " - Price: ")
listPrice.append(float(changeComma(strPrice)))
listUnit.append(float(changeComma(strUnit)))

while not (strUnit == "0" or strPrice == "0"):
    index += 1
    strUnit = inputFloat("Product nº." + str(index) + " - Unit: ")
    listUnit.append(float(changeComma(strUnit)))
    if not (strUnit == "0"):
        strPrice = inputFloat("Product nº." + str(index) + " - Price: ")
        listPrice.append(float(changeComma(strPrice)))

if index == 1:
    print("\nNo data to print")

else:
    print("\n")
        
    try:
        for i in range(0, index - 1):
            floatPriceUnit = listUnit[i] * listPrice[i]
            floatTotalCount += floatPriceUnit
            floatTotalUnit += listUnit[i]
            # "{}€ - {} unidades - {}€".format(variables) 
            outResult = str(round(listUnit[i], 2)) + " units - "
            outResult += str(round(listPrice[i], 2)) + " € - "
            outResult += str(round(floatPriceUnit, 2)) + " €"
            print(outResult)

        print("================================================")
        outResult = "Quantity: " + str(round(floatTotalUnit, 2)) + " units " + "\n"
        outResult += "Total price: " + str(round(floatTotalCount,2)) + " €"
        print(outResult)

    except:
        print("ERROR - occurred when the program was running")

