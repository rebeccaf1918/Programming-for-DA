# Choose a real-world phenomenon that can be measured and for which you could
# collect at least one-hundred data points across at least four different variables.
# Investigate the types of variables involved, their likely distributions, and their relationships with each other.
# Synthesise/simulate a data set as closely matching their properties as possible.
# Detail your research and implement the simulation in a Jupyter notebook – the data set itself can simply be displayed in an output cell within the notebook.




import pandas as pd 
import numpy as np
import seaborn as sea
import sys
import matplotlib.pyplot as plt


''''
Probabiltiy of reoffending: 

1. Age - Numerical continuous data 
2. Gender - Categorical nominal data (Or region)
3. Type of offence - categorical nominal 
4. Length of imprisonment - 
5. Education level/economic of criminal - categorical ordinal
'''

# import pandas with shortcut 'pd' 
import pandas as pd 

#############
# Set the seed so that the numbers can be reproduced.
np.random.seed(0)  


#df = pd.DataFrame('gender': np.random.choice(gender, 1000,p=[0.891, 0.109]))

# 2747 people released in 2020 (41% reoffended within 1 year of release from custodial sentence)

genders = ['Male', 'Female'] 
result = np.random.choice(genders, 4122, p=[0.96, 0.04]) # setting the probability per https://www.iprt.ie/latest-news/irish-prison-service-annual-report-2022/
# as per 2022 prison population 
print(result) # displaying the resultant array 

ages = 

age = np.random.randint(15,100, 4122)


### 
# Determining variables affecting prison commitals: Age, Gender, Education level, Type of offence, region?

#Genders = ['Male', 'Female'] 
#result = np.random.choice(genders, 5801, p=[0.891, 0.109]) # per https://www.iprt.ie/latest-news/irish-prison-service-annual-report-2022/
#print(result)

