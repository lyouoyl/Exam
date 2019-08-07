from selenium import webdriver
from bs4 import BeautifulSoup
import codecs

driver = webdriver.Chrome()
driver.get("https://www.topuniversities.com/university-rankings/world-university-rankings/2019")

import csv
with open("data.csv","wb") as datacsv:
    datacsv.write(codecs.BOM_UTF8)

with open('data.csv', 'a', newline='') as csvfile:
    title = ['學校', 'Total students', 'International students', 'Total faculty stuff', 'International stuff']
    writer = csv.writer(csvfile)
    writer.writerow(title)

    for p in range(0,40):
        paths = driver.find_elements_by_xpath("//a[@class='more']")
        amount = len(paths)

        for i in range(0,amount):
            path = paths[i]
            url = path.get_attribute('href')

            import urllib.request as req
            import ssl
            ssl._create_default_https_context = ssl._create_unverified_context
            request = req.Request(url, headers={
                "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36"
            })
            with req.urlopen(request) as response:
                data = response.read().decode("utf-8")
            
            soup = BeautifulSoup(data, 'lxml')

            elements = []
            for ele in soup.select('header h1'):
                elements.append(ele.string)
            
            num = {}
            for ele in soup.select('#data h4'):
                if ele.string:
                    temp = ele.string.split(" - ", 1)
                    num[temp[0]] = temp[1]
            if 'Total students' in num:
                elements.append(num['Total students'])
            else:
                elements.append('None')
            
            for ele in soup.select('#data h4'):
                if ele.string:
                    temp = ele.string.split(" - ", 1)
                    num[temp[0]] = temp[1]
            if 'International students' in num:
                elements.append(num['International students'])
            else:
                elements.append('None')      
            
            for ele in soup.select('#data h4'):
                if ele.string:
                    temp = ele.string.split(" - ", 1)
                    num[temp[0]] = temp[1]
            if 'Total faculty staff' in num:
                elements.append(num['Total faculty staff'])
            else:
                elements.append('None')
                
            div1 = []
            div2 = []
            for ele in soup.select('#data div label'):
                if ele.string != None:
                    div1.append(ele.string)
            for ele in soup.select('#data div > div'):
                if ele.string != None:
                    div2.append(ele.string)
            if div1 and div2:
                num[div1[-1]] = div2[-1]
            if 'International staff' in num:         
                elements.append(num['International staff'])
            else:
                elements.append('None')
            
            writer = csv.writer(csvfile)
            writer.writerow(elements)

        q = driver.find_element_by_xpath("//a[@class='paginate_button next']")
        from selenium.webdriver.common.keys import Keys
        q.send_keys(Keys.RETURN)
