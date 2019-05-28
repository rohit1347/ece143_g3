
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt5

file = '2019-APTA-Fact-Book-Appendix-A.xlsx'
df = pd.read_excel(file, sheet_name= '1', skiprows = 4)
df = df.iloc[83:106]  # For years 1995- 2017
df = df.rename(columns = {'Unnamed: 4':'Bus','Trolleybus (a)':'TrolleyBus * (10)','Unnamed: 13':'Region Railroad * (10)','Unnamed: 17':'Surface Rail * (10)', 'Ferryboat':'FerryBoat * (100)'})

# #%%
# # df.groupby('').plot(x='year', y='Bus', ax=ax, legend=True)

# df.plot(x = 'Year', y=['Bus','TrolleyBus * (10)','Region Railroad * (10)','Heavy Rail','Surface Rail * (10)','FerryBoat * (100)'], 
# legend = True , figsize = (7,7), linewidth = 2.5)
# plt.ylabel('Ridership (in millions)')
# plt.xlabel('Years')
# plt.title('Ridership change across U.S.')
# plt.grid(color='r', linestyle='--', linewidth=0.1)
# plt.tight_layout()
# plt.show()


#%%

df['Bus'] = pd.to_numeric(df.Bus.astype(str).str.replace(',',''), errors='coerce').fillna(float(5413)).astype(int)

x_1 = list(df['Year'].values)
y_1 = list(df['TrolleyBus * (10)'].values*10)
y_2 = list(df['Region Railroad * (10)'].values*10)
y_3 = list(df['Surface Rail * (10)'].values*10)
y_4 = list(df['FerryBoat * (100)'].values*100)
y_5 = list(df['Bus'].values)
y_6 = list(df['Heavy Rail'].values)

import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

trace0 = go.Scatter(x=x_1,y= y_1,mode = 'lines+markers',name = 'TrolleyBus *10')
trace1 = go.Scatter(x=x_1,y= y_2,mode = 'lines+markers',name = 'Region Railroad * 10')
trace2 = go.Scatter(x=x_1,y= y_3,mode = 'lines+markers',name = 'Surface Rail * 10')
trace3 = go.Scatter(x=x_1,y= y_4,mode = 'lines+markers',name = 'FerryBoat * 100')
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
    title = 'Unlinked Passenger Trips by Mode across U.S.',
    xaxis = dict(title = 'Years'),
    yaxis = dict(title = 'Unlinked Passenger Trips by Mode (in millions)')
)


fig = go.Figure(data=data, layout=layout)
# plotly.offline.iplot(fig)
plotly.offline.plot(fig)
