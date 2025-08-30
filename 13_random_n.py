'''
RANDOM NUMBER DOES NOT MEAN A  DIFFERENT NUMBER EVERY TIME .RANDOM MEANS SOMETHING THAT CAN NOT BE PREDICT LOGICALLY 
'''

# NUMPY OFFERS THE RANDOM MODULE TO WORK WITH RANDOM NUMBERS.
# generating a random integer from 0 to 100 : 
import numpy as np
x = np.random.randint(100)
print (x)

# generating a random float number from 1 to 0 : using rand ()function 
from numpy import random
x = random.rand()
print (x)


# GENERATING RANDOM ARRAY 
'''
IN NUMPY WE WORK WITH ARRAY AND YOU CAN USE THE TWO METHOD FROM THE ABOVE EXAMPLE MAKE RANDOM ARRAYS :

THE RANDINT() METHOD TAKES A SIZE PARAMETER WHERE YOU CAN SPECIFY THE SHAPE OF AN ARRAY :
'''
# GENERATING A 1D ARRAY CONTAINING 5 RANDOM INTEGER FROM 0 TO 100 :

from numpy import random
x = random.randint(100,size=(5))
print ("print random array :",x)

# GENERATING 2-D ARRAY WITH 4 ROWS CONTAINING 5 RANDOM INTEGER FROM 0 TO 100:
x = random.randint(100,size=(4,5))
print ("print random 2d array : ",x)

# GENERATING A 2-D ARRAY WITH 3 ROWS CONTAINING 5 RANDOM FLOATING NUMBER : 
x = random .rand(3 ,5)
print ("generate 2d floating array :",x)

'''
GENERATING ARRAY FROM YOUR GIVEN CHOICE ELEMENT 
THE choice() METHOD ALLOW YOU MTO GENERATING A RANDOM VALUE BASED ON AN ARRAY 
THE choice() METHOD TAKES AN ARRAY AS A PARAMETER AND RANDOM RETURN ONE OF THE VALUES:
'''

# return one of the value in the array : 

x = random .choice([4,3,6,7,2])
print ("choice based return element : " ,x)


#  GENERATE THE 2D ARRAY THAT CONSIST OF THE VALUE IN THE ARRAY PARAMETER (1,2,3,4)

x = random.choice([1,2,3,4,5],size=(3,4))
print("generating random element array : ",x)