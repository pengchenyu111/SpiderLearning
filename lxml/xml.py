from lxml import etree

tree = etree.parse('products.xml')
print(type(tree))
print(str(etree.tostring(tree, encoding="utf-8"), 'utf-8'))
root = tree.getroot()
print(type(root))
print('root：', root.tag)
children = root.getchildren()
print('--------------输出产品信息--------------')
for child in children:
    print('product id = ', child.get('id'))
    print('child[0].name = ', child[0].text)
    print('child[1].price = ', child[1].text)

root = etree.fromstring('''
<products> 
    <product1 name="iPhone"/>
    <product2 name="iPad"/>
</products>
''')

print('------------新产品------------')

print('root =', root.tag)
children = root.getchildren()
for child in children:
    print(child.tag, 'name = ', child.get('name'))
