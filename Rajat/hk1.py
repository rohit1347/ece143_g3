# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib qt5

file = 'table21.xls'
data = pd.read_excel(file, sheet_name = 0, skiprows = 5)
data.head(10)

# %%
# data = data.iloc[0:5]
# data

# data.plot(kind='bar', x='Year', y='Sub-total')

# data.plot(kind='bar',x='Year',y='Sub-total.1')
# plt.show()

# %%

data_1= data.iloc[4:9]
# data_1.rename(columns = {' 年 / 月':'Year'})
fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()

width = 0.3

ax.set_ylim([1200000,1500000])
ax2.set_ylim([1800000,2050000])

# data_1.plot(kind='bar', x=data_1.columns[0], y=data_1.columns[10])
# plt.show()

# data_1.plot(kind='bar', x=data_1.columns[0], y=data_1.columns[15])
# plt.show()

data_1.plot(kind='bar', x=data_1.columns[0], y=data_1.columns[10], color = 'red', width = width, ax=ax, position = 1)
data_1.plot(kind='bar', x=data_1.columns[0], y=data_1.columns[15], color = 'blue', width = width, ax=ax2, position = 0)

ax.set_ylabel('Buses')
ax2.set_ylabel('Railways')
ax.set_xlabel('Year')

ax.get_legend().remove()
ax2.get_legend().remove()

ax.grid(False)
ax2.grid(False)

plt.show()

# %%


#%%


