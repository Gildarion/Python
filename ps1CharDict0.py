from sys import *

parameters = len(argv)

if parameters == 2:
    myText = argv[1]
    print(myText)

else:    
    myText = "Four words for you"
    print(myText)
    print("If you want other text, you could use \n  - python ps1Char.py 'My own text'")

frequency = dict()

for character in myText:
    character = character.lower()
    if character in frequency:
    #if frequency.get(character) != None:
        frequency[character] += 1
    else:
        frequency[character] = 1
        
for letter in frequency.keys():
    print(letter, " - ", frequency[letter])
