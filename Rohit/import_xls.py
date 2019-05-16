# %%
import time
import os
import collections
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import string
from ProjectWorkspace import *
assert os.path.exists(os.path.abspath('ProjectWorkspace.py'))
%matplotlib inline
# plt.style.use('classic')
plt.style.use('fivethirtyeight')


def get_xls(pflag=0):
    """Returns list of Excel files found and for what years.

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
        years.append(int(''.join([y for y in list(year) if y.isdigit()])))
    years = list(sorted(set(years)))
    if pflag:
        print(f'Excel files found= {datasets}\n')
        print(f'Years= {years}\n')
    return datasets, years


def create_empty_city_dataframes(cities=cities, pflag=0):
    """Returns a dictionary containing dataframes corresponding to cities.

    Keyword Arguments:
        cities {dict} -- To be imported from ProjectWorksapce (default: {cities})
    """
    assert isinstance(cities, dict)
    assert all(isinstance(cities[state], list) for state in cities.keys())
    assert os.path.exists(os.path.abspath('ProjectWorkspace.py'))
    dataframe_dict = dict()
    for state in cities.keys():
        dataframe_dict[state] = [None]*len(cities[state])
        for cix, city in enumerate(cities[state]):
            dataframe_dict[state][cix] = pd.DataFrame(
                columns=col_index_names, index=get_xls()[-1])
    if pflag:
        print('Created empty dataframes dict')
    return dataframe_dict


def get_city_indices(cities=cities, sheet=pd.DataFrame()):
    """Returns indices for cities in a pandas dataframe. Function must be called inside `create_city_dataframes()` for now.

    Keyword Arguments:
        cities {dict} -- To be imported from ProjectWorkspace (default: {cities})
        sheet {pandas dataframe} -- Dataframe in which indices are to be found. (default: {sheet})
    """
    assert isinstance(cities, dict)
    assert all(isinstance(cities[state], list) for state in cities.keys())
    assert isinstance(sheet, pd.core.frame.DataFrame)
    assert not sheet.empty
    assert os.path.exists(os.path.abspath('ProjectWorkspace.py'))

    cindexer = {}  # City indexer
    cnames = list(sheet.columns)
    for state in cities.keys():
        cindexer[state] = list()
        for city in cities[state]:
            truevals = sheet[cnames[0]].str.contains(city)
            temp_index = [i for i, x in enumerate(truevals) if x][-1]
            cindexer[state].append(temp_index)
    return(cindexer)


def create_city_dataframes(pflag=0, cities=cities):
    """Creates a dictionary of dataframes, where each dataframe is for a city and has the following structure:
        Columns = Urban Population, Vehicles in Service, Vehicles Available, Vehicle Revenue Miles, Vehicle Revenue Hours, Unlinked Passenger Trips, Passenger Miles.
        Rows = Years for which excel files are present in directory.

    Keyword Arguments:
        pflag {int} -- Print flag, use to check filled dataframes (default: {0})
        cities {dict} -- Dictionary of cities (default: {cities})
    """
    assert isinstance(pflag, int)
    assert pflag == 0 or pflag == 1
    assert isinstance(cities, dict)
    assert all(isinstance(cities[state], list) for state in cities.keys())
    assert os.path.exists(os.path.abspath('ProjectWorkspace.py'))

    datasets, years = get_xls()
    filled_frames = create_empty_city_dataframes()
    for di, excel in enumerate(datasets):
        sheet = pd.read_excel(excel, sheet_name='UZA Totals', index_col=2)
        cnames = list(sheet.columns)
        if pflag:
            print(len(sheet.columns))

        cindexer = get_city_indices(sheet=sheet)
        for state in filled_frames.keys():
            for ix, city_df in enumerate(filled_frames[state]):
                ci = col_index2 if len(cnames) == 15 else col_index
                data = []
                index = zip([cindexer[state][ix]] * len(ci), ci)
                index = list(index)
                for coord in index:
                    data.append(sheet.iloc[coord[0]][coord[1]])
                if years[di] > 2008 and years[di] < 2017:
                    data[3:] = [x*1000 for x in data[3:]]
                city_df.loc[years[di]] = data
    if pflag:
        # Prints the filled dataframe
        print(filled_frames)
    return filled_frames


# %%
start = time.time()
transportation = create_city_dataframes()
end = time.time()
print(f'Time to compute dataframes: {end-start}')

# %% Plotting
sd = transportation['CA'][0]
for column in sd.columns:
    plt.plot(sd.index, sd[column])
    plt.title(f'San Diego - {column}')
    plt.xlabel('Year')
    plt.ylabel(column)
    plt.show()
# %%
# datasets = get_xls()
datasets = ['2009_Fact_Book_Appendix_B.xlsx']
dataset_index = dict()
for excel in datasets:
    sheet = pd.read_excel(excel, sheet_name='UZA Totals', index_col=2)
    cnames = list(sheet.columns)
    print(len(cnames))

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
