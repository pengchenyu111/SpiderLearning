import requests

r = requests.get('http://t.cn/EfgN7gz')
print(r.text)
with open('Python从菜鸟到高手.png', 'wb') as f:
    f.write(r.content)
