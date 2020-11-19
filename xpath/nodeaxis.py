from lxml import etree

parser = etree.HTMLParser()
text = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>XPath演示</title>
</head>
<body class="item">
<div>
    <ul class="item" >
        <li class="item1"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item2"><a href="https://www.jd.com">京东商城</a>
                            <value url="https://geekori.com"/>
                            <value url="https://www.google.com"/>
        </li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a>
                          <a href="https://www.tmall.com/">天猫</a></li>
        <li class="item4" value="1234"><a href="https://www.microsoft.com">微软</a></li>
        <li class="item5"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
</body>
</html>
'''

# 获取所有祖先结点
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
for value in result:
    print(value.tag, end=' ')

print()

# 获取所有属性class为item的祖先结点
result = html.xpath('//li[1]/ancestor::*[@class="item"]')
for value in result:
    print(value.tag, end=' ')

print()
# 获取当前结点的所有属性值
result = html.xpath('//li[4]/attribute::*')
print(result)

# 获取当前节点的所有子节点
result = html.xpath('//li[3]/child::*')
for value in result:
    print(value.get('href'), value.text, end=' ')
print()

# 选取当前节点的所有名为value的后代
result = html.xpath('//li[2]/descendant::value')
for value in result:
    print(value.get('url'), end=' ')
print()

# 选取当前节点的结束标签之后的所有节点
result = html.xpath('//li[1]/following::*')
for value in result:
    print(value.tag, end=' ')
print()

result = html.xpath('//li[1]/following::*[position() > 4]')
for value in result:
    print(value.tag, end=' ')
print()

# 选取文档中当前节点的结束标签之后的所有同级的节点
result = html.xpath('//li[1]/following-sibling::*')
for value in result:
    print(value.tag, end=' ')
print()
