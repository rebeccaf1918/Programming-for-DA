# Choose a real-world phenomenon that can be measured and for which you could
# collect at least one-hundred data points across at least four different variables.
# Investigate the types of variables involved, their likely distributions, and their relationships with each other.
# Synthesise/simulate a data set as closely matching their properties as possible.
# Detail your research and implement the simulation in a Jupyter notebook – the data set itself can simply be displayed in an output cell within the notebook.


# Variables impacting household income in Ireland

'''
1. Age
2. Employment sector 
3. Region
4. Gender (or nationality)
'''

import pandas as pd 

# merging two csv files 
# df = pd.concat( 
 #   map(pd.read_csv, ['Region.csv', 'Employmenttype.csv', 'Age.csv']), ignore_index=True) 
#print(df) 