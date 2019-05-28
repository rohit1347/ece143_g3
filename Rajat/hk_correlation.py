
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib qt5

#%%
file = 'table71.xls'
df = pd.read_excel(file, skiprows = 8)
df = df.iloc[2:8]  # For years 2013- 2018
df = df.rename(columns = {'Year/Month':'Years','道路交通意外總宗數 (1)\nTotal Traffic Accidents (1)':'Traffic Accidents'})

#%%
file = 'table21.xls'
data = pd.read_excel(file, sheet_name = 0, skiprows = 5)
data = data.iloc[4:10] ## For years 2013-2018
data = data.rename(columns = {'Unnamed: 10':'Ridership1','小計\nSub-total':'Ridership2'})

#%%
## Traffic Accidents/Ridership correlation
df_new = pd.DataFrame({'Annual Ridership (in thousands)': list(data['Ridership1'].values + data['Ridership2'].values),
                        'Traffic Accidents': list(df['Traffic Accidents'].values)
                    }, index = None)

df_new = df_new.set_index(df['Years'].values)

#%%
#Alternate dataset
file = 'table11.xls'
df_2= pd.read_excel(file, skiprows = 8)
df_2 = df_2.iloc[4:15]  # For years 2007- 2017
df_2 = df_2.rename(columns = {'Unnamed: 2':'Years','交通乘客人次 (1) (3) (4) ':'Avg. daily ridership',
'Casualties Involved in Road Accidents (1)':'Killed','Unnamed: 20':'Injured', 'Unnamed: 22':'Killed1','Unnamed: 23':'Injured1'})

#%%
df_new2 = pd.DataFrame({'Annual Ridership (in thousands)': list(df_2['Avg. daily ridership'].values*365/1000),
                        'Traffic Accidents': list(((df_2['Killed1'].values)+ df_2['Injured1'].values)*7500000/1000)
                    }, index = None)  ## HK population is taken as 7.5 million

df_new2 = df_new2.set_index(df_2['Years'].values)

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

#%%