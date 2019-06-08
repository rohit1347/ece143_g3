#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
## Area plot

file2 = '2019-APTA-Fact-Book-Appendix-A.xlsx'

def plot_ridership_us(file2):
    """
    
    Arguments:
    file {'2019-APTA-Fact-Book-Appendix-A.xlsx'}  
    
    Returns:
        Returns the public transport ridership change in US over the years plot 
    """
    assert isinstance(file2,str)
    df = pd.read_excel(file2, sheet_name= '1', skiprows = 4)
    df = df.iloc[10:106]  # For years 1922- 2017
    ## Renaming dataframe columns
    df = df.rename(columns = {'Unnamed: 4':'Bus','Trolleybus (a)':'TrolleyBus * (10)','Unnamed: 13':'Region Railroad * (10)','Unnamed: 17':'Surface Rail * (10)', 'Ferryboat':'FerryBoat * (100)'})

    df['TrolleyBus * (10)'] = df['TrolleyBus * (10)'].values*10
    df['Region Railroad * (10)'] = df['Region Railroad * (10)'].values*10 
    df['Surface Rail * (10)'] = df['Surface Rail * (10)'].values*10 
    df['FerryBoat * (100)'] = df['FerryBoat * (100)'].values*100
    ##Cleaning Bus column
    df['Bus'] = pd.to_numeric(df.Bus.astype(str).str.replace(',',''), errors='coerce').fillna(float(5413)).astype(int)

    #%%
    df_1= pd.DataFrame({
        'Bus': list(df['Bus'].values),
        'Heavy Rail': list(df['Heavy Rail'].values),
        'Light Rail' : list(df['Surface Rail * (10)'].values/10)
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
    y_3 = list(df['Surface Rail * (10)'].values)

    #%%
    plotly.offline.init_notebook_mode(connected=True)

    trace0 = dict(x=x_1,y= y_1,hoverinfo='x+y',mode='lines',line=dict(width=0.5,color='rgb(204, 102, 10)'),stackgroup='one',name = 'Bus')
    trace1 = dict(x=x_1,y=y_2, hoverinfo='x+y',mode='lines',line=dict(width=0.5,color='rgb(102, 255, 102)'),stackgroup='one',name = 'Heavy Rail')
    trace2 = dict(x=x_1,y=y_3, hoverinfo='x+y',mode='lines',line=dict(width=0.5,color='rgb(51, 153, 255)'),stackgroup='one',name = 'Light Rail')

    data = [trace0, trace1, trace2]

    layout = dict(title = 'Ridership across U.S.',
                xaxis = dict(title = 'Years'),
                yaxis = dict(title = 'Unlinked Trips (in millions)'),
                )

    fig = dict(data=data, layout = layout)
    return plotly.offline.plot(fig)