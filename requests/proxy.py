import requests

proxies = {
    'http': 'http://144.123.68.152:25653',
    'https': 'http://144.123.68.152:25653'
}

r = requests.get('https://www.tmall.com/', proxies=proxies)
print(r.text)
