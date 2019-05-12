# %%
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
cnames = list(apta2007.columns.values)
cities = {'CA': ['San Diego, CA', 'San Francisco--Oakland, CA', 'Los Angeles--Long Beach--Santa Ana, CA'], 'WA': ['Seattle, WA'], 'TX': ['Austin, TX', 'Houston, TX', 'Dallas--Fort Worth--Arlington, TX'], 'NY': ['New York--Newark, NY-NJ-CT'], 'IN': ['Chicago, IL-IN'], 'MI': ['Detroit, MI'],
          'GA': ['Atlanta, GA'], 'FL': ['Miami, FL', 'Orlando, FL'], 'AZ': ['Phoenix--Mesa, AZ'], 'PA': ['Philadelphia, PA-NJ-DE-MD', 'Pittsburgh, PA'], 'WI': ['Milwaukee, WI', 'Madison, WI'], 'CO': ['Denver--Aurora, CO'], 'NV': ['Las Vegas, NV'], 'UT': ['Salt Lake City, UT']}
cindexer = {}  # City indexer
for state in cities.keys():
    cindexer[state] = list()
    for city in cities[state]:
        temp_index = apta2007.index[apta2007[cnames[0]] == city].tolist()
        if temp_index:  # Makes sure we are not trying to append when list is empty
            cindexer[state].append(temp_index[0])
print(cindexer)

# %%
plt.style.use('seaborn-whitegrid')
apta2007.plot(
    kind='line', x=apta2007.iloc[0][0], y=apta2007.iloc[0][1])
# %%
