import os

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "http://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]
filename = []
for url in urls:
    filename.append(os.path.basename(url))

count = {}
for freq in filename:
        count[freq] = count.get(freq, 0) + 1

countSorted = sorted(count.items(), key = lambda d:(-d[1], d[0]))
countSorted = countSorted[:3]

dictCount = {}
for l in countSorted:
    dictCount[l[0]] = l[1]
 
for key, value in dictCount.items():
    print(key, value)
