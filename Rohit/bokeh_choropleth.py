# %%
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.us_states import data as states
from bokeh.sampledata.unemployment import data as unemployment
from ProjectWorkspace import *
from import_xls import create_city_dataframes
try:
    # del states["HI"]
    del states["AK"]
except:
    pass

# %%
EXCLUDED = ("ak", "pr", "gu", "vi", "mp", "as")
IN = tuple(bokeh_counties.keys())

state_xs = [states[code]["lons"] for code in states]
state_ys = [states[code]["lats"] for code in states]
county_xs = [counties[code]["lons"]
             for code in counties if counties[code]["state"] not in EXCLUDED]
county_ys = [counties[code]["lats"]
             for code in counties if counties[code]["state"] not in EXCLUDED]

# %%
county_xs = []
county_ys = []
for cs in bokeh_counties.values():
    for dname in cs:
        county_xs.append([counties[code]["lons"]
                          for code in counties if counties[code]["detailed name"] == dname][0])
        county_ys.append([counties[code]["lats"]
                          for code in counties if counties[code]["detailed name"] == dname][0])

# %%
county_xs = []
county_ys = []
for state in states.keys():
    if state in bokeh_counties_xs.keys():
        county_xs.append(bokeh_counties_xs[state])
    else:
        county_xs.append([])
    if state in bokeh_counties_ys.keys():
        county_ys.append(bokeh_counties_ys[state])
    else:
        county_ys.append([])
# %%
county_xs = []
county_ys = []

for state in states.keys():
    if state in bokeh_counties_xs.keys() and state in bokeh_counties_ys.keys():
        for ix in range(len(bokeh_counties_xs[state])):
            county_xs.append(bokeh_counties_xs[state][ix])
            county_ys.append(bokeh_counties_ys[state][ix])

# %%
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]
county_colors = []
# %%
ff = create_city_dataframes()
# %%
for state in states.keys():
    if state in ff.keys():
        for cs in ff[state]:
            county_colors.append(colors[int(cs.iloc[0, 1]) % len(colors)])
# %%
# Goes through each county out of 3114+x(in excluded states)
for county_id in counties:
    if counties[county_id]["state"] in EXCLUDED:
        continue
    try:
        rate = unemployment[county_id]
        idx = int(rate/len(colors))
        county_colors.append(colors[idx])
    except KeyError:
        county_colors.append("black")
print(len(county_colors))
# %%
p = figure(title="US Unemployment 2009", toolbar_location="left",
           plot_width=1800, plot_height=700)

p.patches(county_xs, county_ys,
          fill_color=county_colors, fill_alpha=0.7,
          line_color="white", line_width=0.5)

p.patches(state_xs, state_ys, fill_alpha=0.0,
          line_color="#884444", line_width=2, line_alpha=0.3)

output_file("choropleth.html", title="US Counties")

show(p)


# %%
