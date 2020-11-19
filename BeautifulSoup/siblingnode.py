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
        <li class="item1" value1="1234" value2 = "hello world">
            <a href="https://geekori.com"> geekori.com</a>
        </li>
        <li class="item2"><a href="https://www.jd.com"> 京东商城</a></li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item4" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item5"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html,'lxml')
secondli = soup.li.next_sibling.next_sibling
print('第1个li节点的下一个li节点：',secondli)
print('第2个li节点的上一个li节点的class属性值：', secondli.previous_sibling.previous_sibling['class'])
for sibling in secondli.next_siblings:
    print(type(sibling))
    if str.strip(sibling.string) == "":
        print('换行')
    else:
        print(sibling)




