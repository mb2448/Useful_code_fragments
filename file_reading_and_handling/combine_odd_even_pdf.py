import os
from PyPDF2 import PdfFileWriter, PdfFileReader 
dirpath = '/Users/Me/Desktop/research/Coronagraphy/Papers/sdc_jatis/comments/'
even = PdfFileReader(open(os.path.join(dirpath, 'all-even-pages.pdf'), 'rb'))
odd = PdfFileReader(open(os.path.join(dirpath, 'all-odd-pages.pdf'), 'rb'))
all = PdfFileWriter()
all.addBlankPage(612, 792)

for x,y in zip(odd.pages, even.pages):
    all.addPage(x)
    all.addPage(y)

while all.getNumPages() % 2:
    all.addBlankPage()

with open(os.path.join(dirpath,'all.pdf'), 'wb') as f:
    all.write(f)

