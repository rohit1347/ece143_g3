#%%
import PyPDF2


pdfFileObj = open('2018-APTA-Fact-Book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
pageObj = pdfReader.getPage(28)
# # extracting text from page.
# # this will print the text you can also save that into String
a = pageObj.extractText()

#%%
import tabula
df = tabula.read_pdf('2018-APTA-Fact-Book.pdf')


#%%
import tabula

df = tabula.read_pdf('2018-APTA-Fact-Book.pdf', pages=2, multiple_tables=True)