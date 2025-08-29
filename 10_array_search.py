'''
YOU CAN SEARCH AN ARRAY FOR A CERTAIN VALUE AND RETURN THE INDEX THAT GET A MATCH . TO SEARCH AN ARRAY USE THE where() METHOD
'''

import numpy as np 
arr =np.array ([1,2,3,4,2,4,5,4])
x = np.where (arr == 4)
print ("INDEX OF ELEMENT 4:",x)


#  FINDING INDEX WHERE THE VALUE ARE EVEN :
x = np.where(arr % 2 == 0) # we are finding a=odd index using arr % 2 == 1:
print ("even value index : ", x)

'''
there is  method called searchsorted() which performs a binary search in the array , and return the index where the specified value would be inserted to maintain the search order.
'''

# FINDING THE INDEX WHERE THE VALUE 7 SHOULD BE INSERTED : return index to right most 
arr = np.array([1,2,3,4,5,6])
x= np.searchsorted(arr,4)
print ("using searchsorted:",x)

# return index to left most 
arr = np.array([1,2,3,4,5,6])
x = np.searchsorted(arr,4,side='right')
print("right most index 5:",x)

# SEARCH MULTIPLE VALUES 
arr = np.array([1,2,3,4,5,6])
x = np.searchsorted(arr,[3,5,6])
print("search multiple index:",x)
