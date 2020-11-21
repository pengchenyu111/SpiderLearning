import json

# 建议使用load函数，因为eval可执行任何Python代码，若字符串中有代码，则可能带来风险

# 定义一个字典
data = {
    'name': 'Bill',
    'company': 'Microsoft',
    'age': 34
}
# 将字典转换为JSON字符串
jsonStr = json.dumps(data)
# 输出jsonStr变量的类型
print(type(jsonStr))
# 输出JSON字符串
print(jsonStr)
# 将JSON字符串转换为字典
data = json.loads(jsonStr)
print(type(data))
# 输出字典
print(data)
# 定义一个JSON字符串
s = '''
{
    'name' : 'Bill',
    'company' : 'Microsoft',
    'age' : 34
}
'''
# 使用eval函数将JSON字符串转换为字典
data = eval(s)
print(type(data))
print(data)
# 输出字典中的key为company的值
print(data['company'])
# 打开products.json文件
f = open('files/products.json', 'r', encoding='utf-8')
# 读取products.json文件中的所有内容
jsonStr = f.read()
# 使用eval函数将JSON字符串转换为字典
json1 = eval(jsonStr)
# 使用loads函数将JSON字符串转换为字典
json2 = json.loads(jsonStr)
print(json1)
print(json2)
print(json2[0]['name'])
f.close()
