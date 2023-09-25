def gameplay():
    import random
    x = ('paper', 'rock', 'scissors')
    x1 = (random.choice(x))
    computerchoice = x1
    
    

    userchoice = input ('Choose either paper,rock or scissors').lower
    numofround = int (input ('choose number of rounds 3 or 5'))

    userscore = 0
    computerscore = 0

    
    if userchoice != 'paper''rock' 'scissors'.lower:
        print ( ' invalid choice')
    
    elif userchoice==computerchoice:
        print (' a tie')
    elif (userchoice == 'paper' and computerchoice == 'rock', 'or' 'scissors'):
         print ( 'user wins')
    elif (userchoice == 'rock' and computerchoice == 'scissors'):
        userscore += 1
        print ( 'user wins')
    else: 
        computerscore += 1
        print(computerscore, 'computer wins')
 
    
   


    for numofround in range (1,3):
        if userscore >= 2:
            print ('user wins')
        if computerscore >= 2:
            print ('computer wins')

    for numofround in range (1,5):
        if userscore >= 3:
            print ('user wins')
        if computerscore >= 3:
            print ('computer wins')
     
    
    if numofround != (3, 5):
        print ('invalid choice')
    
gameplay()

                                                                            


