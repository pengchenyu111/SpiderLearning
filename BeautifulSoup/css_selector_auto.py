import requests
from bs4 import BeautifulSoup
result = requests.get('https://www.jd.com')
soup = BeautifulSoup(result.text,'lxml')

aTag = soup.select('#navitems-group1 > li.fore1 > a')
print(aTag)
print(aTag[0].string,aTag[0]['href'])
print('---------------')
group1 = soup.select('#navitems-group1')
group2 = soup.select('#navitems-group2')
group3 = soup.select('#navitems-group3')


for value in group1:
    aTags = value.find_all(name="a")
    for aTag in aTags:
        print(aTag.string)

for value in group2:
    aTags = value.find_all(name="a")
    for aTag in aTags:
        print(aTag.string)
for value in group3:
    aTags = value.find_all(name="a")
    for aTag in aTags:
        print(aTag.string)
