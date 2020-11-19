from bs4 import BeautifulSoup

html = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful Soup演示</title>
</head>
<body>
<div>
    <ul>
        <li class="item1"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
</div>
</body>
</html>
'''
# 获得的每一个结点都是<class 'bs4.element.Tag'>对象，可以继续选取
soup = BeautifulSoup(html, 'lxml')
# 选取head结点
print(soup.head)
print(type(soup.head))
head = soup.head
print(head.title.string)
print(soup.body.div.ul.li.a['href'])
