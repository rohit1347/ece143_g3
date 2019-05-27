# %%
import time
import os
import collections
import numpy as np
from numpy import array
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import string
from ProjectWorkspace import *
assert os.path.exists(os.path.abspath('ProjectWorkspace.py'))
%matplotlib qt5

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
# i = 0

# pop2008 = [[0 for x in range(3)] for x in range(14)]

# for state, city_list in transportation.items():
#     city_pop = [d.get('Urban Population') for d in city_list]
#     a = array(city_pop)/1000000
#     col=0
#     for row in a:
#         pop2008[i][col] = row[0]
#         col=col+1
#     i=i+1

# N = 14
# ind = np.arange(N)
# width = 0.35
# p1 = plt.bar(ind, [row[0] for row in pop2008], width)
# p2 = plt.bar(ind, [row[1] for row in pop2008], width, bottom=[row[0] for row in pop2008])
# p3 = plt.bar(ind, [row[2] for row in pop2008], width, bottom=np.array([row[0] for row in pop2008])+np.array([row[1] for row in pop2008]))
# plt.ylabel('Population in millions', color='black')
# plt.title('Population by states and cities', color='black')
# plt.xticks(ind, cities.keys(), color='black')
# plt.tick_params(axis='y', colors='black')
# plt.show()

# fig = plt.Figure()
# ax = Axes3D(fig)
# X = ind
# Y = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2016, 2017, 2019]
# Z =

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = ['r', 'g', 'b', 'y']
for i, (c, z) in enumerate(zip(colors, [30, 20, 10, 0])):
    xs = np.arange(20)
    ys = np.random.rand(20)
    ys2 = np.random.rand(20)
    ys3 = np.random.rand(20)

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.3)
    ax.bar(xs, ys2, bottom=ys, zs=z, zdir='y', color=colors[1], alpha=0.3)
    ax.bar(xs, ys3, bottom=ys+ys2, zs=z, zdir='y', color=colors[2], alpha=0.3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()