def vowelscount (statement):
    count = 0
    vowels = 'a', 'e', 'i','o','u','A','E','I','O','U'
   
    for char in statement:
        if char in vowels:
            count += 1
    return count
            

statement = input ( 'enter a statement')
vocount = vowelscount (statement)
print ( 'number of vowels', vocount)