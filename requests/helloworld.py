import requests

r = requests.get('https://www.taobao.com')
# 返回<class 'requests.models.Response'>类
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.cookies)
print(r.text)
