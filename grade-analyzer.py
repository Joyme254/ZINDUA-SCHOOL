grade = int (input ('Enter your score'))
if (grade> 100):
    print ('Invalid score')

elif (grade == 100):
    print ('Grade A')

elif (grade >= 80):
    print ('Grade A')

elif (grade >= 60):
    print ('Grade B')

elif (grade >=40):
    print ('Grade C')

elif (grade >=20):
    print('Grade D')

elif (grade >=0):
    print('Grade E')

else:
    print ('Error, reenter your Score')
