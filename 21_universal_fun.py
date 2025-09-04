'''
LCM : LOWEST COMMON MULTIPLE 

The lowest common multiple is the smallest number that is a common multiple of two numbers.
'''
import numpy as np 
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print (x)


#  FINDING LCM IN ARRAY : To find the lowest common multiple of all values in an array ,you can the reduce() method.
arr = np.array([3,6,9])
x = np.lcm.reduce(arr)
print ("LCM",x)


#  FIND THE LCM OF ALL VALUES OF AN ARRAY WHERE THE ARRAY CONTAIN ALL INTEGER FROM 1 TO 10 :
arr = np.arange(1,11)
x = np.lcm.reduce(arr)
print (x)


# GCD : the greatest Common devisor also known as HCF (Highest common factor is the biggest number that is a common factor of both of the number .
#  find the HCF of the Following two number :
import numpy as np 
num1 = 6
num2 = 9 
x= np.gcd (num1,num2)
print(x)
#  3 because that is the highest number both number can be divided by (6/3 =2 and 9/3 = 3)


#  FINDING GCD IN ARRAY : 
# mto find the highest common factor of all values in array you can use the reduce() . method 
# the reduce() method will use the ufunc in this case the gcd() function on each element and reduce the array by one dimension .

import numpy as np 
arr = np .array ([20,8,32,36,16])
x= np.gcd.reduce(arr)
print ("gcd in array : ",x)


#  PYTHAGORAS THEOREM IN NUMPY .
# FINDING HYPOTENUES USING PYTHAGORAS THEOREM IN NUMPY .

import numpy as np 
base = 3 
perp = 4
x= np.hypot(base,perp)
print ("find hypotenues:",x)