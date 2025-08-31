'''
POISSON DISTRIBUTION : IT ESTIMATES HOW MANY TIMES AN EVEN HAPPEN IN A SPECIFIED E.G. IF SOMEONE EATS EATS TWICE A DAY WHAT IS THE PROBABILITY HE WILL EAT THRICE .

IT HAS TWO PARAMETER 
LAM =  RATE OF KNOWN NUMBER OF OCCURRENCES E.G. 2 FRO ABOVE PROBLEM .
SIZE = THE SHAPE OF THE RETURN ARRAY . 
'''



# GENERATE RANDOM 1*10 DISTRIBUTION OCCURRENCE 2: 
from numpy import random 
x = random .poisson (lam = 2, size = 10)
print (x)

# VISUALIZATION OF POISSON DISTRIBUTION
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns

sns .displot (random.poisson(lam = 2, size=1000))
plt.show()

# difference between normal and poisson distribution 
from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = {
    "normal": random.normal(loc = 50 , scale=7,size= 1000),
    "poisson": random .poisson(lam =50 ,size=1000)
}
sns.displot(data, kind="kde")
plt.show()