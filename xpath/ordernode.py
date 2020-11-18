from lxml import etree

parser = etree.HTMLParser()
text = '''
<div>
   <a href="https://geekori.com"> geekori.com</a>
   <a href="https://www.jd.com"> 京东商城</a>
   <a href="https://www.taobao.com">淘宝</a>
   <a href="https://www.microsoft.com">微软</a>
   <a href="https://www.google.com">谷歌</a>
</div>
'''
html = etree.HTML(text)
a1 = html.xpath('//a[1]/text()')
a1 = html.xpath('//a[1]/text()')
a2 = html.xpath('//a[2]/text()')
print(a1, a2)
lasta = html.xpath('//a[last()]/text()')
print(lasta)
aList = html.xpath('//a[position() > 3]/text()')
print(aList)
aList = html.xpath('//a[position() = 2 or position() = last() - 1]/text()')
print(aList)
