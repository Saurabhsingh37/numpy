'''
SUMMATIONS : 
what is the difference between summation and addition :
addition is done between two arguments whereas summation happens over n element .
'''

# add the value in array1 and array2 
import numpy as np 
arr1 = np.array ( [1,2,3,4,5])
arr2 = np.array([1,2,3,4,5])
newarr = np.add(arr1,arr2)
print ("addition two array : ", newarr)


# sum of the wwo array : 
newarr = np.sum([arr1,arr2])
print ("sum of two array : ",newarr)


# summation over an axis : 
# if you specify axis=1,numpy will sum the numbers in each array .
import numpy as np 
arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])
newarr = np.sum([arr1,arr2],axis=1)
print ("sum of first array and second array : ",newarr)


#  CUMMULATIVE SUM
# cummulative sum means partially adding the element in array 
# in this using cumsum() function .
import numpy as np 
arr = np.array([1,2,3])
newarr = np.cumsum(arr)
print ("add element partial : ",newarr)


# PRODUCT : TO FIND THE PRODUCT OF THE ELEMENT IN AN ARRAY ,USE THE PROD() FUNCTION 
import numpy as np 
arr = np.array ([1,2,3,4])
x = np.prod(arr)
print("Product of array : ",x)


# FIND THE  PRODUCT OF TWO ARRAY 
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
x = np.prod([arr1,arr2])
print ("product of two array : ",x)


# PRODUCT OVER AN AXIS : IF YOU SPECIFY AXIS = 1 ,NUMPY WILL RETURN THE PRODUCT OF EACH ARRAY :
import numpy as np 
arr1= np.array ([1,2,3,4])
arr2 = np.array([5,6,7,8])
x = np.prod([arr1,arr2],axis=1)
print ("separate product both array : ",x)


# COMMUNICATIVE PRODUCT : communicative product means taking the product partially .using cumprod() function 
arr = np.array ([2,3,4,5])
x = np.cumprod(arr)
print ("cummulative product : ",x)





