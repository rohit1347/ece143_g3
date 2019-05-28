
#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

file = '2019-APTA-Fact-Book-Appendix-A.xlsx'
df = pd.read_excel(file, sheet_name= '3', skiprows = 4)
df = df.iloc[19:42]  # For years 1995- 2017
df = df.rename(columns = {'Unnamed: 4':'Bus','Trolleybus (a)':'TrolleyBus * (100)','Unnamed: 13':'Region Railroad','Unnamed: 17':'Surface Rail * (10)', 'Ferryboat':'FerryBoat * (10)'})

#%%
df['Bus'] = pd.to_numeric(df.Bus.astype(str).str.replace(',',''), errors='coerce').fillna(float(20976)).astype(int)
## Need to change fillna value every sheet

#%%
x_1 = list(df['Year'].values)
y_1 = list(df['TrolleyBus * (100)'].values*100)
y_2 = list(df['Region Railroad'].values)
y_3 = list(df['Surface Rail * (10)'].values*10)
y_4 = list(df['FerryBoat * (10)'].values*10)
y_5 = list(df['Bus'].values)
y_6 = list(df['Heavy Rail'].values)

import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

trace0 = go.Scatter(x=x_1,y= y_1,mode = 'lines+markers',name = 'TrolleyBus *100')
trace1 = go.Scatter(x=x_1,y= y_2,mode = 'lines+markers',name = 'Region Railroad')
trace2 = go.Scatter(x=x_1,y= y_3,mode = 'lines+markers',name = 'Surface Rail * 10')
trace3 = go.Scatter(x=x_1,y= y_4,mode = 'lines+markers',name = 'FerryBoat * 10')
trace4 = go.Scatter(x=x_1,y= y_5,mode = 'lines+markers',name = 'Bus')
trace5 = go.Scatter(x=x_1,y= y_6,mode = 'lines+markers',name = 'Heavy Rail')

data = [trace0, trace1, trace2, trace3, trace4, trace5]

# Edit the layout
layout = go.Layout(
    legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        # layout = dict(title = 'Unlinked Passenger Trips by Mode across U.S.',
        #       xaxis = dict(title = 'Years'),
        #       yaxis = dict(title = 'Unlinked Passenger Trips by Mode (in millions)'),
        #       ),
        font=dict(
            family='sans-serif',
            size=12,
            color='#000'
        ),
        bgcolor='#E2E2E2',
        bordercolor='#FFFFFF',
        borderwidth=2
    ),
    title = 'Passenger Miles by Mode across U.S.',
    xaxis = dict(title = 'Years'),
    yaxis = dict(title = 'Passenger Miles by Mode (in millions)')
)


fig = go.Figure(data=data, layout=layout)
# plotly.offline.iplot(fig)
plotly.offline.plot(fig)