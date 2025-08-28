'''
SHAPE IS A ATTRIBUTE THAT RETURN A TUPLE WITH  HAVING A NUMBER OF CORRESPONDING ELEMENT .
'''
import numpy as np 
arr = np.array([1,2,3,4,5,6])
print (arr.shape)


# 2D ARRAY 
arr = np.array ([[2,3,4,5],[2,5,4,3],[2,3,4,5]])
print ("shape of array :", arr.shape)

'''
RESHAPING ARRAY MEANS CHANGE THE SHAPE OF ARRAY 
WE CAN CHANGED DIMENSION OF EACH  ELEMENT 
'''
arr = np.array([2,3,4,5,3,2,4,5,2,1,4,3])
newarr = arr.reshape(3 , 4)
print ("new array : " ,newarr)
arr2 = arr.reshape(6 , 2)
print ("print arr2 ", arr2)

# change in 3D array 
arr3d = arr.reshape(2,3,2)
print("print 3d array : ",arr3d)

# UNKNOWN DIMENSION ARRAY USING -1 
arr4 = arr.reshape(2,3,-1)
print("print unknown element array : ",arr4)

# RESHAPE MULTI DIMENSION TO SINGLE DIMENSION 
arr = np.array ([[2,3,4,5],[2,5,4,3],[2,3,4,5]])
newarr = arr.reshape(-1)
print ("print multi to single dimension arr : ",newarr)
