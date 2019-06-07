#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

file = '2019-APTA-Fact-Book-Appendix-A.xlsx'

#%%
def emp_compute_plots(file):
    """
    Arguments:
        file {'2019-APTA-Fact-Book-Appendix-A.xlsx'}
    
    Returns:
        Return the employee compensation plots

    """
    assert isinstance(type(file),str)
    df = pd.read_excel(file, sheet_name= '20', skiprows = 3)
    df = df.iloc[44:87]  # For years 1975- 2017
    df['Year'] = pd.to_numeric(df.Year.astype(str).str.replace(',',''), errors='coerce').fillna(float(1984)).astype(int)
    df['Average'] = df['Total Compensation (Millions of Dollars)'].values/df['Number of Employees (Persons) (a)'].values
    x_1 = list(df['Year'].values)
    y_1 = list(df['Number of Employees (Persons) (a)'].values)
    y_2 = list(df['Total Compensation (Millions of Dollars)'].values/100)
    y_3 = list(df['Average'].values*1000)

    import plotly
    import plotly.graph_objs as go

    plotly.offline.init_notebook_mode(connected=True)

    trace0 = go.Scatter(x=x_1,y= y_1,mode = 'lines+markers',name = 'Number of employees')
    trace1 = go.Scatter(x=x_1,y= y_2,yaxis = 'y2', mode = 'lines+markers',name = 'Total Compensation (in ten million dollars)')
    trace2 = go.Scatter(x=x_1,y= y_3, yaxis = 'y2',mode = 'lines+markers',name = 'Average compensation per employee (in thousand of dollars)')

    data = [trace0, trace1, trace2]

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
        title = 'Employee Compensation in Public Transport',
        xaxis = dict(title = 'Years'),
        yaxis = dict(title = 'Number of Employees'),
        yaxis2 = dict(title = 'Employee Compensation (in thousand of dollars)', overlaying='y',side='right')
    )

    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig)
