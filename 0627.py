import requests
from bs4 import BeautifulSoup
import json
import re
import csv
import codecs

url = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/397863_indicators.txt"
req = requests.get(url, headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36"
})
data = json.loads(req.text)

def remove_tag(html):
    text = re.sub('<.*?>', '', html, re.S)
    return text

def data_print(key, d, row):
    if key in d:
        clear_d = remove_tag(d[key])
        if clear_d:
            row.append(clear_d)
        else:
            row.append('None')
    else:
        row.append('None')

with open("data.csv","wb") as datacsv:
    datacsv.write(codecs.BOM_UTF8)

with open('data.csv', 'a', newline='') as csvfile:
    title = ['UNIVERSITY', 'OVERALL SCORE', 'ACADEMIC REPUTATION', 'EMPLOYER REPUTATION', 'FACULTY STUDENT', 'INTERNATIONAL FACULTY', 'INTERNATIONAL STUDENTS', 'CITATIONS PER FACULTY']
    writer = csv.writer(csvfile)
    writer.writerow(title)

for num in range(0,1020):
    reup = data['data'][num]
    
    row = []
    data_print('uni', reup, row)
    data_print('overall', reup, row)
    data_print('3225601', reup, row)
    data_print('3225602', reup, row)
    data_print('3225603', reup, row)
    data_print('3225604', reup, row)
    data_print('3225605', reup, row)
    data_print('3225606', reup, row)

    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)
