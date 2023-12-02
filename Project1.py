import pandas as pd 
import numpy as np
import seaborn as sea
import sys
import matplotlib.pyplot as plt

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

#statuses = np.random.choice([0, 1, 2], n_prisoners, p=[0.597, 0.095, 0.196])
#education_level = np.random.choice([0, 1, 2, 3, 4])
#assigning a number to the education level of the prisoner 

Genders = ['Male', 'Female'] 
result = np.random.choice(Genders, 2604, p=[0.925, 0.075])  # BINOMIAL DISTRIBUTION
#print(result)
#another method would be to assign Binomial distribution with 10 trials and probability 0.5 each trial. 
#fig = np.random.binomial(10, 0.5, 10000)

sea.countplot(x=result, order=Genders)
plt.title('Distribution of Gender') 
plt.show()



p = 2604
Genders = ['Male', 'Female'] 
listGender = np.random.choice(Genders, p, p=[0.925, 0.075])
 
Ages = ['Under 21', '21-25', '26-30', '31-35', '36-40', '41-50', '50+']
listAge = np.random.choice(Ages, 2604, p, p=[0.058, 0.194, 0.211, 0.184, 0.133, 0.141, 0.079])
d = {'Gender': listGender, 'Age': listAge}
df = pd.DataFrame(data=d)
print(df)