'''
universal function are used to implement vectorization in numpy which is way faster than iterating over elements.
ufunc take additional arguments like:

where  boolean array or condition defining where the operations should take place.

dtype define the return type of element 

out output array where the return value be copied .
'''

# ADD THE ELEMENT OF TWO LISTS
# WITHOUT UFUNC WE CAN USE PYTHON'S BUILD IN ZIP() METHOD:

x = [1,2,3,4]
y = [4,5,6,7]
z= []

for i,j in zip(x,y):
    z.append(i + j)
print ("ADD LIS X,Y:",z)    

# NUMPY HAS A UFUNC FOR THIS , CALLED ADD(X,Y) THAT PRODUCE THE SAME RESULT.
# WITH ufunc, we can use the add() function :

import numpy as np 
x = [1,2,3,4]
y = [5,6,7,8]
z = np.add(x, y)

print(z)


'''
HOW TO CREATE YOUR OWN UFUNC
TO CREATE OWN YOUR UFUNC , YOU HAVE TO DEFINE A FUNCTION , LIKE YOU DO WITH NORMAL FUNCTION IN PYTHON , THEN YOU ADD IT TO YOUR NUMPY UFUNC LIBRARY WITH THE frompyfunc() METHOD.

THE frompyfunc() method takes the following the following arguments:
1. function - the name of the function 
2. inputs - the number of in put argument (arrays).
3. output - the number of output array 
'''

# CREATE YOUR OWN UFUNC 
import numpy as np

def sum (x,y):
    return x+y
sum= np.frompyfunc(sum,2,1)
nsum = sum([1,2,3,4,],[5,6,7,8])
print (nsum)

print("type of nsum : " ,type(np.sum))
print("type of nsum : " ,type(nsum))


