import re

#pattern = re.compile ('^Hello') # define a pattern

#result = pattern.search ('Hello, world') # search the pattern
#print ( result)

#result = pattern.finditer ('Hello, world')

#for match in result:
   # print(match.start(), match.end(), match.group())  # 


   #a function that takes in two parameters, pattern and text
   # if the text matches the pattern print out the keyword that matched the pattern


def matchPattern ( pattern, text):
    pattern = re.compile ('^tax')
    match = re.search (pattern, text)
    if match:
        print ('Pattern is', pattern)
    else:
        print ('No pattern found')



#regular expression pattern for a kenyan car number
#car number plate ( KAZ 298 F)


import re
text = 'KAZ 298 F'
pattern = re.compile
