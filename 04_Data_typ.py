# #  python have many data types 
'''STRING 
INTEGER 
FLOAT 
BOOLEAN 
COMPLEX '''

'''
NUMPY  HAS EXTRA MANY SATA TYPES AND REFER TO DATA TYPES WITH ONE CHARACTER .LIKE 
i - INTEGER 
b - BOOLEAN 
u - UNSIGNED INTEGER 
f - FLOAT 
c - COMPLEX FLOAT 
M - TIMEDELTA
O - OBJECT 
S - STRING 
'''

#  CHECK DATA TYPES OF AN ARRAY 
import numpy as np 
arr = np.array([2,3,4,23,2])
print ("array data types : ",arr.dtype)

# STRING DATA TYPES 
arr = np.array(["sa","da","ja"])
print ("array data types : ",arr.dtype)

# CREATING ARRAY WITH DEFINE A DATA TYPES 
arr = np.array([2,5,4,3,3],dtype='S')
print (arr)
print (arr.dtype)

# FOR i,u,F,S AND U WE CAN DEFINE SIZE AS WELL 
# CREATE AN ARRAY WITH DATA TYPES 4BYTE INTEGER 
arr = np.array ([2,3,4,5],'i4')
print (arr)
print (arr.dtype)

# CONVERTING DATA TYPE ON EXISTING ARRAY 
'''
THE BEST WAY TO CHANGE THE DATA  BYTES OF AN EXCITING ARRAY : IS TO MAKE OF THE ARRAY WITH THE astype() METHOD
THE astype() FUNCTION CREATE A COPY OF THE ARRAY AND ALOW YOU TO SPECIFIC DATA TYPE AS A PARAMETER 
'''

arr = np.array([1.2,3.4,6.3,2.2])
newarr = arr.astype('i') # we can write a int 
print (newarr)
print (newarr.dtype)

arr = np.array([2,43,5,3])
newarr = arr.astype('float')
print ("coverted array : ", newarr)
print (newarr.dtype)