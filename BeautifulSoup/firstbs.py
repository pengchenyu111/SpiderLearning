from bs4 import BeautifulSoup

html = '''
<html>
    <head><title>这是一个演示页面</title></head>
    <body>
        <a href='a.html'>第一页</a>
        <p>
        <a href='b.html'>第二页</a>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
# 获取title标签内的值
print('<' + soup.title.string + '>')
# 获取第一个a标签的href属性值
print('[' + soup.a["href"] + ']')
print(soup.prettify())
