import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import codecs

url = "http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/"
req = requests.get(url, headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36"
})
soup = BeautifulSoup(req.text, 'lxml')

def page_source(area, subject, sub):
    url = "http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/{0}"
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url.format(sub))

    soup = BeautifulSoup(driver.page_source, 'lxml')
    temp = soup.select('tbody tr')
    countery = soup.select('tbody tr td img')
    length = len(temp)

    for i in range(0,length-1):
        row = []
        row.append(area)
        row.append(subject)
        for tem in temp[i+1]:
            if tem.text:
                row.append(tem.text)
            else:
                row.append('None')

        cou1 = countery[i]['src'].split('../image/flag/')
        cou2 = cou1[1].split('.png')
        row.append(cou2[0])

        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row)



with open("data.csv","wb") as datacsv:
    datacsv.write(codecs.BOM_UTF8)

temp_ns = soup.select('.subject-ns')
for tem in temp_ns:
    page_source('Natural Sciences', tem.text, tem['href'])

temp_eng = soup.select('.subject-eng')
for tem in temp_eng:
    page_source('Engineering', tem.text, tem['href'])

temp_life = soup.select('.subject-life')
for tem in temp_life:
    page_source('Life Sciences', tem.text, tem['href'])

temp_med = soup.select('.subject-med')
for tem in temp_med:
    page_source('Medical Sciences', tem.text, tem['href'])

temp_soc = soup.select('.subject-soc')
for tem in temp_soc:
    page_source('Social Sciences', tem.text, tem['href'])
