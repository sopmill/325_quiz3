def printBackwards (userWord):
    return userWord[::-1]


userWord = input("Enter a word that will output backwards: ")
wordBackwards = printBackwards(userWord)

print(wordBackwards)