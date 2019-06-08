#%%
import camelot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#%%
tables = camelot.read_pdf('123.pdf', pages = '17')     
tables.export('abc.csv', f='csv', compress=False)
table = pd.read_csv('abc-page-17-table-1.csv')
# print(table)
table = table.iloc[0]

def ridership_elec_consumption_corr_hk_plot(table):
    """
    Arguments:
    file {'abc-page-17-table-1.csv'}   
    
    Returns:
        Returns the electricity consumption and ridership data in HK in form of a dataframe which 
        from which correlation plot can be obtained.
    """
    assert isinstance(table,pd.Series)
    # a = list(table.columns[1:11].values)
    df = pd.DataFrame({'Years':table.index[1:], 'Electricity consumption (in kWh)':table.values[1:]})

    df['Electricity consumption (in kWh)'] = df['Electricity consumption (in kWh)'].str.replace(',', '')
    df['Electricity consumption (in kWh)'] = df['Electricity consumption (in kWh)'].astype(int)

    #%%
    ##Total ridership in HK from 2007-2017

    file = 'table11.xls'
    df_2= pd.read_excel(file, skiprows = 8)
    df_2 = df_2.iloc[5:15]  # For years 2007- 2017
    df_2 = df_2.rename(columns = {'Unnamed: 2':'Years','交通乘客人次 (1) (3) (4) ':'Avg. daily ridership',
    'Casualties Involved in Road Accidents (1)':'Killed','Unnamed: 20':'Injured', 'Unnamed: 22':'Killed1','Unnamed: 23':'Injured1'})


    #%%
    df_new2 = pd.DataFrame({'Electricity consumption (in kWh)': list(df['Electricity consumption (in kWh)'].values),
                            'Annual Ridership (in thousands)': list(((df_2['Avg. daily ridership'].values*365/1000)))
                        }, index = None)  ## HK population is taken as 7.5 million

    df_new2 = df_new2.set_index(df['Years'].values)
    return df_new2

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
