from lxml import etree

parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)
nodes = html.xpath('//li/a')
print('共', len(nodes), '个节点')
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].text, end=' ')

print()
nodes = html.xpath('//ul//a')
print('共', len(nodes), '个节点')
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].text, end=' ')

print()
# 无法找到，因为a不是ul的直接子节点
nodes = html.xpath('//ul/a')
print('共', len(nodes), '个节点')
print(nodes)
