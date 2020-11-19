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
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item4" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item5"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
# 获取节点的名称，注意是名称，不是标签之间的值
print(soup.title.name)
# 获取第一个li结点的所有属性名和属性值
print(soup.li.attrs)
# 获取第一个属性名为value2的li节点的属性值
print(soup.li.attrs["value2"])
# 获取第一个属性名为value1的li节点的属性值
print(soup.li["value1"])
# 获取第一个a标签内的href的值
print(soup.a['href'])
# 获取第一个a标签的文本值
print(soup.a.string)
