import os
from PyPDF2 import PdfFileReader, PdfFileWriter

folder = 'BostonCityBudgets/FY16'
names = []
paths = []

with os.scandir(folder) as it:
    for entry in it:
        if entry.name.endswith(".pdf") and entry.is_file():
            names.append(entry.name)
            paths.append(entry.path)

print(paths)
n = 0

for path in paths:
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf.getPage(2))
    output_name = 'page_3_{}'.format(names[n])
    with open('BostonCityBudgets/FY16/' + output_name, 'wb') as out:
        pdf_writer.write(out)
    n += 1
