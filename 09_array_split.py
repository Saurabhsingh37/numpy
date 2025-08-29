'''
SPLITTING ARRAY BREAKS ONE ARRAY INTO MULTIPLE ARRAY 
'''
import numpy as np 
arr = np.array ([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print ("split array : ",newarr,end='  ')

# IF THE ARRAY HAS LESS ELEMENT THEN REQUIRED IT WILL ADJUST FROM THE END ACCORDINGLY 

arr = np.array([1,2,3,4,5,6,7])
newarr = np.array_split(arr,4)
print ("split array 7 element : ",newarr)

'''
ARRAY_SPLIT FUNCTION RETURN ARRAY A KIST FORM BUT WE CAN RETURN ELEMENT A ARRAY FORM SO THEM FROM THE RESULT JUST LIKE WRITE DOWN .....
'''
arr = np.array ([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print (newarr[0])
print (newarr[1])
print (newarr[2])

# SPLITTING 2D ARRAYS 
arr = np.array([[1,2,3,4],[5,6,7,8],[2,3,4,2]])
newarr = np.array_split(arr,1)
print ("split 2d array : ",newarr)

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)


# using axis = 1 
newarr = np.array_split(arr,3,axis=1)  # same work hsplit() function 
print ("using axis = 1 : ",newarr) 

'''
NOTE : SIMILAR ALTERNATE MTO VSTACK()AND DSTACK() ARE AVAILABLE AS VSPLIT() ANS DSPLIT().
'''