from bs4 import BeautifulSoup

html = '''
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
    <button id="button1">确定</button>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>

'''

soup = BeautifulSoup(html,'lxml')
tags = soup.find_all(attrs={"class":"item"})
for tag in tags:
    print(tag)

tags = soup.find_all(class_='item2')
print(tags)
tags = soup.find_all(id='button1')
print(tags)




