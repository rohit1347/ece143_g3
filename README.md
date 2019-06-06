ECE143 Group 3 Project - Please use branch **final**
<img src="w_BusTrolley_SantaFe.jpg" height="250" width="1550" alt="SDMTS">

# Effectiveness of Public Transportation

Spring 2019 @ UCSD

## Description
Public transportation is an economical and eco-friendly way to travel. More cities should be investing in public transport infrastructure.

This project tries to analyse:

* Annual ridership trends of public transportation.
* Fuel savings due to usage of public transport.
* Correlation between public transport ridership and road accidents.
* Correlation between public transport ridership and car sales.
* US county level public transport vehicle availability.

## Requirements/Dependencies
```
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
from bokeh.palettes import Reds as palette
from bokeh.layouts import column, row, widgetbox
from bokeh.models import CustomJS, Slider, Toggle
from bokeh.models.callbacks import CustomJS
from bokeh.models import ColumnDataSource, HoverTool, LogColorMapper
from datetime import datetime
import plotly
import plotly.tools as tls
import matplotlib.lines as mlines
```

## Code Organization
1. `import_xls.py` in the folder `Master` contains `apta_utils()` class to obtain data from APTA sources, and visualization *(correlations, choropleths, fuel saved)* for the data.
2. `graph_county_properties.py` gives a bar graph of all counties for the required property.

## Plots
### US Annual Trends
* [Ridership](http://acsweb.ucsd.edu/~rokumar/ridership_from_1922_rajat.html)
* [Revenue Miles](http://acsweb.ucsd.edu/~rokumar/miles_rajat_final.html)
* [Employees](http://acsweb.ucsd.edu/~rokumar/employee_compensation_us_rajat.html)
* [Fuel Savings](http://acsweb.ucsd.edu/~rokumar/employee_compensation_us_rajat.html)
#### Correlations
* [Ridership vs Motor Vehicle Accident Deaths](http://acsweb.ucsd.edu/~rokumar/corrTvD.jpg)
* [Ridership vs Personal Motor Vehicle Sales](http://acsweb.ucsd.edu/~rokumar/corrTvT.jpg)
### US County Trends
* [Vehicles in Service Overview](http://acsweb.ucsd.edu/~rokumar/VehiclesinService(per1000persons).html)
* [Vehicles in Service](http://acsweb.ucsd.edu/~rokumar/vehicles_in_service.html)
* [Unlinked Trips](http://acsweb.ucsd.edu/~rokumar/unlinked_trips.html)
#### Correlations
* [Ridership vs Traffic Accidents](http://acsweb.ucsd.edu/~rokumar/corrAvT.jpg)
* [Ridership vs Transportation Electricity Consumption](http://acsweb.ucsd.edu/~rokumar/corrAvE.jpg)
### New York vs Hong Kong
* [NY vs HK Ridership](http://acsweb.ucsd.edu/~rokumar/ny_vs_hk_ridership.html)
* [NY vs HK Transportation Accidents](http://acsweb.ucsd.edu/~rokumar/nyvshk_traffic.html)

## Project by:
* Himanshu Gupta

* Mingkun Yin

* Rajat Sethi

+ Rohit Kumar

[Project Presentation](https://drive.google.com/a/eng.ucsd.edu/file/d/1Bk8idTlstwerVcrGewY6Z3Pjgp48-w7_/view?usp=sharing)
---
[Project Proposal](https://drive.google.com/a/eng.ucsd.edu/file/d/1tMI7DCHLvUNBs6RAQkT9LqQ2Diw3NZZU/view?usp=sharing)
---
