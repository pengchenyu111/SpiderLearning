import xmltodict

# 打开products.xml文件
f = open('files/products.xml', 'rt', encoding="utf-8")
# 读取products.xml文件中的所有内容
xml = f.read()
# 分析XML字符串，并转化为字典
d = xmltodict.parse(xml)
# 输出字典内容
print(d)
f.close()
import pprint

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(d)
