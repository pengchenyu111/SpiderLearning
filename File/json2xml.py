import json
import dicttoxml

f = open('files/products.json', 'r', encoding='utf-8')
jsonStr = f.read()
# 将JSON字符串转换为字典
d = json.loads(jsonStr)
print(d)
# 将字典转换为XML字符串
xmlStr = dicttoxml.dicttoxml(d).decode('utf-8')
print(xmlStr)
f.close()
