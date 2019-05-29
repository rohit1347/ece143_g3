
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

#%%
file = 'NY.csv'
df = pd.read_csv(file)
df = df.iloc[7:18]
df_new = pd.read_csv('a.csv')

# df = df.iloc[0:10]
#%%
file1 = 'table21.xls'
df1 = pd.read_excel(file1, sheet_name = 0, skiprows = 9)
df1 = df1.iloc[0:5]  
df1 = df1.rename(columns = {'Unnamed: 0':'Years','Unnamed: 10':'sum1','Unnamed: 15':'sum2'})
df1['Total'] = df1['sum1'].values*1000 + df1['sum2'].values*1000
df1_new = pd.read_csv('b.csv')

#%%
# Plot in plotly

import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

countries = ['NY', 'Hong Kong']
# fill_colors = ['#66c2a5', '#fc8d62']

x = list(df_new['Year'].values)
y_1 = list(np.array(['HK','HK','HK','HK','HK','HK','HK','HK','HK','HK']))
y_2 = list(np.array(['NY','NY','NY','NY','NY','NY','NY','NY','NY','NY']))
z_1 = list(df_new['Unlinked Passenger Trips'].values/1000000)
z_2 = list(df1_new['Total'].values/1000000)


data1 = [(dict(type = 'scatter3d', x=x,y= y_1, z = z_1, mode = 'lines',name = '',surfaceaxis = 1,surfacecolor = '#66c2a5', )),(dict(type = 'scatter3d', x=x,y= y_2, z = z_2, mode = 'lines',name = '',surfaceaxis = 1,surfacecolor = '#fc8d62'))]
# trace1 = go.Scatter3d(x=x_1,y= z,mode = 'lines',name = 'Passenger Trips')
# data1 = [trace0]
    
# data.append(dict(
#     type='scatter3d',
#     mode='lines',
#     x=years + years[::-1] + [years[0]],  # year loop: in incr. order then in decr. order then years[0]
#     y=country_coords * 2 + [country_coords[0]],
#     z=pop + zeros + [pop[0]],
#     name='',
#     surfaceaxis=1, # add a surface axis ('1' refers to axes[1] i.e. the y-axis)
#     surfacecolor=fill_color,
#     line=dict(
#         color='black',
#         width=4
#     ),
# ))

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
        borderwidth=1
    ),
    title = 'Ridership Comparison',
    showlegend=False,
    scene=dict(
        xaxis=dict(title='Years', tickmode='linear',ticks='outside',tickcolor='#000'),
        yaxis=dict(title='Cities'),
        zaxis=dict(title='Unlinked Passenger Trips',tickmode='linear',ticks='outside',tick0=3000,dtick=500,tickcolor='#000'),
        camera=dict(
            eye=dict(x=-1.7, y=-1.7, z=0.5)
        )
    )
)

fig = dict(data=data1, layout=layout)

# IPython notebook
# py.iplot(fig, filename='filled-3d-lines')

plotly.offline.plot(fig, filename='3dplot_rajat.html')

#%%

import plotly
import pandas as pd

plotly.offline.init_notebook_mode(connected=True)

# The datasets' url. Thanks Jennifer Bryan!
url_csv = 'http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt'

df = pd.read_csv(url_csv, sep='\t')
df.head()

countries = ['China', 'India']
fill_colors = ['#66c2a5', '#fc8d62']
gf = df.groupby('country')

data = []

for country, fill_color in zip(countries[::-1], fill_colors):
    group = gf.get_group(country)
    years = group['year'].tolist()
    length = len(years)
    country_coords = [country] * length
    pop = group['pop'].tolist()
    zeros = [0] * length
    
    data.append(dict(
        type='scatter3d',
        mode='lines',
        x=years + years[::-1] + [years[0]],  # year loop: in incr. order then in decr. order then years[0]
        y=country_coords * 2 + [country_coords[0]],
        z=pop + zeros + [pop[0]],
        name='',
        surfaceaxis=1, # add a surface axis ('1' refers to axes[1] i.e. the y-axis)
        surfacecolor=fill_color,
        line=dict(
            color='black',
            width=4
        ),
    ))

layout = dict(
    title='Population from 1957 to 2007 [Gapminder]',
    showlegend=False,
    scene=dict(
        xaxis=dict(title=''),
        yaxis=dict(title=''),
        zaxis=dict(title=''),
        camera=dict(
            eye=dict(x=-1.7, y=-1.7, z=0.5)
        )
    )
)

fig = dict(data=data, layout=layout)

# IPython notebook
# py.iplot(fig, filename='filled-3d-lines')

plotly.offline.iplot(fig, filename='filled-3d-lines')

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

file = 'NY.csv'
df = pd.read_csv(file)
df = df.iloc[7:18]

# df = df.iloc[0:10]
#%%
file1 = 'table21.xls'
df1 = pd.read_excel(file1, sheet_name = 0, skiprows = 9)
df1 = df1.iloc[0:5]  
df1 = df1.rename(columns = {'Unnamed: 0':'Years','Unnamed: 10':'sum1','Unnamed: 15':'sum2'})
df1['Total'] = df1['sum1'].values*1000 + df1['sum2'].values*1000

#%%
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

