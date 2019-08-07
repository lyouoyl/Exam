import csv
import codecs
from bs4 import BeautifulSoup
from selenium import webdriver

with open("data2.csv","wb") as datacsv:
    datacsv.write(codecs.BOM_UTF8)

with open('data2.csv', 'a', newline='') as csvfile2:
    title = ['Name', 'Scholarly Output', 'Most recent publication', 'Citations', 'Citations per Publication', 'Field-Weighted Citation Impact', 'h-index', 'Scopus author ID', 'Scopus author profile', '系所']
    writer = csv.writer(csvfile2)
    writer.writerow(title)

with open('data1.csv', 'r', encoding="utf8", errors='ignore', newline = '') as csvfile1:
    rows = csv.reader(csvfile1)
    driver = webdriver.PhantomJS(executable_path='/Users/mingyu/phantomjs-2.1.1-macosx/bin/phantomjs')

    for row in rows:
        url = row[8]
        driver.get(url)
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, "lxml")

        temp = soup.select('.authAffilcityCounty')
        if temp:
            reup = temp[0].text.strip()
        else:
            reup = 'None'
        
        school_name = ('National Sun Yat-Sen University')
        if school_name in reup:
            row.append('中山教授')
        elif reup == 'None':
            row.append('None')
        else:
            row.append('非中山教授')
        
        with open('data2.csv', 'a', newline='') as csvfile2:
            writer = csv.writer(csvfile2)
            writer.writerow(row)
    driver.close()
