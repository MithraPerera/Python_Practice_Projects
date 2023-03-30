import csv
import PyPDF2
import re

# Task One: Grab the Google Drive Link from .csv File

data = open('find_the_link.csv', encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

url = ""
i = 0
# for line in data_lines:
#     url += line[i]
#     i += 1
#     if i == 67:
#         break

for row_num, data in enumerate(data_lines):
    url += data[row_num]

print(url)

# Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.

f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
#print(len(pdf_reader.pages))

pattern = r'\d{3}.\d{3}.\d{4}'
all_text = ''

for n in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[n]
    page_text = page.extract_text()
    all_text = all_text + ' ' + page_text

# Regex Search - need to find all the possible matches
for match in re.finditer(pattern, all_text):
    s = match.start()
    e = match.end()
    #print(all_text[s:e])
    print(match.group())