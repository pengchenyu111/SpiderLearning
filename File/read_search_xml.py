from xml.etree.ElementTree import parse

# 开始分析products.xml文件，files/products.xml是要读取的XML文件的名字
doc = parse('files/products.xml')
# 通过XPath搜索子节点集合，然后对这个子节点集合进行迭代
for item in doc.iterfind('products/product'):
    # 读取product节点的id子节点的值
    id = item.findtext('id')
    # 读取product节点的name子节点的值
    name = item.findtext('name')
    # 读取product节点的price子节点的值
    price = item.findtext('price')
    # 读取product节点的uuid属性的值
    print('uuid', '=', item.get('uuid'))
    print('id', '=', id)
    print('name', '=', name)
    print('price', '=', price)
    print('-------------')
