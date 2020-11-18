from lxml import etree

parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)

# 选取href属性为https://www.jd.com的所有a结点的父节点，并输出class属性值
result = html.xpath('//a[@href="https://www.jd.com"]/../@class')
print('class属性 =', result)
# 选取href属性为https://www.jd.com的所有a结点的父节点，并输出class属性值
result = html.xpath('//a[@href="https://www.jd.com"]/parent::*/@class')
print('class属性 =', result)
