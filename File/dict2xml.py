import dicttoxml
from xml.dom.minidom import parseString
import os

# 定义一个字典
d = [20, 'names',
     {'name': 'Bill', 'age': 30, 'salary': 2000},
     {'name': '王军', 'age': 34, 'salary': 3000},
     {'name': 'John', 'age': 25, 'salary': 2500}]
# 将字典转换为XML格式（bytes形式）
bxml = dicttoxml.dicttoxml(d, custom_root='persons')
# 将bytes形式的XML数据按utf-8编码格式解码成XML字符串
xml = bxml.decode('utf-8')
# 输出XML字符串
print(xml)
# 解析XML字符串
dom = parseString(xml)
# 生成带缩进格式的XML字符串
prettyxml = dom.toprettyxml(indent='   ')
# 创建files目录
os.makedirs('files', exist_ok=True)
# 以只写和utf-8编码格式的方式打开persons.xml文件
f = open('files/persons.xml', 'w', encoding='utf-8')
# 将格式化的XML字符串写入persons.xml文件
f.write(prettyxml)
f.close()
