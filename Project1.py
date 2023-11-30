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

# import pandas with shortcut 'pd' 
import pandas as pd 


#############
# Set the seed so that the numbers can be reproduced.
np.random.seed(0)  

# 2747 people released in 2020 (41% reoffended within 1 year of release from custodial sentence)
#Ages = ['18-24', '25-34', '35-44', '45-54', '55+']
#age = np.random.choice(Ages, 5045, p=[0.153, 0.38, 0.297, 0.118, 0.052])
#print(age)
# excludes those not sentenced eg those commited on contempt of court & on remand awaiting trial
# https://www.irishprisons.ie/wp-content/uploads/documents_pdf/SENTENCED-COMMITTALS-by-Age-and-Gender-Year-2007-to-2022.pdf


## If you want to visualize this distribution, you can use a bar plot or a pie chart, which are suitable for categorical data. If you want to fit a known distribution to your data, that’s a more complex task and may not be possible without additional assumptions or data.
# if you have reason to believe that the underlying age distribution is normal (or any other known distribution), you could fit a model to your data using maximum likelihood estimation or other methods. However, this would require you to assign a numerical value to each age group, which may not accurately reflect the true age distribution.
#In most cases, the best way to model a distribution across categorical data is to use the observed frequencies (or probabilities) of each category, as you’ve done. This gives you a direct representation of the distribution without making additional assumptions.
#^^^ # rewrite


#

Economic_Status = ['Neither employment nor education', 'substantial employment only', 'education and training only',
                   'education and training and substantial employment', 'not identified' ]

Status = np.random.choice(Economic_Status, 2604, p=[0.597, 0.095, 0.196, 0.022, 0.09])
#print(Status)

sea.countplot(x=Status, order=Economic_Status)
plt.title('Distribution of Age Groups')
plt.show()



#https://www.cso.ie/en/releasesandpublications/fp/p-offo/offenders2016employmenteducationandotheroutcomes2016-2019/introduction/
#statuses = np.random.choice([0, 1, 2], n_prisoners, p=[0.597, 0.095, 0.196])

#education_level = np.random.choice([0, 1, 2, 3, 4])

#assigning a number to the education level of the prisoner 


