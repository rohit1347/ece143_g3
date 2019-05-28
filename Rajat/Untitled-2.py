#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../ece143_g3/Rajat'))
	print(os.getcwd())
except:
	pass

#%%
import camelot
import pandas as pd
import matplotlib.pyplot as plt


#%%
tables = camelot.read_pdf('2018-APTA-Fact-Book.pdf', pages = '28,29')     
tables.export('apta2018.csv', f='csv', compress=False)


#%%
table = pd.read_csv('apta2018-page-29-table-1.csv')
print(table)


#%%
cities = table.iloc[0].values[0]
cities = cities.split(" \n")


#%%
ppl_2010 = table.iloc[0].values[1]
ppl_2010 = ppl_2010.split(" \n")


#%%
trip_2016 = table.iloc[0].values[2]
trip_2016 = trip_2016.split(" \n")


#%%
rpc_2016 = table.iloc[0].values[3]
rpc_2016 = rpc_2016.split(" \n")


#%%
rpc_2016 = table.iloc[0].values[3]
rpc_2016 = rpc_2016.split(" \n")
rpc_2016 = rpc_2016[1:5]


#%%
plt.barh(cities,trip_2016)
plt.xlabel('Ridership per capita', fontsize=5)
# plt.ylabel('No of Movies', fontsize=5)
# plt.xticks(index, label, fontsize=5, rotation=30)
plt.title('2016')
plt.show()


#%%
rpc_2016 = table.iloc[0].values[3]
x_1 = rpc_2016.split(" \n")

trip_2016 = table.iloc[0].values[2]
y_1 = trip_2016.split(" \n")

rpc_2016 = table.iloc[0].values[3]
y_2 = rpc_2016.split(" \n")

import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

# plotly.offline.iplot({
#     "data" : [go.Bar(x=a_1,y= b_1)],
#     "layout": go.Layout(title="Ridership")
# })

trace1 = go.Bar(
    x=x_1,
    y=y_1,
    text=y_1,
    textposition = 'auto',
    name='Buses',
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=0.5),
        ),
    orientation = 'h',
    opacity=0.6
)

# trace2 = go.Bar(
#     x=x_1,
#     y=y_2,
#     text=y_2,
#     textposition = 'auto',
#     name='Railways',
#     marker=dict(
#         color='rgb(58,200,225)',
#         line=dict(
#             color='rgb(8,48,107)',
#             width=0.5),
#         ),
#     orientation = 'h',
#     opacity=0.6
# )

data = [trace1]

layout = go.Layout(
    xaxis=dict(tickangle=-45),
    barmode='group',
    title = 'Ridership'
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig, filename='angled-text-bar')


#%%
import plotly
import plotly.graph_objs as go

data = [go.Bar(
            x=x_1,
            y=y_2,
            orientation = 'h'
)]

plotly.offline.iplot(data, filename='horizontal-bar')


#%%



