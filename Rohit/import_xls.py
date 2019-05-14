# %%
import os
import collections
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import string
plt.style.use('classic')

# %%
# Extracting list of the names of all required excels


def get_xls():
    """Returns a list of excel files in the directory.
    """
    items = os.listdir(".")  # all items in current directory
    datasets = []
    for names in items:
        if ("Appendix_B.xls" in names) or ("Appendix-B.xls" in names):
            datasets.append(names)
    datasets = sorted(datasets)
    print(f'Excel files found= {datasets}')
    return datasets

# %%
# Using pandas


cities = {'CA': ['San Diego', 'San Francisco', 'Los Angeles'], 'WA': ['Seattle'], 'TX': ['Austin', 'Houston', 'Dallas'], 'NY': ['New York'], 'IN': ['Chicago'], 'MI': ['Detroit'],
          'GA': ['Atlanta'], 'FL': ['Miami', 'Orlando'], 'AZ': ['Phoenix'], 'PA': ['Philadelphia', 'Pittsburgh'], 'WI': ['Milwaukee', 'Madison'], 'CO': ['Denver'], 'NV': ['Las Vegas'], 'UT': ['Salt Lake City']}


def create_city_dataframes(cities=cities):
    """Returns a list of empty dataframes for each city in the input dictionary.

    Keyword Arguments:
        cities {dict} -- Dict with keys='states', and values='cities' (default: {cities})
    """
    assert isinstance(cities, dict)
    assert all(isinstance(cities[state]) for state in cities.keys())
    total_cities = 0
    for state in cities.keys():
        total_cities += len(cities[state])
    dataframe_list = [None] * total_cities
    for idx in range(total_cities):
        dataframe_list[idx] = pd.DataFrame()
    return dataframe_list


# %%
datasets = get_xls()
for excel in datasets:
    sheet = pd.read_excel(excel, sheet_name='UZA Totals', index_col=3)
    cnames = list(sheet.columns)
    print(cnames[0])

    cindexer = {}  # City indexer
    for state in cities.keys():
        cindexer[state] = list()
        for city in cities[state]:
            truevals = sheet[cnames[0]].str.contains(city)
            temp_index = [i for i, x in enumerate(truevals) if x][-1]
            cindexer[state].append(temp_index)
    dataset_index[excel] = cindexer
print(dataset_index)

# %%
dataset_index = dict()

# %%
plt.style.use('seaborn-whitegrid')
apta2007.plot(
    kind='line', x=apta2007.iloc[0][0], y=apta2007.iloc[0][1])
