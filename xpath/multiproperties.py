from lxml import etree

# 多属性匹配，主要就是用好and or 等运算符
# 注意大小写敏感，AND OR 不起作用

parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)

aList = html.xpath('//a[@href="https://www.jd.com" or @href="https://geekori.com"]')
for a in aList:
    print(a.text, a.get('href'))

#  <li class="item4" value="1234"><a href="https://www.microsoft.com">微软</a></li>
print('----------------')
aList = html.xpath('//a[contains(@href,"www") and ../@value="1234"]')
for a in aList:
    print(a.text, a.get('href'))
