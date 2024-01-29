def printBackwards (userWord):
    return userWord[::-1]


userWord = input("Enter a word: ")
wordBackwards = printBackwards(userWord)

print(wordBackwards)