'''
NOTE : IF THE VALUE AT AN INDEX IS TRUE THAT ELEMENT IS CONTAINED IN THE FILTERED ARRAY IF THE VALUE THAT INDEX IS FALSE THAT ELEMENT IS EXCLUDED FROM THE FILTERED ARRAY .
'''
# CREATE AN ARRAY FROM THE ELEMENT ON INDEX O OR 2 
import numpy as np   
arr = np.array ([32,42,34,31])
x= [ True, False, True, False]
newarr = arr[x]
print (newarr)


'''
CREATING A FILTER ARRAY  -> IN THE EXAMPLE ABOVE WE HARD TRUE FALSE VALUES BUT THE COMMON USE IS TO CREATE A FILTER ARRAY BASED ON CONDITION 
'''

# CREATING A FILTER ARRAY THAT WILL RETURN ONLY VALUES HIGHER THEN 43 :
arr = np.array ([32,45,56,34,23,52])
# create an empty array 
filter_array  = []

# go through each element in arr 
for i in arr:
    # if i is higher than 43 ,set the value True ,otherwise False :
    if i >42:
        filter_array .append(True)
    else : 
        filter_array.append(False)
newarr = arr[filter_array]
print (filter_array)
print(newarr)            #print element 


# CREATING ARRAY THAT WILL RETURN ONLY EVEN ELEMENT FROM THE ORIGINAL ARRAY :
arr = np.array ([34,25,32,46,76,22])
filter_array = []
for i in arr: 
    if i % 2 == 0:
        filter_array.append(True)
    else:
        filter_array.append(False)
newarr = arr[filter_array] 
print ("print even element : ",newarr)           

# creating filter directly from array Using filter_array keyword : 
# creating a  filter array that will  return only values higher than 32 :
arr = np.array ([43,56,32,23,12])
filter_array = arr>32
newarr = arr[filter_array]
print (filter_array)
print (newarr)

# create a filter array that will return only even element from the original array :
arr = np.array ([23,43,21,23,43,44])
filter_array = arr % 2 == 0
newarr = arr[filter_array]
print (filter_array)
print (newarr)
