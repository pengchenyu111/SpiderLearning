from requests import Request, Session

url = 'http://httpbin.org/post'

data = {
    'name': 'Bill',
    'age': 30
}
headers = {
    'country': 'China'
}

session = Session()
req = Request('post', url, data=data, headers=headers)
prepared = session.prepare_request(req)
r = session.send(prepared)
print(type(r))
print(r.text)
