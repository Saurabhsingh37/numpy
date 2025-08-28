'''
JOIN MEANS PUTTING CONTENT OF TWO OR MORE ARRAYS IN A SINGLE ARRAY .
WE PASS A SEQUENCE OF ARRAY THAT MWE WANT TO JOIN TO THE CONCATENATE() FUNCTION  //WE USE TO THIS FUNCTION SQL
'''

import numpy as np 
arr = np.array([1,2,3])
arr2 = np.array ([4,5,6])
newarr = np.concatenate((arr,arr2))
print ("concatenate array : ",newarr)


#  JOIN 2D ARRAY 
arr1 = np. array([[1,2,3,4],[5,6,7,8]])
arr2 = np. array([[1,2,3,4],[5,6,7,8]])
arr = np.concatenate((arr1,arr2))
print ("concatenate 2d array :", arr)
print (arr.shape)

arr = np.concatenate((arr1,arr2),axis=1) 
print("column wise ",arr)
arr = np.concatenate((arr1,arr2),axis=0) 
print ("row wise ",arr)

# axis using a if axis = 1 so join column wise  and if axis = 0 so function join rows wise 

# JOIN USING STACK() FUNCTION  STACK FUNCTION SAME AS A CONCATENATION FUNCTION BUT STACK FUNCTION CRETE A NEW AXIS 

arr = np.stack((arr1,arr2),axis=0)
print ("using stack",arr)

# USING HSTACK() PRINT SINGLE ROWS ELEMENT 
arr = np.hstack ((arr1,arr2))
print ("using hstack():",arr)

# VSTACK() TO STACK ALONG COLUMN 
arr = np.vstack ((arr1,arr2))
print ("using vstack():",arr)

# USING DSTACK() 
arr = np.dstack ((arr1,arr2))
print ("using dstack():",arr)
