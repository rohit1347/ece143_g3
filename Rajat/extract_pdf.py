#%%
import camelot
import pandas as pd

tables = camelot.read_pdf('2018-APTA-Fact-Book.pdf', pages = '28')     
tables.export('apta2018.csv', f='csv', compress=False)

table = pd.read_csv('apta2018-page-28-table-1.csv')
table.head()
#%%
