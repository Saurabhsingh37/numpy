import numpy as np
arr = np.array([2,3,5,4,3,2,3,5])
print ("print to first two element : ", arr[0:1])
print ("print second index to end of index :",arr[1:])
print("print starting to 4th indexing :" , arr[ :3])

# negative indexing using accessing element to last 
print ("print last element ",arr[-1:])
print("quid the last element : ", arr[:-1])
print(arr[-2:-1])

# using gap between element of array 
print ("print all even index element: ", arr[1: :2])
print ("gap between element of 4 indexing :" , arr[0:7:4])
print (arr[::2])



# 2D array 

arr2 = np.array([[2,3,4,5],[5,8,7,1]])
print("first row second column print : ",arr2[0,0: ])
print("first row third column to last :",arr2[0,2: ])
print ("both index slicing : ",arr2[0:3 ,1: ])