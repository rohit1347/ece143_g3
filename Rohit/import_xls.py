# %%
import os
import collections
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('classic')

# %%
# Using pandas
# Picking data for 2007 from 2009 xls

apta2007 = pd.read_excel('2009_Fact_Book_Appendix_B.xlsx',
                         sheet_name='UZA Totals', index_col=3)
apta2007 = apta2007.iloc[1:, :]  # Selecting all rows except the 1st one
# Resetting the row index to start from 0
apta2007.index = range(len(apta2007.index))
cnames = list(apta2007.columns)
cities = {'CA': ['San Diego', 'San Francisco', 'Los Angeles'], 'WA': ['Seattle'], 'TX': ['Austin', 'Houston', 'Dallas'], 'NY': ['New York'], 'IN': ['Chicago'], 'MI': ['Detroit'],
          'GA': ['Atlanta'], 'FL': ['Miami', 'Orlando'], 'AZ': ['Phoenix'], 'PA': ['Philadelphia', 'Pittsburgh'], 'WI': ['Milwaukee', 'Madison'], 'CO': ['Denver'], 'NV': ['Las Vegas'], 'UT': ['Salt Lake City']}
cindexer = {}  # City indexer
for state in cities.keys():
    cindexer[state] = list()
    for city in cities[state]:
        truevals = apta2007[cnames[0]].str.contains(city)
        temp_index = [i for i, x in enumerate(truevals) if x][-1]
        cindexer[state].append(temp_index)
print(cindexer)

items = os.listdir(".")

datasets = []
for names in items:
    if names.endswith("Appendix_B.xls") or names.endswith("Appendix_B.xlsx"):
        datasets.append(names)
print(datasets)

# print(cnames)

# %%
plt.style.use('seaborn-whitegrid')
apta2007.plot(
    kind='line', x=apta2007.iloc[0][0], y=apta2007.iloc[0][1])
# %%
