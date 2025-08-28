'''
ITERATING ARRAY MEANS GOING THROUGH ELEMENT ONE BY ONE .
'''

# PRINT SINGLE DIMENSION ARRAY
import numpy as np
arr = np.array([1,2,3,4,5,6])

for i in arr:
    print ("element of array :",i , end = '\n')


# iterating 2d array 
arr = np.array([[2,2,4,5],[3,4,3,2]]) 

for x in arr:
    for y in x:
        print ("element of 2d array :",y ,end='\n')
        
# ITERATING 3D ARRAY 

arr = np.array([[[2,3,4],[1,2,3]],[[5,4,3],[4,3,2]]])
for i in arr:
    for j in i:
        for k in j:
            print ("print 3d array element :" , k ,end='\n') 
            
'''
USING nditer() IS A HELPING FUNCTION THAT CAN BE USED VERY BASIC TO VERY ADVANCED ITERATIONS IT SOLVE SOME BASIC ISSUES WHICH WE FACE IN ITERATION LETS GO THROUGH IT WITH EXAMPLES .
'''           

arr = np.array([[[1,2,3],[4,5,6]],[[4,5,6],[5,4,3]]])
for x in np.nditer(arr):
    print("element using nditer:", x)
    

#ITERATE WITH DIFFERENT DATA TYPES 
arr = np.array([1,2,3])
for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
    print ("change data types : ",x)
    
#ITERATING WITH DIFFERENT STEP SZE : 
arr = np.array ([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[ : ,: : 2]):
    print (x)
    
# PRINT ELEMENT WITH INDEX USING NDENUMERATE() FUNCTION 
arr = np.array([1,2,3,4,5])
for idx, x in np.ndenumerate(arr):
    print ("index of ele: ",idx,"element :",x)    
    
#Enumerate on following 2d arrays elements:
arr = np.array([[1,2,3],[2,3,4]]) 
for ind , x in np.ndenumerate(arr):
    print ("index:",ind,"element: ",x)   