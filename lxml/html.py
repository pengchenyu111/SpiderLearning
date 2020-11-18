from lxml import etree

parser = etree.HTMLParser()
print(type(parser))
tree = etree.parse('test.html', parser)
root = tree.getroot()
result = etree.tostring(root, encoding='utf-8',
                        pretty_print=True, method="html")
print(str(result, 'utf-8'))
print(root.tag)
print('lang =', root.get('lang'))
print('charset =', root[0][0].get('charset'))
print('charset =', root[0][1].text)
