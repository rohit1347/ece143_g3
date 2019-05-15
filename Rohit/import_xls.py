# %%
import os
import collections
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import string
from ProjectWorkspace import *

plt.style.use('classic')

# %%


def get_xls(pflag=0):
    """Returns a list of Excel files found and for what years.

    Keyword Arguments:
        pflag {int} -- Print flag (default: {0})
    """
    items = os.listdir(".")  # all items in current directory
    datasets = []
    for names in items:
        if ("Appendix_B.xls" in names) or ("Appendix-B.xls" in names):
            datasets.append(names)
    datasets = sorted(datasets)
    years = []
    for year in datasets:
        years.append(''.join([y for y in list(year) if y.isdigit()]))
    if pflag:
        print(f'Excel files found= {datasets}\n')
        print(f'Years= {years}\n')
    return datasets, years


def create_empty_city_dataframes(cities=cities):
    """Returns a dictionary containing dataframes corresponding to cities.

    Keyword Arguments:
        cities {dict} -- To be imported from ProjectWorksapce (default: {cities})
    """
    assert isinstance(cities, dict)
    assert all(isinstance(cities[state], list) for state in cities.keys())
    # total_cities = 0
    # for state in cities.keys():
    #     total_cities += len(cities[state])
    # dataframe_list = [None] * total_cities
    dataframe_dict = dict()
    for state in cities.keys():
        dataframe_dict[state] = [None]*len(cities[state])
        for cix, city in enumerate(cities[state]):
            dataframe_dict[state][cix] = pd.DataFrame(
                columns=col_index_names, index=get_xls()[-1])
    # for idx in range(total_cities):
    #     dataframe_list[idx] = pd.DataFrame(columns=col_index_names)
    print('Created dataframes list')
    return dataframe_dict


# %%
def create_city_dataframes(pflag=0, cities=cities):
    assert isinstance(pflag, int)
    assert pflag == 0 or pflag == 1
    assert isinstance(cities, dict)
    assert all(isinstance(cities[state], list) for state in cities.keys())

    datasets, years = get_xls()
    filled_frames = create_empty_city_dataframes()
    for excel in datasets:
        sheet = pd.read_excel(excel, sheet_name='UZA Totals', index_col=3)
        cnames = list(sheet.columns)
        if pflag:
            # Prints the columns found in each excel file
            print(f'Columns in {excel}: {cnames}\n')
        cindexer = get_city_indices()
        for citynum, cframe in enumerate(filled_frames):
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


def get_city_indices(cities=cities, sheet=sheet):
    """Returns indices for cities in a pandas dataframe. Function must be called inside `create_city_dataframes()` for now.

    Keyword Arguments:
        cities {dict} -- To be imported from ProjectWorkspace (default: {cities})
        sheet {pandas dataframe} -- Dataframe in which indices are to be found. (default: {sheet})
    """
    assert isinstance(cities, dict)
    assert all(isinstance(cities[state], list) for state in cities.keys())
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
plt.style.use('seaborn-whitegrid')
apta2007.plot(
    kind='line', x=apta2007.iloc[0][0], y=apta2007.iloc[0][1])
# %% Testing
create_empty_city_dataframes()
