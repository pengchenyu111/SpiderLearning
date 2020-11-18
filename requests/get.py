import requests

data = {
    'name': 'Bill',
    'country': '中国',
    'age': 20
}
# 如果同时在URL和params参数中指定GET请求的参数，那么ｇｅｔ方法会将参数合并；若出现同名参数，会按顺序保存在列表中
r = requests.get('http://httpbin.org/get?name=Mike&country=美国&age=40', params=data)
print(r.text)
print(r.json())
print(r.json()['args']['country'])
