import requests

data = {
    'name': 'Bill',
    'country': '中国',
    'age': 20
}

r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
print(r.json())
print(r.json()['form']['country'])
