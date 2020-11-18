import requests
from urllib.parse import quote, unquote

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    # 将中文编码
    'name': quote('李宁')
}

r = requests.get('http://httpbin.org/get', headers=headers)
print(r.text)
print('Name:', unquote(r.json()['headers']['Name']))
