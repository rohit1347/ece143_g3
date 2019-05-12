# %%
import camelot
import pandas as pd
# %%
tables = camelot.read_pdf('APTA_2004_Fact_Book.pdf',
                          pages='75,76,77,78,79,80,81')
print(tables)
tables.export('apta2004.csv', f='csv', compress=True)
print(tables[0])
print(tables[0].parsing_report)
for table in range(len(tables)):
    tables[table].to_csv('apta2004_' + str(table) + '.csv')

# %%
table0 = pd.read_csv('apta2004_0.csv', sep='\n')
table0.head(-1)

# %%
table1 = pd.read_csv('apta2004_1.csv', sep='\n')
table1.head(-1)


# %%
