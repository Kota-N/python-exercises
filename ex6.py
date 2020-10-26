# Exercises from http://www.practicepython.org/

#6 String Lists

import math

word = input("Enter a word: ")

middleIndex = math.floor(len(word)/2)
firstHalf = word[0:middleIndex]
lastHalf = word[middleIndex+1:]

if firstHalf[::-1] == lastHalf:
    print(word, ": Your word is palindrome!")
else:
    print(word, ": Your word isn't palindrome...")