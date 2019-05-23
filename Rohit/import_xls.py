# %%
from ProjectWorkspace import *
import plotly.figure_factory as ff
import plotly
import plotly.plotly as py
import time
import os
import collections
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import string
import itertools as it
%matplotlib inline
plt.style.use('fivethirtyeight')
# %%


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
        years.append(int(''.join([y for y in list(year) if y.isdigit()]))-2)
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
            dataframe_dict[state][cix].index.name = 'Year'
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
                if years[di] > 2006 and years[di] < 2015:
                    data[3:] = [x * 1000 for x in data[3:]]
                data = pd.to_numeric(data)
                city_df.loc[years[di]] = data
    if pflag:
        # Prints the filled dataframe
        print(filled_frames)
    return filled_frames


def get_simple_plots(filled_frames, state='CA', city_index=0):
    """Gives simple plots for specified city.

    Arguments:
        filled_frames {dict} -- Dictionary containing the relevant data for all cities.
        Specify `Matplotlib` style and magic commands before the function, if needed.

    Keyword Arguments:
        state {str} -- Specify which state the city is in (default: {'CA'})
        city_index {int} -- Look up the index for cities in the dictionary `cities` (default: {0})
    """
    assert isinstance(filled_frames, dict)
    assert isinstance(filled_frames[state]
                      [city_index], pd.core.frame.DataFrame)
    assert 'matplotlib' in sys.modules
    df_to_plot = filled_frames[state][city_index]
    for column in df_to_plot.columns:
        plt.figure(figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.plot(df_to_plot.index, df_to_plot[column])
        plt.title(f'{cities[state][city_index]} - {column}')
        plt.xlabel('Year')
        plt.ylabel(column)
        plt.show()


def transform_city_dataframes(filled_frames, ttype=[0]):
    """Generator for returning transformed city transportation data.

    Arguments:
        filled_frames {dict} -- Dictionary containing city data.

    Keyword Arguments:
        ttype {list} -- Choose type of transform. Can obtain multiple transforms by adding options to list (default: {[0]}).

    `ttype` Options:
        0 -- Per 1000 people
        1 -- Per person
    """
    assert isinstance(ttype, list)
    assert all(isinstance(obj, int) for obj in ttype)
    assert isinstance(filled_frames, dict)
    mdf = filled_frames
    # Modified dataframe
    for tix, ty in enumerate(ttype):
        if ty == 0:
            # For per 1000 people calculation, value/pop*1000
            for state in mdf.keys():
                for city, df in enumerate(mdf[state]):
                    df.columns = col_index_names1000
                    df.iloc[:, 1:] = df.iloc[:, 1:].div(1/1000).div(
                        df.iloc[:, 0], axis='index')
        if ty == 1:
            for state in mdf.keys():
                for city, df in enumerate(mdf[state]):
                    df.columns = col_index_names_p
                    df.iloc[:, 1:] = df.iloc[:, 1:].div(
                        df.iloc[:, 0], axis='index')
        yield mdf


def plotly_transportation():
    plotly.tools.set_credentials_file(
        username='rohit1347', api_key='wP0wJffd8666ba1iS6CT')
    plotly.tools.set_config_file(world_readable=True, sharing='public')
    df = create_city_dataframes()
    df = next(transform_city_dataframes(df, ttype=[0]))
    COUNTIES = []
    values = []
    fips = []
    idx = 1
    for state in df.keys():
        for county in range(len(df[state])):
            values.append(df[state][county].iloc[0, idx])
            COUNTIES.append(cities[state][county])
            fips.append(int(cities_fips[state][county]))

    colorscale = [
        'rgb(68.0, 1.0, 84.0)',
        'rgb(66.0, 64.0, 134.0)',
        'rgb(38.0, 130.0, 142.0)',
        'rgb(63.0, 188.0, 115.0)',
        'rgb(216.0, 226.0, 25.0)'
    ]

    fig = ff.create_choropleth(fips=fips, values=values, county_outline={
                               'color': 'rgb(255,255,255)', 'width': 0.5}, legend_title=df[state][county].columns[idx])
    fig['layout']['legend'].update({'x': 0})
    fig['layout']['annotations'][0].update({'x': -0.12, 'xanchor': 'left'})
    return fig


# %%
start = time.time()
tp = create_city_dataframes()
end = time.time()
print(f'Time to compute dataframes: {end-start:.2f}')
sd = tp["CA"][0]

# %%
h = next(transform_city_dataframes(tp, ttype=[1]))

# %% Plotting
get_simple_plots(tp, state='NY')
# %%
py.iplot(plotly_transportation(), filename='transportation')


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
