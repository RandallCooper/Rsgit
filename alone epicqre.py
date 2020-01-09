import urllib.request
import re


url = "http://www.tl95.com/rihanju/1244.html"


request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

html = response.read()


html = html.decode('gb2312')


u = r'<a rel="external nofollow".*?>'
want = re.findall(u, html)


for each in want:
    print(each)
    with open('4.txt', 'a') as f:
        name = each.split('"')[3].split('》')[0]
        lianjie = each.split('"')[5].split('"')[0]
        f.write(name + '\n' + lianjie + '\n')
