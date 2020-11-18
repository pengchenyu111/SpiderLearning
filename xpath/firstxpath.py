from lxml import etree

parser = etree.HTMLParser()
tree = etree.parse('test.html', parser)
titles = tree.xpath('/html/head/title')
if len(titles) > 0:
    print(titles[0].text)

html = '''
<div>
    <ul>
        <li class="item1"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item2"><a href="https://www.jd.com"> 京东商城</a></li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
    </ul>
</div>
'''
tree = etree.HTML(html)
aTags = tree.xpath("//li[@class='item2']")
if len(aTags) > 0:
    print(aTags[0][0].get('href'), aTags[0][0].text)
# https://www.jianshu.com/p/2ae6d51522c3
