def printBackwards (userWord):
    return userWord[::-1]


userWord = input("Yo yo, enter a word that will output: ")
wordBackwards = printBackwards(userWord)

print(wordBackwards + ";)")