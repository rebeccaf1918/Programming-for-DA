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

1. Age - categorical discrete 
2. Gender - Categorical nominal data (Or region)
3. Type of offence - categorical nominal 
4. Length of imprisonment - 
5. Education level/economic of criminal - categorical ordinal
'''
# Look at those sentenced in 2022 and their probability of reoffending

# import pandas with shortcut 'pd' 
import pandas as pd 

#############
# Set the seed so that the numbers can be reproduced.
np.random.seed(0)  

# 2747 people released in 2020 (41% reoffended within 1 year of release from custodial sentence)

#genders = ['Male', 'Female'] 
#result = np.random.choice(genders, 4122, p=[0.96, 0.04]) # setting the probability per https://www.iprt.ie/latest-news/irish-prison-service-annual-report-2022/
# as per 2022 prison population 
#print(result) # displaying the resultant array 

#Bernoulli distribution


### 
# Determining variables affecting prison commitals: Age, Gender, Education level, Type of offence, region?

#Genders = ['Male', 'Female'] 
#result = np.random.choice(genders, 5801, p=[0.891, 0.109]) # per https://www.iprt.ie/latest-news/irish-prison-service-annual-report-2022/
#print(result)

Ages = ['18-24', '25-34', '35-44', '45-54', '55+']
age = np.random.choice(Ages, 5045, p=[0.153, 0.38, 0.297, 0.118, 0.052])
#print(age)
# excludes those not sentenced eg those commited on contempt of court & on remand awaiting trial
# https://www.irishprisons.ie/wp-content/uploads/documents_pdf/SENTENCED-COMMITTALS-by-Age-and-Gender-Year-2007-to-2022.pdf

#Ages = ['Under 21', '21-25', '26-30', '31-35', '36-40', '41-50' '50+']
#age = np.random.choice(Ages, 2604, p=[0.057, 0.193, 0.211, 0.184, 0.133, 0.141, 0.078])



sea.countplot(x=age, order=Ages)
plt.title('Distribution of Age Groups')
plt.show()

## If you want to visualize this distribution, you can use a bar plot or a pie chart, which are suitable for categorical data. If you want to fit a known distribution to your data, that’s a more complex task and may not be possible without additional assumptions or data.
# if you have reason to believe that the underlying age distribution is normal (or any other known distribution), you could fit a model to your data using maximum likelihood estimation or other methods. However, this would require you to assign a numerical value to each age group, which may not accurately reflect the true age distribution.
#In most cases, the best way to model a distribution across categorical data is to use the observed frequencies (or probabilities) of each category, as you’ve done. This gives you a direct representation of the distribution without making additional assumptions.
#^^^ # rewrite


#total prison releases in 2017 = 2604 
