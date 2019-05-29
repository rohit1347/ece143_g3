#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

file = '2019-APTA-Fact-Book-Appendix-A.xlsx'
df = pd.read_excel(file, sheet_name= '1', skiprows = 4)
df = df.iloc[10:106]  # For years 1922- 2017
df = df.rename(columns = {'Unnamed: 4':'Bus','Unnamed: 17':'Surface Rail', 'Ferryboat':'FerryBoat * (100)'})

#%%
df = df.rename(columns = {'Unnamed: 4':'Bus','Trolleybus (a)':'TrolleyBus * (10)','Unnamed: 13':'Region Railroad * (10)','Unnamed: 17':'Surface Rail * (10)', 'Ferryboat':'FerryBoat * (100)'})
df['Bus'] = pd.to_numeric(df.Bus.astype(str).str.replace(',',''), errors='coerce').fillna(float(5413)).astype(int)

#%%
df_1= pd.DataFrame({
    'Bus': list(df['Bus'].values),
    'Heavy Rail': list(df['Heavy Rail'].values),
    'Light Rail' : list(df['Surface Rail'].values)
}, index = df['Year'].values
)
#%%
# Using Matplotlib

df_1.plot.area()
plt.xlabel('Years')
plt.ylabel('Unlinked Trips (in millions)')
plt.title('Changing transit ridership for major modes of public transport')
ax = plt.gca()
ax.grid(which='major', axis='y', linestyle='--', linewidth = '0.5')

plt.tight_layout()
plt.show()

#%%
# Using Plotly

import plotly
import plotly.graph_objs as go


x_1 = list(df['Year'].values)
y_1 = list(df['Bus'].values)
y_2 = list(df['Heavy Rail'].values)
y_3 = list(df['Surface Rail'].values)

#%%
plotly.offline.init_notebook_mode(connected=True)

trace0 = dict(x=x_1,y= y_1,hoverinfo='x+y',mode='lines',line=dict(width=0.5,color='rgb(204, 102, 10)'),stackgroup='one',name = 'Bus')
trace1 = dict(x=x_1,y=y_2, hoverinfo='x+y',mode='lines',line=dict(width=0.5,color='rgb(102, 255, 102)'),stackgroup='one',name = 'Heavy Rail')
trace2 = dict(x=x_1,y=y_3, hoverinfo='x+y',mode='lines',line=dict(width=0.5,color='rgb(51, 153, 255)'),stackgroup='one',name = 'Light Rail')

data = [trace0, trace1, trace2]

layout = go.Layout(
    legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        font=dict(
            family='sans-serif',
            size=12,
            color='#000'
        ),
        bgcolor='#E2E2E2',
        bordercolor='#FFFFFF',
        borderwidth=2
    ),
    title = 'Ridership by Mode across U.S.',
    xaxis = dict(title = 'Years'),
    yaxis = dict(title = 'Unlinked Trips (in millions)')
)

fig = dict(data=data, layout = layout)
plotly.offline.plot(fig)

#%%
df_2 = pd.DataFrame({
    'Year':list(df['Year'].values),
    'Total Ridership (in millions)':list(df['All Modes Reported Total (Parts A and B)'].values)
})

#df_2.to_csv('ridership_US.csv')
