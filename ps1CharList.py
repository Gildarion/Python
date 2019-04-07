from sys import *

def existChar(character, listChar):
    index = 0
    while index < len(listChar):
        if listChar[index] == character:
            return index
        index += 1

    return None

parameters = len(argv)

if parameters == 2:
    myText = argv[1]
    print(myText)

else:    
    myText = "Four words for you"
    print(myText)
    print("If you want other text, you could use \n  - python ps1Char.py 'My own text'")

letter = []
frequency = []

for character in myText:

    position = existChar((character).lower(), letter)

    if position != None:
        frequency[position] += 1

    else:
        letter.append((character).lower())
        frequency.append(1)

print(letter)
print(frequency)
