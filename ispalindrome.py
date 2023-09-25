def ispalindrome (word):
    word = word.strip()
    if (word == word [::-1]):
        print (True)
    else:
        print (False)

word = input ('Enter a word')

ispalindrome (word)