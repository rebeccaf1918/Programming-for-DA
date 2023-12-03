import pandas as pd 
import numpy as np
import seaborn as sea
import sys
import matplotlib.pyplot as plt

# Set the seed so that the numbers can be reproduced.
np.random.seed(0)  

# excludes those not sentenced eg those commited on contempt of court & on remand awaiting trial
# https://www.irishprisons.ie/wp-content/uploads/documents_pdf/SENTENCED-COMMITTALS-by-Age-and-Gender-Year-2007-to-2022.pdf

## If you want to visualize this distribution, you can use a bar plot or a pie chart, which are suitable for categorical data. If you want to fit a known distribution to your data, that’s a more complex task and may not be possible without additional assumptions or data.
# if you have reason to believe that the underlying age distribution is normal (or any other known distribution), you could fit a model to your data using maximum likelihood estimation or other methods. However, this would require you to assign a numerical value to each age group, which may not accurately reflect the true age distribution.
#In most cases, the best way to model a distribution across categorical data is to use the observed frequencies (or probabilities) of each category, as you’ve done. This gives you a direct representation of the distribution without making additional assumptions.
#^^^ # rewrite

#statuses = np.random.choice([0, 1, 2], n_prisoners, p=[0.597, 0.095, 0.196])
#education_level = np.random.choice([0, 1, 2, 3, 4])
#assigning a number to the education level of the prisoner 

#result = np.random.choice(Genders, 2604, p=[0.925, 0.075])  # BINOMIAL DISTRIBUTION
#print(result)
#another method would be to assign Binomial distribution with 10 trials and probability 0.5 each trial. 
#fig = np.random.binomial(10, 0.5, 10000)

original_stdout = sys.stdout 
with open ("SimulatedDataSet.txt", "w") as f: #w to write to file and opened it as it didn't already exist  
    sys.stdout = f
    p = 2604
    Genders = ['Male', 'Female'] 
    listGender = np.random.choice(Genders, p, p=[0.925, 0.075])
 
    Ages = ['Under 21', '21-25', '26-30', '31-35', '36-40', '41-50', '50+']
    listAge = np.random.choice(Ages, 2604, p, p=[0.058, 0.194, 0.211, 0.184, 0.133, 0.141, 0.079])

    Economic_Status = ['No employment nor education', 'substantial employment only', 'education and training only',
                   'education, training and substantial employment', 'Not identified' ]
    Shorter_Name = ['No Edu or Emp', 'Emp Only', 'Edu & Training Only', 'Edu, Training & Emp Only',
                        'Not Identified']
    label_dict = dict(zip(Shorter_Name, Economic_Status))
    listEconomicStatus = np.random.choice(Shorter_Name, 2604, p=[0.298, 0.047, 0.264, 0.028, 0.363])

    Original_Offence_Type = ['Homicide Offences', 'Sexual Offences', 'Attempts/threats to murder, assaults, harassments and related offences',
                        'Dangerous or negligent acts', 'Kidnapping & related offences', 'Robbery, extortion and hijacking offences',
                        'Burglary and related offences', 'Theft and related offences', 'Fraud, deception and related offences', 
                        'Controlled drug offences', 'Weapons and Explosives Offences', 'Damage to property and to the environment',
                        'Public order and other social code offences', 'Road and traffic offences', 'Offences against government, justice procedures and organisation of crime',
                        'offences not elsewhere classified']

    Shortened_Offence = ['Homicide', 'SO', 'Atmptd murder/assault', 'Negligence', 'Kidnapping', 
                    'Robbery', 'Burglary', 'Theft', 'Fraud', 'DO', 'WO', 'PD', 'Public Order',
                    'RTO', 'Offences agnst Gov', 'Unclassified']

    label_dict = dict(zip(Shortened_Offence, Original_Offence_Type))
    probabilities = [0.0096, 0.03226, 0.1321, 0.0411, 0.00384, 0.01728, 0.07411, 
                 0.22772,0.02457, 0.09254, 0.04032, 0.05299, 0.05798, 0.10637,
                 0.06835, 0.01881]
    probabilities = [i/sum(probabilities) for i in probabilities]   # rescaling the probabilities ******

    listOffence = np.random.choice(Shortened_Offence, 2604, p=probabilities)

    d = {'Gender': listGender, 'Age': listAge, 'Economic Status' :listEconomicStatus, 'Offence Type': listOffence}
    # creating a dictionary for the dataframe
    df = pd.DataFrame(data=d)
    print(df)
    print(df.describe())
    sys.stdout = original_stdout


