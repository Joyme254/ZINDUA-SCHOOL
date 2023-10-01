#Write a python program that reads the words.txt file and prints out all the palindromes in the file to a palindromes.txt file



with open ('words.txt', 'r') as file:
        
    for words in file:
     words = words.strip()
     if (words == words [::-1]):
        with open ('palindromes.txt', 'w') as pal:
         pal.writelines(words)
                



# or as a function

def ispalindrome ( fromFile, toFile):
  with open (fromFile, 'r') as file:
    for words in file:
      if (words == words [::-1]):
        with open (toFile, 'w') as pal:
          pal.writelines(words)

ispalindrome ('words.txt', 'palindromes.txt')



