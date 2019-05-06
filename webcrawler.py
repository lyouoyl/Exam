import urllib.request as req
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.ptt.cc/bbs/movie/index.html"
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")

for title in titles:
    if title.a != None:
        u = "https://www.ptt.cc"+ title.a["href"]
        u_request = req.Request(u, headers={
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"
        })
        with req.urlopen(u_request) as response:
            u_data = response.read().decode("utf-8")

        import bs4
        u_root = bs4.BeautifulSoup(u_data, "html.parser")
        outputs = u_root.find_all("span", class_="article-meta-value")
        for output in outputs:
            print(output.string)
        contents = u_root.find("div", class_="bbs-screen bbs-content")
        for content in contents:
            if content.string != None:
                print(content.string)
