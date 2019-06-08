ECE143 Group 3 Project
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

1. bokeh
2. bokeh sampledata
3. matplotlib 
4. seaborn
5. plotly
6. numpy

For the choropleth plots, we are using a [native bokeh choropleth implementation](http://bokeh.pydata.org/en/0.11.1/docs/gallery/choropleth.html), for which bokeh sampledata needs to be installed.
Please install it by typing in terminal using: `bokeh sampledata`
## Code Organization 
### Instructions
1. Please use branch **final**. Select branch using `git checkout final`.
2. `
Root > Master
`
The folder `Master` contains all scripts and some dataset files.
3. The repo contains dataset files totalling **9.73 MB**.
4. Instead of using the provided Jupyter notebook to view plots, we recommend using the links provided in the section below to view all the plots. Mitigates the need to compile code to view plots.
### Running the Code
1. `import_xls.py` contains `apta_utils()` class to obtain data from APTA sources, and visualization *(correlations, choropleths, fuel saved)* for the data.
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