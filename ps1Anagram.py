def isAnagram(word1, word2):
    longWord1 = len(word1)
    longWord2 = len(word2)

    if longWord1 != longWord2:
        return False
    for character2 in word2:
        for character1 in word1:
            if character1 == character2:
               word1 = list(word1)
               word1.remove(character1)
               longWord2 -= 1
               break
        if longWord2 != len(word1):
            break
                    
 
    if longWord2 == 0:    
    	return True
    else:
        return False

def inputWord(message):
    while True:
        word = input(message)
        if word.isalpha():
            break
        else:
            print("ERROR - You must introduce a word")
    return word

strWord1 = inputWord("Introduce the first word: ")
strWord2 = inputWord("Introduce the second word: ")


if isAnagram((strWord1).lower(), (strWord2).lower()) == False:
    print("These words are not anagrams \n")
else:
    print(strWord1 + " and ", strWord2, " are anagrams \n")
