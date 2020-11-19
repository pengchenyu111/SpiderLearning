from bs4 import BeautifulSoup
html = '''
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world">
            <a href="https://geekori.com"> geekori.com</a>
        </li>
        <li class="item">
           <a href="https://www.jd.com"> 京东商城</a>
           <a href="https://www.google.com">谷歌</a>
        </li>        
    </ul>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
    </ul>
</div>

'''

soup = BeautifulSoup(html,'lxml')
tags = soup.select('.item')
print(type(tags))
for tag in tags:
    aTags = tag.select('a')
    for aTag in aTags:
        print(aTag['href'],aTag.get_text())

print('---------')
for tag in tags:
    aTags = tag.find_all(name='a')
    for aTag in aTags:
        print(aTag.attrs['href'],aTag.string)