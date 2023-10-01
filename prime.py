# a function that prints prime numbers in a range

def prime (num ) :
    if num <= 2:
        return False
    for i in range ( 2, num):
        if num%i ==0:
            return False
    return True

   

#def primenumberinrange (x,y):
    
for num in range ( 1, 100):
    if prime (num):
        print (num)



#x =int ( input ('enter the lowest number in range'))
#y =int ( input ('enter the highest number in range'))

#primenumberinrange (x,y)

