from urllib.parse import parse_qs, parse_qsl

query = 'name=王军&age=35'
# 输出{'name': ['王军'], 'age': ['35']}
print(parse_qs(query))
# 输出[('name', '王军'), ('age', '35')]
print(parse_qsl(query))
query = 'name=王军&age=35&name=Bill&age=30'
# 输出{'name': ['王军', 'Bill'], 'age': ['35', '30']}
print(parse_qs(query))
# 输出[('name', '王军'), ('age', '35'), ('name', 'Bill'), ('age', '30')]
print(parse_qsl(query))
