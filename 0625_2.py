import csv
import codecs
import requests
from bs4 import BeautifulSoup

with open("data4.csv","wb") as datacsv:
    datacsv.write(codecs.BOM_UTF8)

with open('data4.csv', 'a', newline='') as csvfile3:
    title = ['Name', 'Scholarly Output', 'Most recent publication', 'Citations', 'Citations per Publication', 'Field-Weighted Citation Impact', 'h-index', 'Scopus author ID', 'Scopus author profile', '系所']
    writer = csv.writer(csvfile3)
    writer.writerow(title)

with open('data2.csv', 'r', encoding="utf8", errors='ignore', newline = '') as csvfile2:
    rows = csv.reader(csvfile2)
    
    for row in rows:
        url = "https://www.google.com.tw/search"
        t_name = row[0] + '中山'
        params = {'q': t_name}
        req = requests.get(url, params, headers={
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36"
        })
        soup = BeautifulSoup(req.text, 'lxml')

        reup = soup.select('.st')
        if reup:
            for reu in reup:
                if '指導教授(外文)' in reu.text and '系所名稱' in reu.text:
                    row.append(reu.text)
        else:
            row.append('notFind')

        with open('data4.csv', 'a', newline='') as csvfile3:
            writer = csv.writer(csvfile3)
            writer.writerow(row)
