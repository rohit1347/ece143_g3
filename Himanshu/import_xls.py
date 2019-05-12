# %%
import os
import collections
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('classic')

# %%
# Extracting list of the names of all required excels
items=os.listdir(".") #all items in current directory
datasets=[]
for names in items:
    if ("Appendix_B.xls" in names) or ("Appendix-B.xls" in names):
        datasets.append(names)
datasets=sorted(datasets)
print(datasets)

# %%
# Using pandas
# Picking data for 2007 from 2009 xls
i=0
for excel in datasets:
         sheet = pd.read_excel(excel, sheet_name='UZA Totals', index_col=3)
         sheet = sheet.iloc[1:, :]  # Selecting all rows except the 1st one
         # Resetting the row index to start from 0
         sheet.index = range(len(sheet.index))
         cnames = list(sheet.columns)
         print(cnames)
         cities = {'CA': ['San Diego', 'San Francisco', 'Los Angeles'], 'WA': ['Seattle'], 'TX': ['Austin', 'Houston', 'Dallas'], 'NY': ['New York'], 'IN': ['Chicago'], 'MI': ['Detroit'],
                 'GA': ['Atlanta'], 'FL': ['Miami', 'Orlando'], 'AZ': ['Phoenix'], 'PA': ['Philadelphia', 'Pittsburgh'], 'WI': ['Milwaukee', 'Madison'], 'CO': ['Denver'], 'NV': ['Las Vegas'], 'UT': ['Salt Lake City']}
         cindexer = {}  # City indexer
         for state in cities.keys():
                 cindexer[state] = list()
         for city in cities[state]:
                 truevals = sheet[cnames[0]].str.contains(city)
                 temp_index = [i for i, x in enumerate(truevals) if x][-1]
                 cindexer[state].append(temp_index)
         print(cindexer)
         i=i+1
         print(i)

# %%
plt.style.use('seaborn-whitegrid')
apta2007.plot(
    kind='line', x=apta2007.iloc[0][0], y=apta2007.iloc[0][1])