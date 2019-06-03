# %%
from ProjectWorkspace import *

import time
import os
import collections
import numpy as np
from numpy import array
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import string
from bokeh.plotting import figure, show, output_file
#from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.us_states import data as states
from bokeh.palettes import Greys256 as palette
from bokeh.layouts import column, row, widgetbox
from bokeh.models import CustomJS, Slider, Toggle
from bokeh.models.callbacks import CustomJS
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, HoverTool, LogColorMapper
from datetime import datetime
%matplotlib qt5
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


def create_bokeh_choro(ff, prop=0):
    """Creates Interactive Bokeh Choropleth for US counties transportationdata.

    Arguments:
        ff {dict} -- Dictionary containing filled dataframes

    Keyword Arguments:
        prop {int} -- Select the property for which choropleth needs to be created (default: {0})
    """
    year = 0
    # Very Important Function
    assert isinstance(prop, int)
    assert isinstance(year, int)
    assert len(ff['CA'][0].columns) > prop >= 0
    assert len(ff['CA'][0].index) > year >= 0
    try:
        # del states["HI"]
        del states["AK"]
    except:
        pass
    nyears = len(ff['CA'][0].index)
    state_xs = [states[code]["lons"] for code in states]
    state_ys = [states[code]["lats"] for code in states]
    county_xs = []
    county_ys = []
    district_name = []
    for cs in bokeh_counties.values():
        for dname in cs:
            county_xs.append([counties[code]["lons"]
                              for code in counties if counties[code]["detailed name"] == dname][0])
            county_ys.append([counties[code]["lats"]
                              for code in counties if counties[code]["detailed name"] == dname][0])
            district_name.append(dname)
    if isinstance(palette, dict):
        color_mapper = LogColorMapper(
            palette=palette[list(palette.keys())[-1]])
    else:
        color_mapper = LogColorMapper(palette=palette)
    pvalues = []

    for yx in range(nyears):
        yvalues = []
        for state in ff.keys():
            for cs in ff[state]:
                yvalues.append(cs.iloc[yx, prop])
        pvalues.append(yvalues)
    alldat = {}
    syear = ff['CA'][0].index[0]
    for ix, yy in enumerate(range(syear, syear + nyears)):
        alldat[str(yy)] = pvalues[ix]
    source = ColumnDataSource(data=dict(
        x=county_xs, y=county_ys,
        name=district_name, pvalue=pvalues[0], **alldat))
    TOOLS = "pan,wheel_zoom,reset,hover,save"
    p = figure(title=f"{ff['CA'][0].columns[prop]} across Counties", tools=TOOLS, plot_width=1200,
               plot_height=600, x_axis_location=None, y_axis_location=None)
    p.toolbar.active_scroll = "auto"
    p.toolbar.active_drag = 'auto'
    p.background_fill_color = "#B0E0E6"
    p.patches(state_xs, state_ys, fill_alpha=1.0, fill_color='#FFFFE0',
              line_color="#884444", line_width=2, line_alpha=0.3)
    p.patches('x', 'y', source=source,
              fill_color={'field': 'pvalue', 'transform': color_mapper},
              fill_alpha=0.8, line_color="white", line_width=0.3)
    hover = p.select_one(HoverTool)
    hover.point_policy = "follow_mouse"
    property = ff['CA'][0].columns[prop]
    hover.tooltips = [("County", "@name"), (property,
                                            "@pvalue"), ("(Long, Lat)", "($x, $y)")]
    output_file(f"{ff['CA'][0].columns[prop].replace(' ','')}.html",
                title="US Public Transport")
    slider = Slider(start=int(ff['CA'][0].index[0]), end=int(ff['CA'][0].index[-1]),
                    value=int(ff['CA'][0].index[0]), step=1, title="Start Year")

    def update(source=source, slider=slider, window=None):
        """ Update the map: change the bike density measure according to slider
            will be translated to JavaScript and Called in Browser """
        data = source.data
        v = cb_obj.getv('value')
        data['pvalue'] = [x for x in data[v]]
        source.trigger('change')
        # source.change.emit()
    slider.js_on_change('value', CustomJS.from_py_func(update))
    show(column(p, widgetbox(slider),))


def get_sales_data(fname='TOTALSA.csv'):
    """Returns car sales data from 1978 to 2019(provisional).

    Keyword Arguments:
        fname {str} -- Filename from which sales data needs to be pulled (default: {'TOTALSA.csv'})
    """
    sales_months = pd.read_csv(fname)
    dates = sales_months['DATE'].tolist()
    for ix, date in enumerate(dates):
        dates[ix] = datetime.strptime(date, '%Y-%m-%d')
        dates[ix] = int(dates[ix].strftime('%Y'))
    sales_months['Year'] = dates
    result = sales_months.groupby(
        'Year')['TOTALSA'].sum().to_frame().sort_index()
    result['TOTALSA'] = result['TOTALSA']
    result.rename(
        columns={'TOTALSA': 'Total Sales of Personal Vehicles (in millions)'}, inplace=True)
    return(result)


def interpolate_dataframes(ff):
    """Interploate values for missing years.

    Arguments:
        ff {dict} -- Dictionary of filled frames
    """
    assert isinstance(ff, dict)
    year_min = ff['CA'][0].index[0]
    year_max = ff['CA'][0].index[-1]
    years = list(range(year_min, year_max + 1))
    for state in ff.keys():
        for cf in ff[state]:
            for year in years:
                if year not in cf.index:
                    cf.loc[year] = cf.loc[year-1:year+1, :].sum(axis=0)
                    cf.loc[year] = (cf.loc[year] / 2).astype(np.int64)
            cf.sort_index(inplace=True)
    return(ff)


def get_car_economy(fname='car_economy.csv'):
    """Returns national car economy stats for years 1975-2017.

    Keyword Arguments:
        fname {str} -- CSV fiename from which data needs to be pulled. (default: {'car_economy.csv'})
    """
    car_eco = pd.read_csv(fname)
    car_eco = car_eco.iloc[:-1, :]
    years = car_eco['Model Year'].astype(int).tolist()
    emit = car_eco['Real-world MPG'].tolist()
    car_eco2 = pd.DataFrame(index=years, columns=[
                            'Real World Fuel Economy (mpg)'])
    car_eco2['Real World Fuel Economy (mpg)'] = emit
    car_eco2['Real World Fuel Economy (mpg)'] = car_eco2['Real World Fuel Economy (mpg)'].astype(
        int)
    car_eco2.index.name = 'Year'
    return (car_eco2)


def get_us_ridership(fname='ridership_US.csv'):
    """Returns the US public transportation from 1922-2017.

    Keyword Arguments:
        fname {str} -- CSV filename from which to pull data (default: {'ridership_US.csv'})
    """
    return pd.read_csv(fname, index_col='Year')


def combine_for_correlation(df1=get_us_ridership(), df2=get_sales_data()):
    """Takes fuel economy, ridership and car sales data and combines them for the years in which all 3 are present.
    """
    df1.index.astype(int)
    df2.index.astype(int)
    temp = pd.concat([df1, df2], axis=1)
    return temp.dropna()


def create_correlation_plot(df):
    """Create seaborn correlation plot for input data frame.

    Arguments:
        df {pd Dataframe} -- Dataframe with index as years and column1=data1 and column2=data2.
    """
    xdata = df.iloc[:, 0]
    ydata = df.iloc[:, 1]
    plt.clf
    plt.figure(figsize=(20, 18))
    sns.regplot(xdata, ydata, marker='o', data=df.index)
    plt.title(f'{df.columns[0]} vs. {df.columns[1]}', color='k')
    plt.xlabel(f'{df.columns[0]}', color='k')
    plt.ylabel(f'{df.columns[1]}', color='k')
    plt.grid(True)
    plt.xticks(color='k')
    plt.yticks(color='k')
    plt.show()
    plt.savefig(f'corr{df.columns[0][0]}v{df.columns[1][0]}.jpg')


def get_mv_deaths(fname='deaths-and-population-ra.csv'):
    """Get motor vehicle deaths from 1913-2017.

    Keyword Arguments:
        fname {str} -- File name from which data is to be pulled (default: {'deaths-and-population-ra.csv'})
    """
    df = pd.read_csv(fname)
    df2 = pd.DataFrame(index=df['Category'].astype(
        int), columns=['Deaths Due to MVs'], dtype=int)
    df2.index.name = 'Year'
    data = df.iloc[:, 1].tolist()
    df2[df2.columns[0]] = data
    return df2


# %%
start = time.time()
tp = create_city_dataframes()
end = time.time()
print(f'Time to compute dataframes: {end-start:.2f}')
# %%
tp = interpolate_dataframes(tp)
# %%
sd = tp["CA"][0]

# %%
h = next(transform_city_dataframes(tp, ttype=[0]))

# %% Plotting
get_simple_plots(tp, state='NY')

# %% Bokeh Plotting
create_bokeh_choro(tp, prop=7)

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
def graph_year_property(h, p_no=0):
    '''
    Creates bar graphs for particular year and property
    '''
    from bokeh.core.properties import value
    from bokeh.plotting import figure
    from bokeh.io import show, output_file
    from bokeh.layouts import row, column
    from bokeh.models import ColumnDataSource
    from bokeh.models.widgets import Dropdown
    from bokeh.models.callbacks import CustomJS
    output_file("bars.html")
    xlabels = []
    
    for key, value in cities.items():
        xlabels.append(key + ': ' + value[0])
    
    yr_ind = 0

    p_values = []
    for yr_ind in range(12):
        i = 0
        p_value = [0 for x in range(18)]
        for state, city_list in h.items():
            city_p = [d.get(str(col_index_names1000[p_no])) for d in city_list]
            a = array(city_p)
            col = 0
            for row in a:
                if col == 2:
                    break
                p_value[i] = row[yr_ind]
                col = col + 1
            i = i + 1
        p_values.append(p_value)
    print(p_values)
    # cs = ['C1']
    # colors = ["#e84d60", "#718dbf", "#c9d9d3"]
    # alldat = {}
    # for yx, yy in enumerate(range(12)):
    #     alldat[str(yy)]=p_values[yx]
    # data = dict(xlabels= xlabels,
    #         C1= [row[0] for row in p_values[0]],**alldat)
    # source = ColumnDataSource(data)
    p = figure(x_range=xlabels, plot_height=450, plot_width=800, title='Year', toolbar_location=None, tools="")
    p.vbar(x=xlabels, top=p_values[0], width=0.4)
    #p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.title.align = 'center'
    p.yaxis.axis_label = col_index_names1000[p_no]
    p.yaxis.axis_label_text_font_size = '12pt'
    p.xaxis.major_label_orientation = 3.14/2
    p.xaxis.major_label_text_font_size = '12pt'
    p.axis.minor_tick_line_color = 'black'
    p.outline_line_color = 'black'
    show(p)
    slider = Slider(start=0, end=9, value=0, step=1, title="Start Year")

    def update(source=source, slider=slider, window=None):
        """ Update the map: change the bike density measure according to slider
            will be translated to JavaScript and Called in Browser """
        source.data = data
        v = cb_obj.getv('value')
        data['C1'] = [x for x in data[v][0]]
        source.trigger('change')
    slider.js_on_change('value', CustomJS.from_py_func(update))
    #show(column(p, widgetbox(slider),))