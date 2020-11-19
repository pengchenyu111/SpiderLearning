from bs4 import BeautifulSoup

html = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful Soup演示</title>
    <tag1><a><b></b></a></tag1>
</head>
<body>
<div>
    <ul>
        <li class="item1" value = "hello world">
            <a href="https://geekori.com"> 
                geekori.com
            </a>
        </li>
        <li class="item2"><a href="https://www.jd.com"> 京东商城</a></li>

    </ul>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html,'lxml')
print(soup.head.contents)
print(soup.head.children)
print(type(soup.head.contents))
print(type(soup.body.div.ul.children))
print(type(soup.head.descendants))
for i, child in enumerate(soup.body.div.ul.contents):
    print(i,child)
print('----------')
i = 1
for child in soup.body.div.ul.children:
    print('<', i, '>',child, end=" ")
    i += 1
print('----------')
for i, child in enumerate(soup.body.div.ul.descendants):
    print('[',i,']',child)


