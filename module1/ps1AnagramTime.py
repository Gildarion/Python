import timeit
import sys

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


if isAnagram(str(sys.argv[1]),str(sys.argv[2])):
    print("These words are anagrams")
else:
    print("These words are not anagrams")


function = "'isAnagram(" + str(sys.argv[1]) + "," + str(sys.argv[2]) + ")'"

t = timeit.Timer(function,"from __main__ import isAnagram")
timeAnagram = t.timeit()

print("time: {}".format(timeAnagram))

