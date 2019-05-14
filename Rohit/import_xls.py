# %%
import os
import collections
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import string
from ProjectWorkspace import cities

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


def create_empty_city_dataframes(cities=cities):
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
    print('Created dataframes list')
    return dataframe_list
# %%


def get_city_indices(cities=cities, sheet=sheet):
    assert isinstance(cities, dict)
    assert all(isinstance(cities[state]) for state in cities.keys())
    assert sheet.__name__ == 'pandas.core.frame.DataFrame'
    cindexer = {}  # City indexer
    cnames = list(sheet.columns)
    for state in cities.keys():
        cindexer[state] = list()
        for city in cities[state]:
            truevals = sheet[cnames[0]].str.contains(city)
            temp_index = [i for i, x in enumerate(truevals) if x][-1]
            cindexer[state].append(temp_index)
    return(cindexer)


# %%
def create_city_dataframes(pflag=0, cities=cities):
    assert isinstance(pflag, int)
    assert pflag == 0 or pflag == 1
    assert isinstance(cities, dict)
    assert all(isinstance(cities[state]) for state in cities.keys())

    datasets = get_xls()
    filled_frames = create_empty_city_dataframes()
    for excel in datasets:
        sheet = pd.read_excel(excel, sheet_name='UZA Totals', index_col=3)
        cnames = list(sheet.columns)
        if pflag:
            # Prints the columns found in each excel file
            print(f'Columns in {excel}: {cnames}\n')
        for citynum, cframe in enumerate(filled_frames):
            cindexer = get_city_indices()
            # What is left:
            # (i) You are in a sheet
            # (ii) you have the row indices for the cities in the sheet
            # (iii) You need to find the column indices for the data you want
            # (iv) Store the data in one column of the dataframe


datasets = get_xls()
dataset_index = dict()
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
plt.style.use('seaborn-whitegrid')
apta2007.plot(
    kind='line', x=apta2007.iloc[0][0], y=apta2007.iloc[0][1])
