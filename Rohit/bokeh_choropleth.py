# %%
from ProjectWorkspace import *

import time
import os
import collections
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import string
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.us_states import data as states
from bokeh.palettes import Greys256 as palette
from bokeh.layouts import row
from bokeh.layouts import column, row, widgetbox
from bokeh.models import CustomJS, Slider, Toggle
from bokeh.models.callbacks import CustomJS
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, HoverTool, LogColorMapper
from datetime import datetime
%matplotlib qt5
plt.style.use('fivethirtyeight')
# %%


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
    for ix, yy in enumerate(range(syear, syear+nyears)):
        alldat[str(yy)] = pvalues[ix]
    source_visible = ColumnDataSource(data=dict(
        x=county_xs, y=county_ys,
        name=district_name, pvalue=pvalues[0]))
    source_available = ColumnDataSource(data=alldat)
    print(source_available.data)
    TOOLS = "pan,wheel_zoom,reset,hover,save"
    p = figure(title=f"{ff['CA'][0].columns[prop]} across Counties", tools=TOOLS, plot_width=1200,
               plot_height=600, x_axis_location=None, y_axis_location=None)
    p.toolbar.active_scroll = "auto"
    p.toolbar.active_drag = 'auto'
    p.background_fill_color = "#B0E0E6"
    p.patches(state_xs, state_ys, fill_alpha=1.0, fill_color='#FFFFE0',
              line_color="#884444", line_width=2, line_alpha=0.3)
    p.patches('x', 'y', source=source_visible,
              fill_color={'field': 'pvalue', 'transform': color_mapper},
              fill_alpha=0.8, line_color="white", line_width=0.3)
    hover = p.select_one(HoverTool)
    hover.point_policy = "follow_mouse"
    property = ff['CA'][0].columns[prop]
    hover.tooltips = [("County", "@name"), (property,
                                            "@pvalue"), ("(Long, Lat)", "($x, $y)")]
    output_file(f"{ff['CA'][0].columns[prop].replace(' ','')}.html",
                title="US Public Transport")
    slider = Slider(start=syear, end=syear+nyears,
                    value=syear, step=1, title="Year")
    # slider.callback = CustomJS(
    #     args=dict(source_visible=source_visible,
    #               source_available=source_available), code="""
    #     var seledted_year = cb_obj.value;
    #     // Get the data from the data sources
    #     var data_visible = source_visible.data;
    #     var data_available = source_available.data;
    #     // Change y-axis data according to the selected value
    #     data_visible.y = data_available[selected_year];
    #     // Update the plot
    #     source_visible.change.emit();
    # """)
    # show(column(p, widgetbox(slider),))

    def update(source=source_visible, slider=slider, window=None):
        """ Update the map: change the bike density measure according to slider
            will be translated to JavaScript and Called in Browser """
        data = source_available.data
        v = cb_obj.getv('value')
        data['pvalue'] = [x for x in data[v]]
        source.trigger('change')
        # source.change.emit()
    slider.js_on_change('value', CustomJS.from_py_func(update))
    show(column(p, widgetbox(slider),))


# %%
create_bokeh_choro(h, prop=2)


# %%
