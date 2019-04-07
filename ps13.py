def fahToCel(g):
    return (g - 32) * 5/9

def celToFah(g):
    return g * (9/5) + 32
    
def celsius(minDegree, maxDegree):
    for degree in range(minDegree, maxDegree + 10, 10):
        print("{0}ºF -> {1:0.2f}ºC".format(degree, fahToCel(degree)))
        
def fahrenheit(minDegree, maxDegree):
    for degree in range(minDegree, maxDegree + 10, 10):
        print("{0}ºC -> {1:0.2f}ºF".format(degree, celToFah(degree)))

typeDegree = ""

while not (typeDegree == "C" or typeDegree == "F"):
    typeDegree = (input("What kind of temperature do you want? (C/F)\n")).upper()
    
    if typeDegree == "C":
        celsius(0, 230)

    elif typeDegree == "F":
        fahrenheit(0, 100)

    else:
        print("Your input is not correct.")
        print("Please try again. \n")
    
