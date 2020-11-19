from bs4 import BeautifulSoup

html = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful Soup演示</title>
    <tag1><xyz><b></b></xyz></tag1>
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
print(soup.a.parent)
print(soup.a.parent['class'])

print(soup.a.parents)
for parent in soup.a.parents:
    print('<',parent.name,'>')


