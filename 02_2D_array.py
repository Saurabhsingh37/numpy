# crete a 2d array 
#  in this array dimension represent to rows and indexing to column 

import numpy as np 
arr = np.array([[2,5,3,4],[8,7,4,5]])
print ("second element on 1st rows ", arr[0,1]) # first element define to row and second element define to column 

print ("print second row third element : ",arr[1,2])
print ("array:", arr)

#  create 3D array 
arr3 = np. array([[[2,4,5],[6,7,8]],[[1,3,5],[2,4,6]]])
print ("3d array :",arr3)
print(type(arr3))
print ("first block second row third column :", arr3[0,1,2]) #8
print ("second block first row second column :", arr3 [ 1,0,1]) #3


# multi dimension or 3d array 
arr = np.array([[[1,3,4,3],[4,3,2,5],[3,4,5,3]],[[5,4,3,2],[5,8,6,1],[2,3,4,9]],[[2,3,5,2],[4,3,2,3],[6,5,4,4]]])
print(arr)
print ("third block second row third column :", arr[2,1,2]) #2 [b,r,c]- first element represent to block of array and second element represent to rows of block and third element represent to column in rows .

print ("print last element of 2nd dim : ", arr[1,-1])