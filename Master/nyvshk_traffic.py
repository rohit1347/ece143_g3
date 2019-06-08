
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib qt5

#%%

f = 'NY_crashes.csv'
file1 = 'table11.xls'

#%%
#for accident
def plot_nyvshk_accidents(f,file1):
    """
    
    Arguments:
        f {'NY_crashes.csv'}
        file1 {'table11.xls'}
    
    Returns:
        Returns the NY vs HK Traffic Accidents plot
    """

    assert isinstance(file1,str)
    assert isinstance(f,str)
    import plotly
    import plotly.graph_objs as go

    df_2= pd.read_excel(file1, skiprows = 8)
    df_2 = df_2.iloc[6:15]  # For years 2009- 2017
    df_2 = df_2.rename(columns = {'Unnamed: 2':'Years','交通乘客人次 (1) (3) (4) ':'Avg. daily ridership',
    'Casualties Involved in Road Accidents (1)':'Killed','Unnamed: 20':'Injured', 'Unnamed: 22':'Killed1','Unnamed: 23':'Injured1'})
    df_new2 = pd.DataFrame({'Annual Ridership (in thousands)': list(df_2['Avg. daily ridership'].values*365/1000),
                        'Traffic Accidents': list(((df_2['Killed1'].values)+ df_2['Injured1'].values)*7500000/1000)
                    }, index = None)  ## HK population is taken as 7.5 million

    df_new2 = df_new2.set_index(df_2['Years'].values)

    df_a = pd.read_csv(f)
    df_ny = df_a.iloc[0:9]
    x1 = list(df_ny['YEAR'].values)
    y1 = list(df_ny['Total'].values)
    y11=[]
    for i in y1:
        y11.append(int(i))
    y1 = y11
    y2 = list(df_new2['Traffic Accidents'].values)
    s_1 = []
    s_2 = []
    for i in range(len(y1)-1):
        s_1.append(100*((y1[i+1] - y1[i])/y1[i]))
        s_2.append(100*((y2[i+1] - y2[i])/y2[i]))

    yr = []
    for i in range(len(x1)-1):
        yr.append(x1[i+1])
    trace0 = go.Bar(x = yr,y = s_1, name = 'NY',marker = dict(color = '#c9d9de'))
    trace1 = go.Bar(x = yr,y = s_2, name = 'HK',marker = dict(color = '#718dbf'))
    data = [trace0,trace1]
    layout_1 = dict(title = 'Percentage Change in # of Accidents',
                    xaxis = dict(title = 'Years'),
                    yaxis = dict(title = '# of Accidents change in %')
                    )
    fig = go.Figure(data = data, layout = layout_1)
    return plotly.offline.plot(fig)


#%%
def create_correlation_plot(df):
    """Create seaborn correlation plot for input data frame.

    Arguments:
        df {pd Dataframe} -- Dataframe with index as years and column1=data1 and column2=data2.
    """
    assert isinstance(df,pd.DataFrame)
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

#%%