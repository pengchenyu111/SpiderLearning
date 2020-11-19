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
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item2"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
    <ul>
    <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item4" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item5"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html,'lxml')
ulTags = soup.find_all(name='ul')

print(type(ulTags))
for ulTag in ulTags:
    print(ulTag)
print('---------------------')
for ulTag in ulTags:
    liTags = ulTag.find_all(name='li')
    for liTag in liTags:
        print(liTag)



