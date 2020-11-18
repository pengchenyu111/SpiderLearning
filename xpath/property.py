from lxml import etree

# 根据属性过滤，则要将属性放于[...]中
# 不放在其中表示获取该属性值

parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)
nodes = html.xpath('//a[@href="https://geekori.com"]')
print('共', len(nodes), '个节点')

for i in range(0, len(nodes)):
    print(nodes[i].text)

# contain函数参数1表示待匹配的值，参数2是被包含的字符串

# 选取所有href属性包含www的a的结点
nodes = html.xpath('//a[contains(@href,"www")]')
print('共', len(nodes), '个节点')

for i in range(0, len(nodes)):
    print(nodes[i].text)

# 获取所有(所有href属性包含www的a结点)的href属性
urls = html.xpath('//a[contains(@href,"www")]/@href')

for i in range(0, len(urls)):
    print(urls[i])
