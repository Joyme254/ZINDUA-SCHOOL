#with open ('words.txt', 'r') as file:
  #  for line in file:
        #print (line)

# how to open a file
# with open ('name odf the file' , 'r') r is read mode, w is write mode
# for line in file
    # print (line)


# how to create  a file
# with open ( text.text, 'w') as textfile:
    #   textfile.writelines(lines)

with open ('words.txt', 'r') as file:
        
        for words in file:
            word = word.strip()
            if (word == word [::-1]):
                with open ('palindromes.txt', 'w') as textfile:
                 textfile.writelines(words)

#line 15 means or can be also written as:
# file = open ('words.txt', 'r')
# for line in file:
        # print (line)

# line 20 can be rewtitten as:
# textfile = open ('palindromes.txt', 'w')

                     