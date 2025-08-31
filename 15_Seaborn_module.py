'''
SEABORN  IS A  LIBRARY THAT USE MATPLOTLIB UNDERNEATH TO PLOT GRAPHS .
IT WILL BE USED TO VISUALIZE RANDOM DISTRIBUTION 
'''
'''
DISPLOTS : DISPLOTS STAND FOR PLOT IT TAKES AS INPUT AN ARRAY PLOT A CURVE CORRESPONDING TO THE DISTRIBUTION OF IN THE ARRAY .
'''
# IMPORT MATPLOTLIB AND SEABORN MODULE :

# import matplotlib.pyplot as plt 
import seaborn as sns
sns.displot([0,1,2,3,4,5,6])
plt.show()

# plotting a displot without the histogram
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()

'''
NORMAL DISTRIBUTION : THE NORMAL DISTRIBUTION IS ONE OF THE MOST IMPORTANT DISTRIBUTION 
IT IS ALSO CALLED THE GAUSSIAN DISTRIBUTION AFTER THE GERMAN MATHEMATICS CARL FRIENDRICH GAUSS:
IN THIS USE THE random.normal() METHOD TO GET A NORMAL DATA DISTRIBUTION : 
IT HAS THREE PARAMETER : 
loc = where the peek of the bell exists 
scale - standard deviation how flat the graph distribution should be .
size - the shape of the return array : 
'''
#  generate of normal distribution of size 2*3:
from numpy import random 
x = random .normal(size=(2,3))
print (x)

# GENERATE A RANDOM NORMAL DISTRIBUTION OF SIZE 2*3 WITH MEAN AT 1 AND STANDARD DEVIATION OF 2 :
from numpy import random 
x = random .normal (loc= 1, scale= 2,size=(2,3))
print(x)

# VISUALIZATION OF NORMAL DISTRIBUTION 

from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal (size=1000), kind = "kde")
plt.show()