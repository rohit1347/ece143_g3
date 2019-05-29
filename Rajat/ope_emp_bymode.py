
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt5

file = '2019-APTA-Fact-Book-Appendix-A.xlsx'
df = pd.read_excel(file, sheet_name= '18', skiprows = 4)
# df['Year']
df = df.iloc[12:35]  # For years 1995- 2017
df = df.rename(columns = {'Total Roadway Modes Reported':'Roadway employees','Total Fixed- Guideway Modes Reported (e)':'Railway + Other misc. employees','All Modes Reported Total (Parts A and B)':'Total employees'})

#%%
index = df['Year'].values
df_2 = pd.DataFrame({'Roadway_emp': list(df['Roadway employees'].values),
                'Railway + misc._emp': list(df['Railway + Other misc. employees'].values),
                    }, index=index)
df_2.plot.barh(stacked=True, width = 1, alpha = 0.5)
plt.xlabel('Number of Employees')
plt.ylabel('Years')
plt.title('Public Transport Employees')
ax = plt.gca()
ax.grid(which='major', axis= 'both', linestyle='--', linewidth = '0.7')

plt.tight_layout()
plt.show()


#%%
x_1 = list(df['Year'].values)
y_1 = list(df['Roadway employees'].values)
y_2 = list(df['Railway + Other misc. employees'].values)


import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

trace0 = go.Bar(x=x_1,y= y_1,name = 'Roadway employees')
trace1 = go.Bar(x=x_1,y= y_2,name = 'Railway + Other misc. employees')

data = [trace0, trace1]

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
    title = 'Number of Public Transport Employees by Mode across U.S.',
    xaxis = dict(title = 'Years'),
    yaxis = dict(title = 'Number of employees')
)

fig = go.Figure(data=data, layout=layout)
# plotly.offline.iplot(fig)
plotly.offline.plot(fig)
