from lxml import etree

parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)
nodes = html.xpath('//*')
print('共', len(nodes), '个节点')
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].tag, end=' ')


# 按层次输出节点
def printNodeTree(node, indent):
    print(indent + node.tag)
    indent += "  "
    children = node.getchildren()
    if len(children) > 0:
        for i in range(0, len(children)):
            printNodeTree(children[i], indent)


print()
printNodeTree(nodes[0], "")
nodes = html.xpath('//a')
print()
print('共', len(nodes), '个<a>节点')
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].text, end=' ')
