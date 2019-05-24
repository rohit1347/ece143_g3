# %%
import plotly.graph_objs as go
import numpy as np
from bokeh.plotting import *
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.us_states import data as states
from bokeh.sampledata.unemployment import data as unemployment
import plotly.plotly as py
import plotly
import plotly.figure_factory as ff

import pandas as pd
# %%
us_states = states
del states["HI"]
del states["AK"]

EXCLUDED = ("ak", "hi", "pr", "gu", "vi", "mp", "as")

state_xs = [states[code]["lons"] for code in states]
state_ys = [states[code]["lats"] for code in states]

county_xs = [counties[code]["lons"]
             for code in counties if counties[code]["state"] not in EXCLUDED]
county_ys = [counties[code]["lats"]
             for code in counties if counties[code]["state"] not in EXCLUDED]

colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

county_colors = []
for county_id in counties:
    if counties[county_id]["state"] in EXCLUDED:
        continue
    try:
        rate = unemployment[county_id]
        idx = int(rate/6)
        county_colors.append(colors[idx])
    except KeyError:
        county_colors.append("black")

p = figure(title="US Unemployment 2009", toolbar_location="left",
           plot_width=1100, plot_height=700)

p.patches(county_xs, county_ys,
          fill_color=county_colors, fill_alpha=0.7,
          line_color="white", line_width=0.5)

p.patches(state_xs, state_ys, fill_alpha=0.0,
          line_color="#884444", line_width=2, line_alpha=0.3)

output_file("choropleth.html", title="choropleth.py example")

show(p)


# %%

# separate latitude and longitude points for the borders
#   of the states.
state_xs = [us_states[code]["lons"] for code in us_states]
state_ys = [us_states[code]["lats"] for code in us_states]

# init figure
p = figure(title="Plotting Points Example: The 5 Largest Cities in Texas",
           toolbar_location="left", plot_width=1100, plot_height=700)

# Draw state lines
p.patches(state_xs, state_ys, fill_alpha=0.0,
          line_color="#884444", line_width=1.5)

#  Latitude and Longitude of 5 Cities
# ------------------------------------
# Austin, TX -------30.26° N, 97.74° W
# Dallas, TX -------32.77° N, 96.79° W
# Fort Worth, TX ---32.75° N, 97.33° W
# Houston, TX ------29.76° N, 95.36° W
# San Antonio, TX --29.42° N, 98.49° W

# Now group these values together into a lists of x (longitude) and y (latitude)
x = [-97.7431, -96.79, -97.33, -95.36, -98.49]
y = [30.26, 32.77, 32.75, 29.76, 29.42]

# The scatter markers
p.circle(x, y, size=8, color='navy', alpha=1)

# output to static HTML file
output_file("texas.html")

# show results
show(p)

# %%
plotly.tools.set_credentials_file(
    username='rohit1347', api_key='wP0wJffd8666ba1iS6CT')
plotly.tools.set_config_file(world_readable=True, sharing='public')
df_sample = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv')
df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(
    lambda x: str(x).zfill(2))
df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(
    lambda x: str(x).zfill(3))
df_sample['FIPS'] = df_sample['State FIPS Code'] + \
    df_sample['County FIPS Code']

colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
              "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
              "#08519c", "#0b4083", "#08306b"]
endpts = list(np.linspace(1, 12, len(colorscale) - 1))
fips = df_sample['FIPS'].tolist()
values = df_sample['Unemployment Rate (%)'].tolist()

fig = ff.create_choropleth(
    fips=fips, values=values,
    binning_endpoints=endpts,
    colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='USA by Unemployment %',
    legend_title='% unemployed'
)
py.iplot(fig, filename='choropleth_full_usa')
# %%
plotly.tools.set_credentials_file(
    username='rohit1347', api_key='wP0wJffd8666ba1iS6CT')
plotly.tools.set_config_file(world_readable=False, sharing='public')
# %%

# min year in your dataset
year = 1998

# your color-scale
scl = [[0.0, '#ffffff'], [0.2, '#b4a8ce'], [0.4, '#8573a9'],
       [0.6, '#7159a3'], [0.8, '#5732a1'], [1.0, '#2c0579']]  # purples

data_slider = []
for year in df['years'].unique():
    df_segmented = df[(df['years'] == year)]

    for col in df_segmented.columns:
        df_segmented[col] = df_segmented[col].astype(str)

    data_each_yr = dict(
        type='choropleth',
        locations=df_segmented['state'],
        z=df_segmented['sightings'].astype(float),
        locationmode='USA-states',
        colorscale=scl,
        colorbar={'title': '# Sightings'})

    data_slider.append(data_each_yr)

steps = []
for i in range(len(data_slider)):
    step = dict(method='restyle',
                args=['visible', [False] * len(data_slider)],
                label='Year {}'.format(i + 1998))
    step['args'][1][i] = True
    steps.append(step)

sliders = [dict(active=0, pad={"t": 1}, steps=steps)]

layout = dict(title='UFO Sightings by State Since 1998', geo=dict(scope='usa',
                                                                  projection={'type': 'albers usa'}),
              sliders=sliders)

fig = dict(data=data_slider, layout=layout)
periscope.plotly(fig)
