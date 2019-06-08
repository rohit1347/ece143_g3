
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib qt5

file2 = '2019-APTA-Fact-Book-Appendix-A.xlsx'

def plot_unlinked_trips_us(file2):
    """
    Arguments:
    file {'2019-APTA-Fact-Book-Appendix-A.xlsx'}   
    
    Arguments:
        Returns the number of unlinked trips in public transport in US over the years plot
    """

    assert isinstance(file2,str)
    df = pd.read_excel(file2, sheet_name= '1', skiprows = 4)
    df = df.iloc[10:106]  # For years 1922- 2017
    df = df.rename(columns = {'Unnamed: 4':'Bus','Trolleybus (a)':'TrolleyBus','Unnamed: 13':'Region_Railroad','Unnamed: 17':'Surface Rail', 'Ferryboat':'FerryBoat'})
    df['TrolleyBus'] = pd.to_numeric(df.TrolleyBus.astype(str).str.replace('---','0'),errors = 'coerce').astype(int)
    df['Region_Railroad'] = pd.to_numeric(df.Region_Railroad.astype(str).str.replace('---','0'),errors = 'coerce').astype(int)
    df['FerryBoat'] = pd.to_numeric(df.FerryBoat.astype(str).str.replace('---','0'),errors = 'coerce').astype(int)
    ## Clean the Bus column
    df['Bus'] = pd.to_numeric(df.Bus.astype(str).str.replace(',',''), errors='coerce').fillna(float(5413)).astype(int)

    x_1 = list(df['Year'].values)
    y_1 = list(df['TrolleyBus'].values)
    y_2 = list(df['Region_Railroad'].values)
    y_3 = list(df['Surface Rail'].values)
    y_4 = list(df['FerryBoat'].values)
    y_5 = list(df['Bus'].values)
    y_6 = list(df['Heavy Rail'].values)

    import plotly
    import plotly.graph_objs as go

    plotly.offline.init_notebook_mode(connected=True)

    trace0 = go.Scatter(x=x_1,y= y_1,yaxis = 'y2',mode = 'lines+markers',name = 'TrolleyBus (*)')
    trace1 = go.Scatter(x=x_1,y= y_2,yaxis = 'y2',mode = 'lines+markers',name = 'Region Railroad (*)')
    trace2 = go.Scatter(x=x_1,y= y_3,yaxis = 'y2',mode = 'lines+markers',name = 'Surface Rail (*)')
    trace3 = go.Scatter(x=x_1,y= y_4,yaxis = 'y2',mode = 'lines+markers',name = 'FerryBoat (*)')
    trace4 = go.Scatter(x=x_1,y= y_5,mode = 'lines+markers',name = 'Bus')
    trace5 = go.Scatter(x=x_1,y= y_6,mode = 'lines+markers',name = 'Heavy Rail')

    data = [trace0, trace1, trace2, trace3, trace4, trace5]

    # Edit the layout
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
        title = 'Unlinked Passenger Trips by Mode across U.S.',
        xaxis = dict(title = 'Years'),
        yaxis = dict(title = 'Unlinked Passenger Trips (in millions)'),
        yaxis2 = dict(title = 'Unlinked Passenger Trips (in millions)', overlaying='y',side='right')
    )


    fig = go.Figure(data=data, layout=layout)
    # plotly.offline.iplot(fig)
    return plotly.offline.plot(fig)
