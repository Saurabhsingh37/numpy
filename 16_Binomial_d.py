'''
BINOMIAL DISTRIBUTION : THIS IS A DISCRETE DISTRIBUTION .
IT DESCRIBES THE OUTCOME OF LIBRARY SCENARIOS E.G. TOSS OF A COIN IT WILL EITHER BE HEAD OR TAILS .
IT HAS THREE PARAMETER 
n = NUMBER OF TRAILS .
P = PROBABILITY OF OCCURENCE OF EACH TRAIL (I.G. FOR TOSS OF A COIN 0.5 EACH ).
SIZE = THE SHAPE OF THE RETURNED ARRAY : 
'''
#  GIVE 190 TRAIL FOR COIN TOSS GENERATE 10 DATA POINTS:

from numpy import random 
x = random .binomial(n= 10 , p =0.5 , size= 10)
print (x)

# VISUALIZATION OF BINOMIAL DISTRIBUTION 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

x = sns.displot(random.binomial(n= 10 , p= 0.9 , size= 100))
print (x)
plt.show()

#  DIFFERENCE BETWEEN NORMAL AND BINOMIAL DISTRIBUTION 

from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns

data = {
    "normal" : random.normal(loc = 50 , scale = 5 , size = 1000),
    "binomial": random .binomial ( n = 100 , p = 0.5 , size= 1000)
}
sns.displot(data , kind = "kde")
plt.show()


# Student exam score 
import matplotlib.pyplot as plt
import numpy as np

# Simulating exam scores of 100 students (mean=70, std=10)
scores = np.random.normal(70, 10, 100)

plt.hist(scores, bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of Exam Scores")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.show()


