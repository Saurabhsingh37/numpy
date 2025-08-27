'''
THE MAIN DIFFERENCE A COPY DATA AND A VIEW OF AN ARRAY IS THAT THE COPY IS A ARRAY AND THE VIEW IS JUST A VIEW OF THE ORIGINAL ARRAY . 
'''

# USING COPY FUNCTION THIS FUNCTION CREATE A NEW ARRAY OR COPY ARRAY 
import numpy as np 
arr = np.array([2,3,4,5,5])
a = arr.copy()
arr[0] = 32
a[0] = 42
print ("print array arr: ",arr)
print ("print array a /copy array : ", a)

# MAKE A VIEW CHANGE THE ORIGINAL ARRAY ,AND DISPLAY BOTH ARRAYS:
arr = np.array([2,1,3,4,3])
x = arr.view()
arr[0] = 32
print ("print arr : ", arr) 
print ("print view array x : ", x)
# THE VIEW SHOULD BE EFFECTED BY HTE CHANGE MADE TO THE  ORIGINAL ARRAY 


# CHANGED A VIEW ELEMENT TO EFFECTED TO ORIGINAL ARRAY 
arr  = np.array([2,4,3,5,8])
x = arr.view()
x[0] = 32
print ("print original array : ", arr)
print ("print view of array :", x)
# THE ORIGINAL ARRAY SHOULD BE AFFECTED BY THE CHANGES MAKE TO THE VIEW 

# USING BASE ATTRIBUTE IT IS RETURN ORIGINAL DATA OR NOT 
arr  = np.array([2,4,3,5,8])
x = arr.view()
y = arr.copy()
print ("print view array types: ", x.base)
print ("print copy of array datatypes :", y.base)