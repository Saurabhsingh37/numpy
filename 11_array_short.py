'''
SORTING MEANS PUTT9NG ELEMENT IN AN ORDER SEQUENCE. ASCENDING OR DESCENDING ORDER 
'''

# SHORT THE ARRAY 
import numpy as np  
arr = np.array ([5,3,4,1,2])
newarr = np.sort(arr)
print ("shorting array: ",newarr)
print(np.sort(arr))

# THIS METHOD RETURN A COPY OF THE ARRAY LEAVING THE ORIGINAL ARRAY UNCHANGED .

# YOU CAN ALSO SORT ARRAY OF STRING , OR ANY OTHER SATA TYPES 

arr = np.array (["saurabh", "gaurabh","sajan","meera"])
sortarr = np.sort(arr)
print ("sort string : ", sortarr)

# 2D ARRAY SORTING , IF YOU USE THE SHORT METHOD ON A 2D ARRAY BOTH ARRAY WILL BE SORTED:

arr = np.array ([[2,5,3,1],[7,5,9,4]])
newarr  = np.sort(arr)
print ("sorting 2d array : ",newarr)