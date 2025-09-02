'''
arithmetic conditionally : means we can define conditions where the arithmetic operation should happen.
'''
# ADDITION 
# the add function sums the connect of two arrays and return the result in a array.

import numpy as np  
arr1 = np.array([10,11,12,13,14,15])
arr2 = np.array([20,21,22,23,24,25])
newarr = np.add(arr1,arr2)
print (newarr)


# subtraction function : The subtraction function subtract the value from ine array with the value from another array and return result in a new array .

import numpy as np 
arr1  = np.array([10,20,30,40,50,60])
arr2 = np.array ([20,21,22,23,24,25])
newarr = np.subtract(arr1 , arr2)
print ("SUBTRACT arr1 and arr2 :",newarr)


# MULTIPLICATION >
arr1 = np.array ([1,2,3,4,5])
arr2 = np.array ([1,2,3,4,5])

newarr = np.multiply (arr1 , arr2)
print ("multiply of two array",newarr)

#Division
arr1 = np.array([10,20,30,40])
arr2 = np.array([5,2,4,3])
newarr = np.divide(arr1,arr2)
print ("division : ",newarr)

# POWER : the power () function rises the values from the first array to the power pof the power of the values of the second array and return the result in a array .

import numpy as np  
arr1 = np.array ([2,3,4,5,6])
arr2 = np.array ([2,2,2,2,2])

newarr = np.power(arr1, arr2)
print ("squire / power : ",newarr)



# REMINDER : both the mood () and the function return the reminder of the value in the first array corresponding  to the value in the second array ,and return the result new array .

import numpy as np 
arr1= np.array([10,20,30,40,50])
arr2 = np.array ([3,7,2,4,5])
newarr = np.remainder(arr1 , arr2) #using mod same work as reminder function .
print("reminder : ",newarr)


# QUOTIENT AND MOD
# the divmod() function return both the quotient the mod . the return value is two arrays the first array contains the quotient and second array contains the mod . 

arr1 = np.array ([10,20,30,40])
arr2 = np.array([3,7,8,9])
newarr = np.divmod(arr1,arr2)
print ("first array is quotient : and second array is reminder : ",newarr )